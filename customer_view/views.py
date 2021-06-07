from django.shortcuts import render
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from admin_view.models import Menu, Section, Items, Order, OrderItemMap, Tables
from custom_user.models import Organization

# Create your views here.
@api_view(['GET',])
def fetchMenu(request):
    print(request.GET.get('hotel'))
    hotel       =   Organization.objects.get(pk=str(request.GET.get('hotel')))
    print(hotel)
    menu        =   Menu.objects.get(hotel=hotel)
    print(menu)
    sections    =   Section.objects.filter(menu=menu)
    response    =   []
    for section in sections:
        temp    =   {}
        items   =   Items.objects.filter(section=section)

        temp['section_name']    =   section.name
        temp['items']           =   []

        for item in items:
            temp['items'].append({
                "id"            :   item.pk,
                "item_name"     :   item.name,
                "description"   :   item.description,
                "price"         :   item.price
            })

        response.append(temp)

    return Response(response)


@api_view(['POST',])
def placeOrder(request):
    try:
        req = json.loads(request.body)
        table = Tables.objects.get(pk=req.get('table'))
        order = Order(table=table, state="active", read=False)
        order.save()

        for item in req.get('order_items'):
            temp = Items.objects.get(pk=item.get('item').get('id'))
            quantity = item.get('quantity')
            oi = OrderItemMap(order=order, item=temp, quantity=quantity)
            oi.save()

        return Response({
            "message": "Order Placed Successfully",
            "status": True
        })
    except Exception as e:
        print(e)
        return Response({
            "message": "Some Error Occured",
        }, status=500)