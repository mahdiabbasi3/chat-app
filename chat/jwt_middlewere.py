from urllib.parse import parse_qs
from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import UntypedToken
from django.contrib.auth.models import AnonymousUser
from asgiref.sync import sync_to_async

class jwtmiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = parse_qs(scope["query_string"].decode())
        token = query_string.get("token", [None])[0]

        if token:
            try:
                UntypedToken(token)  # اعتبار اولیه
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(token)

                # این خط مهمه 🔥
                user = await sync_to_async(jwt_auth.get_user)(validated_token)

                scope["user"] = user
            except Exception as e:
                print("❌ خطا در JWT Middleware:", e)
                scope["user"] = AnonymousUser()
        else:
            scope["user"] = AnonymousUser()

        return await super().__call__(scope, receive, send)
