from rest_framework import viewsets
import json
from itertools import repeat
from rest_framework.response import Response
from admin_view.models import Order, Tables, OrderItemMap, Items
from django.db.models import Q

class OrdersViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            hotel       =   request.user.organization
            print(hotel)
            tables      =    Tables.objects.filter(hotel=hotel)
            print(tables)
            response       =    {}
            for table in tables:
                print(table.number)
                orders      =    Order.objects.filter(table=table).filter(~Q(state='inactive'))
                response[table.pk] = {}
                for order in orders:
                    response[table.pk][order.pk] = []
                    order_items   =   OrderItemMap.objects.filter(order=order)
                    order_response = []
                    for order_item in order_items:
                        items_json = {
                            "table": table.pk,
                            "name": order_item.item.name,
                            "price": order_item.item.price,
                            "quantity": order_item.quantity
                        }
                        order_response.append(items_json)
                    response[table.pk][order.pk] = {
                        "state": order.state,
                        "items": order_response,
                        "read": order.read
                    }

            return Response(response)
        except Exception as e:
            print(e)
            return Response({
                "message": "Entry Not Found"
            }, status=400)

    def partial_update(self, request, pk):
        try:
            req = json.loads(request.body)
            print(req)
            for o in req.get('orders'):
                order = Order.objects.get(pk=o)
                if(req.get('read')):
                    order.read = req.get('read')
                    order.save(update_fields=["read"])
                if(req.get('state')):
                    order.state = req.get('state')
                    order.save(update_fields=["state"])
            return Response({
                "message": "Successfully done",
                "status": True
            })

        except Exception as e:
            print(e)
            return Response({
                "message": "Successfully done",
                "status": True
            })
