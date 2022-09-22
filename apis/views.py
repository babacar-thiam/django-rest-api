from rest_framework import generics

from users.models import User
from .serializers import UserSeriliazer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSeriliazer

