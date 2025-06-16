from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class AccountProviderCallback(APIView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>BI Designer Authentication</title>
        </head>
        <body>
            <h2>Welcome to the BI Designer</h2>
            <p>This windows will close shortly.</p>
            <script>
                //window.close();
            </script>
        </body>
        </html>
        """
        return HttpResponse(html)