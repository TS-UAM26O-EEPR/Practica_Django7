import os
import re
from pathlib import Path

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / 'logs'


def leer_log(nombre_archivo, filtros=None, limite=100):
    """
    Lee un archivo .log y devuelve sus líneas como lista.
    Aplica filtros opcionales (dict de clave:valor a buscar en cada línea).
    """
    ruta = LOGS_DIR / nombre_archivo
    if not ruta.exists():
        return []

    with open(ruta, encoding='utf-8') as archivo:
        lineas = archivo.readlines()
    lineas = [linea for linea in lineas if linea.startswith('[')]
    if filtros:
        for clave, valor in filtros.items():
            if valor:
                lineas = [linea for linea in lineas if valor.lower() in linea.lower()]

    return [linea.strip() for linea in reversed(lineas[-limite:])]


class LogAuditoriaView(APIView):
    """
    Devuelve entradas del log de auditoría.
    Solo accesible para administradores.
    """

    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(tags=['logs'])
    def get(self, request):
        filtros = {
            'usuario': request.query_params.get('usuario'),
            'accion': request.query_params.get('accion'),
        }
        limite = int(request.query_params.get('limite', 100))

        entradas = leer_log('auditoria.log', filtros=filtros, limite=limite)

        return Response(
            {
                'total': len(entradas),
                'filtros_aplicados': {key: value for key, value in filtros.items() if value},
                'entradas': entradas,
            },
            status=status.HTTP_200_OK,
        )


class LogTecnicoView(APIView):
    """
    Devuelve entradas del log técnico (WARNING, ERROR, CRITICAL).
    Solo accesible para administradores.
    """

    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(tags=['logs'])
    def get(self, request):
        filtros = {
            'nivel': request.query_params.get('nivel'),
            'modulo': request.query_params.get('modulo'),
        }
        limite = int(request.query_params.get('limite', 100))

        entradas = leer_log('tecnico.log', filtros=filtros, limite=limite)

        return Response(
            {
                'total': len(entradas),
                'filtros_aplicados': {key: value for key, value in filtros.items() if value},
                'entradas': entradas,
            },
            status=status.HTTP_200_OK,
        )