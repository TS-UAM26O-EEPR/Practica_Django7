import logging

from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


logger_auditoria = logging.getLogger('auditoria')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        request = self.context.get("request")

        user = authenticate(
            request=request,
            username=username,
            password=password,
        )

        ip = request.META.get(
            'REMOTE_ADDR',
            'IP desconocida',
        )

        if user is None:
            logger_auditoria.warning(
                f"ip:{ip}] [accion: LOGIN_FALLIDO] "
                f"[usuario:{username}] [detalle: credenciales incorrectas]"
            )
            raise AuthenticationFailed("Credenciales inválidas.")

        data = super().validate(attrs)

        logger_auditoria.info(
            f"ip:{ip}] [accion: LOGIN_EXITOSO] "
            f"[usuario:{username}] [id:{user.id}]"
        )

        return data
