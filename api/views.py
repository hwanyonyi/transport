from rest_framework.response import Response
from rest_framework.views import APIView

from .resource_handler import get_resources


# Create your views here.

class TransportList(APIView):

		def get(self, request, format=None):
				fro = request.query_params.get('from')
				to = request.query_params.get('to')

				resources = []
				if fro is None and to is None:
					resources.append(get_resources(fro=1, to=100))
				else: 
					resources.append(get_resources(fro=int(fro), to=int(to)))
				return Response(resources)
