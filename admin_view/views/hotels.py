from rest_framework import viewsets
import json
from rest_framework.response import Response

class HotelsViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response({
            "message": "Hello"
        })
        # req = json.loads(request)
        # try:
        #     # hotel = Hotels.objects.filter(pk=req.get('id'))
        #     hotels      =    Hotels.objects.all()
        #     response    =    []
        #     for hotel in hotels:
        #         response.append({
        #             "id"    :   hotel.pk,
        #             "name"  :   hotel.name
        #         })
        #
        #     return Response(response)
        # except Exception as e:
        #     print(e)
        #     return Response({
        #         "message": "Entry Not Found"
        #     }, status=400)

    # def create(self, request):
    #     req     =   json.loads(request)
    #     try:
    #         new_hotel =  Hotels(name=req.get("name"))
    #         new_hotel.save()
    #         return Response({
    #             id: new_hotel.pk
    #         })
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             "message": 'Some Error Occured',
    #             "status": False
    #         }, status=400)

