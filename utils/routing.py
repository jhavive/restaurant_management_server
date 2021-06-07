operation_to_rest = {
    "add": 'POST',
    "view": "GET",
    "change": "PUT",
    "delete": "DELETE"
}

class route:
    method = ''
    route = ''

    def __init__(self, method, route):
        self.method = method
        self.route = route

def permission_to_route(permissions):
    router = {}
    for i in permissions:
        # print(i.content_type.natural_key()[0])
        # print(router)
        if i.content_type.natural_key()[0] != 'admin' and i.content_type.natural_key()[0] != 'auth' \
                and i.content_type.natural_key()[0] != 'authtoken' and i.content_type.natural_key()[0] != 'contenttypes' \
                and i.content_type.natural_key()[0] != 'custom_auth' and i.content_type.natural_key()[0] != 'sessions':
            app_name = i.content_type.natural_key()[0]
            model = i.content_type.natural_key()[1]
            if not app_name in router:
                router[app_name] = {}
                router[app_name][model] = {
                    "app": app_name,
                    "path": model,
                    "methods": [],
                }
            # print(router[app_name])
            try:
                router[app_name][model]
            except KeyError:
                router[app_name][model] = {
                    "app": app_name,
                    "path": model,
                    "methods": []
                }
            # print (router)
            router[i.content_type.natural_key()[0]].get(i.content_type.natural_key()[1]).get('methods').append( operation_to_rest[i.codename.split('_')[0]] )
            # router[i.content_type.natural_key()[0]].append( operation_to_rest[i.codename.split('_')[0]] )
            # try:
            #
            # except:
            #     router[i.content_type.natural_key()[0]] = []
            #     router[i.content_type.natural_key()[0]].append({
            #         "method": operation_to_rest[i.codename.split('_')[0]],
            #         "route": i.content_type.natural_key()[1]
            #     })
            # print(hasattr(router, i.content_type.natural_key()[0]))
            # if not hasattr(router, i.content_type.natural_key()[0]):
            #
            #     router[i.content_type.natural_key()[0]] = []
            #     print(router)
            #
            # router[i.content_type.natural_key()[0]].append({
            #     "method": operation_to_rest[i.codename.split('_')[0]],
            #     "route": i.content_type.natural_key()[1]
            # })
        # router.append({
        # router.append({
        #     "app": i.content_type.natural_key()[0],
        #     "method": operation_to_rest[i.codename.split('_')[0]],
        #     "route": i.content_type.natural_key()[1]
        # })

    return router