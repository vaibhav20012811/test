from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class EcomUserAPIView(APIView):
    def get(self, request):
        try:
            return Response(data={"test":"test"})
        except Exception as ex:
            return Response(data={"test":"test"})