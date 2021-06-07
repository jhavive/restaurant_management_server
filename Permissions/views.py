from rest_framework import viewsets
from rest_framework.response import Response
import json
from django.core import serializers
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

class PermissionsViewSet(viewsets.ViewSet):

    def list(self, request):
        per = Permission.objects.all()
        permissions_dict = json.loads(serializers.serialize('json', per))
        permissions = []
        for p in per:
            permissions.append(p.name)
        return Response(permissions)

    def create(self, request):
        return Response({
            "url": 'partial_update'
        })

    def retrieve(self, request, pk=None):
        return Response({
            "url": 'partial_update'
        })

    def update(self, request, pk=None):
        return Response({
            "url": 'partial_update'
        })

    def partial_update(self, request, pk=None):
        try:
            User = get_user_model()
            user = User.objects.get(pk=pk)
            req = json.loads(request.body)
            requested_permissions = req.get('permission_list')
            permissions = []
            for per in requested_permissions:
                print(per)
                permission = Permission.objects.filter(name=per).first()
                user.user_permissions.add(permission)

            # print(permissions)
            # user.user_permissions.set(permissions)
            return Response({
                "message": "Updated Successfully",
                "status": True
            })
        except Exception as e:
            print(e)
            return Response({
                "message": "Unable Tp Update",
                "status": False
            }, status=400)

    def destroy(self, request, pk=None):
        return Response({
            "url": 'partial_update'
        })

