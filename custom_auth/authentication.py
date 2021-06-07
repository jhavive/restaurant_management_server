# from django.contrib.auth.models import User
# from rest_framework import authentication
# from rest_framework import exceptions
#
# class CustomAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         username = request.META.get('HTTP_X_USERNAME')
#         if not username:
#             return None
#
#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('No such user')
#
#         return (user, None)

from rest_framework.authentication import TokenAuthentication
from custom_auth.token import MyOwnToken
from django.utils.translation import gettext_lazy as _
from rest_framework import HTTP_HEADER_ENCODING, exceptions

def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth

class CustomAuthentication(TokenAuthentication):
    model = MyOwnToken
    print("authenticate")
    def authenticate(self, request):
        print("authenticate")
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token, request)

    def authenticate_credentials(self, key, request):
        model = self.get_model()
        print("authenticate")
        try:
            token = model.objects.select_related('user').get(key=key)
            user = model.objects.get(key=key).user
            if(str(user.organization.id) != request.META.get('HTTP_X_ORG_ID')):
                raise exceptions.AuthenticationFailed(_('Invalid token.'))

            print("authenticate_credentials", str(user))
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        # except exceptions:


        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)