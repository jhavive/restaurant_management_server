from rest_framework import permissions


rest_to_operation = {
    'POST':" add",
    "GET":" view",
    "PUT":" change",
    "PATCH": " change",
    "DELETE": "delete"
}

class UserAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print("UserAccessPermission "+request.path)
        if(request.method!='OPTIONS'):
            if (request.path=='/login/' or request.path=='/login') and (request.method=='POST'):
                return True
            elif 'fetch-menu' in request.path and request.method=='GET':
                return True
            elif 'qr' in request.path and request.method == 'GET':
                return True
            elif 'place-order' in request.path and request.method == 'POST':
                return True
            else:
                if request.META.get('HTTP_AUTHORIZATION') and request.META.get('HTTP_X_ORG_ID'):
                    path = request.path
                    path.split('/')
                    app_name = path.split('/')[1]
                    model_name = path.split('/')[2]
                    perm = app_name+'.'+rest_to_operation[request.method]+"_"+model_name
                    if request.user.has_perm(perm):
                        print("authenticated")
                    else:
                        print("unauthenticated")
                        return False
                else:
                    print("unauthenticated")
                    return False
            # for key in request.keys():
            #     print("Key : {} , Value : {}".format(key, request.get(key)))
            return True
        return True