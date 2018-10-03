from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = ['name', 'total_budget']
