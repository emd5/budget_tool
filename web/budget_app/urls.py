from django.urls import path
from .views import BudgetListView, BudgetDetailView, BudgetCreateView

urlpatterns = [
    path('', BudgetListView.as_view(), name='budget_view'),
    path('new/', BudgetCreateView.as_view(), name='budget_create'),
    path('transaction/<int:id>', BudgetDetailView.as_view(), name='budget_detail'),

]
