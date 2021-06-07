from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
import json
from bson.objectid import ObjectId
from bson import json_util
from django.core import serializers
from django.contrib.auth.models import Permission
from custom_user.models import Organization
from django.contrib.auth import get_user_model

class UsersViewSet(viewsets.ViewSet):

    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True
        return super(UsersViewSet, self).has_permission(request, view)

    def list(self, request):
        org = Organization.objects.get(pk=request.user.organization.id)
        print("LeadsViewSet org" + str(org))
        User = get_user_model()
        users = User.objects.filter(organization=org)
        user_response = []
        for user in users:
            temp                    =   {}
            temp['id']              =   user.pk
            temp['last_login']      =   user.last_login
            temp['last_login']      =   user.last_login
            temp['is_superuser']    =   user.is_superuser
            temp['username']        =   user.username
            temp['is_active']       =   user.is_active
            temp['date_joined']     =   user.date_joined
            user_permission         =   []
            permissions             =   Permission.objects.filter(user=user)

            for up in permissions:
                user_permission.append(up.name)
            temp['user_permissions'] = user_permission
            user_response.append(temp)
        return Response(user_response)

    def create(self, request):
        try:
            # Get request data
            req = json.loads(request.body)
            # print(req)
            org = request.user.organization.id
            print(org)
            organisation = Organization.objects.get(pk=org)

            # Save User
            User = get_user_model()
            new_user = User.objects.create_superuser(
                            username        =   req.get('username'),
                            password        =   req.get('password'),
                            email           =   req.get('email'),
                            first_name      =   req.get('first_name'),
                            last_name       =   req.get('last_name'),
                            organization    =   organisation)
            print(new_user)
            return Response({
                "message": "User Created",
                "status": True,
                "id": str(new_user.id)
            })

        except Exception as e:
            print(e)
            return Response({
                "message": "User Could'nt be Created",
                "status": False
            }, status=400)

    def retrieve(self, request, pk=None):
        print("retrieve")
        org = Organization.objects.get(pk=request.user.organization.id)
        print("LeadsViewSet org" + str(org))
        User = get_user_model()
        user = User.objects.filter(organization=org,pk=pk)[0]
        temp = {}
        temp['id'] = user.pk
        temp['last_login'] = user.last_login
        temp['last_login'] = user.last_login
        temp['is_superuser'] = user.is_superuser
        temp['username'] = user.username
        temp['is_active'] = user.is_active
        temp['date_joined'] = user.date_joined
        user_permission = []
        permissions = Permission.objects.filter(user=user)
        for up in permissions:
            user_permission.append(up.name)
        temp['user_permission'] = user_permission

        return Response(temp)

    def update(self, request, pk=None):
        return Response({
            "url": 'update'
        })

    def partial_update(self, request, pk=None):
        return Response({
            "url": 'partial_update'
        })

    def destroy(self, request, pk=None):
        try:
            User = get_user_model()
            org = Organization.objects.get(pk=str(request.user.organization.id))
            u = User.objects.get(pk=pk, organization=org)
            u.delete()
            return Response({
                "message": "User Deleted",
                "status": True
            })
        except User.DoesNotExist:
            return Response({
                "message": "User couldnt be found",
                "status": False
            }, status=400)

        except Exception as e:
            return Response({
                "message": "Some Error ocured",
                "status": False
            }, status=500)


    @action(detail=True, methods=['get'])
    def leads_in_module(self, request, pk=None):
        return Response({
            "url": 'custom '+pk
        })
