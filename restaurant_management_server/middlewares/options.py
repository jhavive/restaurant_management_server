from django.http import JsonResponse

def options(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if(request.method=="OPTIONS"):
            return JsonResponse(data={}, status=200)
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware