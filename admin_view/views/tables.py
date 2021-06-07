from rest_framework import viewsets
import json
from itertools import repeat
from rest_framework.response import Response
from admin_view.models import Tables
from utils.qr import saveQRCode

class TablesViewSet(viewsets.ViewSet):

    def list(self, request):
        print("organization",request.user.organization)
        try:
            tables      =    Tables.objects.all()
            response    =    []
            for table in tables:
                response.append({
                    "id"            :   table.pk,
                    "number"        :   table.number,
                    "capacity"      :   table.capacity
                })

            return Response(response)
        except Exception as e:
            print(e)
            return Response({
                "message": "Entry Not Found"
            }, status=400)

    def create(self, request):
        req     =   json.loads(request.body)
        try:
            hotel       =   request.user.organization
            new_tables  =   []
            # table_number
            index = 1

            for table in repeat(0, int(req.get("number_of_table"))):
                new_tables.append(Tables(number=index, capacity=req.get('table_quantity'), hotel=hotel))
                index = index + 1

            tables = Tables.objects.bulk_create(new_tables)

            for table in tables:
                saveQRCode(hotel.pk, table.pk)

            return Response({
                "message": "Successfully Added",
                "status": True
            })
        except Exception as e:
            print(e)
            return Response({
                "message": 'Some Error Occured',
                "status": False
            }, status=400)

