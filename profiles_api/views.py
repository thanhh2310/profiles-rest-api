from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        an_apiview = [
            'Su that', 'luonn', 'chi', 'co mot',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
