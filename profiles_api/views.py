from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods a functions',
            'is similar to a traditional django view',
            'gives most control over application logic',
            'is mapped manually to Urls'
        ]

        return Response({'msg': 'Hello!', 'apiview': an_apiview})
