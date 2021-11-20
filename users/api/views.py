from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User
from users.models import UserModel
from users.api.serializers import UserSerializer

@api_view(['GET',])
def api_detail_user_view(request,username):
    try:
        user = User.objects.get(username= username)
    except User.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
