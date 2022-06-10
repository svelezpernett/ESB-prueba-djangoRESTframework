from rest_framework.response import Response
from rest_framework.views import APIView
from modules.maaji.models import *
from modules.maaji.api.serializers import *

class ClienteAPIview(APIView):
    def get(self, request):
        cliente = Cliente.objects.all()
        cliente_serializer = Cliente_serializer(cliente, many=True)
        return Response(cliente_serializer.data)

