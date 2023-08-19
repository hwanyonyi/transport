from rest_framework.response import Response
from rest_framework.views import APIView

from .resource_handler import get_resources


# Create your views here.

class TransportList(APIView):

		def get(self, request, format=None):
				# fro = request.query_params.get('from')
				# to = request.query_params.get('to')
				fro = 1
				to = 10
				resources = get_resources(fro, to)
				return Response(resources)
