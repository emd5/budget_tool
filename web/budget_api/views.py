from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import UserSerializer, User, BudgetSerializer, TransactionSerializer, Budget, Transaction


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


class BudgetListApiView(generics.CreateAPIView):
    """Concrete view for creating a model instance to specific user object by id"""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(
            user_username=self.request.user.username
        )

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class TransactionListApiView(generics.CreateAPIView):
    """Concrete view for creating a model instance to specific user object by id"""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            budget__user__username=self.request.user.username)


