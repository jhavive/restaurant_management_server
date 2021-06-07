from rest_framework import viewsets
import json
from rest_framework.response import Response
from admin_view.models import Menu, Section, Items

class MenuViewSet(viewsets.ViewSet):

    # def list(self, request):



    def list(self, request, pk=None):
        try:
            menu            =   {}
            sections        =   []
            response        =   []
            try:
                menu        =   Menu.objects.get(hotel=request.user.organization)
                sections    =   Section.objects.filter(menu=menu)
            except Exception as e:
                print(e)

            for section in sections:
                section_items = []
                items   =   Items.objects.filter(section=section)
                for item in items:
                    section_items.append({
                        "id"            :    item.pk,
                        "item_name"          :    item.name,
                        "description"   :    item.description,
                        "price"         :    item.price,
                        # "non_veg"       :    item.non_veg,
                        "tags"          :    item.tags,
                    })
                response.append({
                    "section_name"  :   section.name,
                    "items" :   section_items
                })

            return Response(response)
        except Exception as e:
            print(e)
            return Response({
                "message": "Somerror occured"
            }, status=500)

    def create(self, request):
        try:
            req         =   json.loads(request.body)
            hotel       =   request.user.organization
            menu        =   Menu.objects.get_or_create(hotel=hotel)
            menu        =   Menu.objects.get(hotel=hotel)

            sections    =   Section.objects.filter(menu=menu).delete()
            items       =   Items.objects.filter(menu=menu).delete()

            print(req)
            for section in req.get('sections'):
                new_section     =   Section(name=section.get('section_name'), menu=menu)
                new_section.save()
                for item in section.get('items'):
                    new_item    =   Items(
                                        name            =   item.get('item_name'),
                                        description     =   item.get('description'),
                                        price           =   item.get('price'),
                                        menu            =   menu,
                                        section         =   new_section,
                                        hotel           =   hotel
                                    )
                    new_item.save()
            return Response({
                "message": "Successfully Created A new Menu",
                "status": True
            })

        except Exception as e:
            print(e)
            return Response({
                "message": 'Some Error Occured',
                "status": False
            }, status=400)

