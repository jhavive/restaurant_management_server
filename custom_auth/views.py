import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from .token import MyOwnToken
from custom_user.models import Organization
from django.contrib.auth.models import Permission
from utils.routing import permission_to_route
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer



# Create your views here.
@csrf_exempt
@api_view(['POST', 'OPTIONS'])
def login(request):
    if request.method == 'OPTIONS':
        print("wassup")
        response = HttpResponse()
        response['allow'] = 'post'
        return response
    req = json.loads(request.body)
    username = req.get('username')
    password = req.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        print(user.organization)
        org = Organization.objects.get(name=user.organization.name)
        token, _ = MyOwnToken.objects.get_or_create(user=user, company=org)
        return Response({
            "message": "Successfully Logged In",
            "success": True,
            "token": str(token),
            "organization": user.organization.id
        })
    else:
        return Response({
            "message": "Incorrect Username or Password",
            "success": False,
        }, status=400)

@csrf_exempt
@api_view(['GET','OPTIONS'])
def get_routes(request):
    if request.method == 'OPTIONS':
        print("wassup")
        response = HttpResponse()
        response['allow'] = 'get'
        return response
    # permissions = Permission.objects.filter(user=request.user)
    permissions = Permission.objects.all()
    return Response(permission_to_route(permissions))
