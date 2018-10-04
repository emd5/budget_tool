from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .serializers import UserSerializer, User


class RegisterApiView(generics.CreateAPIView):
    """Concrete view for creating a model instance to serialize user object """
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserApiView(generics.RetrieveAPIView):
    """Concrete view for creating a model instance to specific user object by id"""
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])

