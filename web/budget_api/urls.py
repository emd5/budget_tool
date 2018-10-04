from django.urls import path
from .views import RegisterApiView, UserApiView
from rest_framework.authtoken import views

urlpatterns = [
    path('user/<int:pk>', UserApiView.as_view(), name='user_detail'),
    path('register', RegisterApiView.as_view(), name='register'),
    path('login', views.obtain_auth_token),
    # path('budget', BudgetListApiView.as_view(), name='budget_view'),
    # path('budget/new/', BudgetCreateApiView.as_view(), name='budget_create'),
    # path('transaction/<int:id>', TransactionDetailApiView.as_view(), name='transaction_detail'),
    # path('transaction/new', TransactionCreateApiView.as_view(), name="transaction_create")
]
