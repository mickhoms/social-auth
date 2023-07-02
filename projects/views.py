from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User

from .models import Project
from .serializers import ProjectSerializer


class ProjectView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

@api_view(['GET'])
def get_headers(request):
    headers = request.headers
    print(headers, '\n\n')
    if not headers:
        return Response({'msg': 'headers'})
    return Response(headers)
