from django.forms import ModelForm
from .models import Budget, Transaction


class BudgetForm(ModelForm):
    """This class inherits the modelform to retrieve certain attributes from the model Budget object"""
    class Meta:
        model = Budget
        fields = ['name', 'total_budget']


class TransactionForm(ModelForm):
    """This class inherits the modelform to retrieve certain attributes from the model Transaction object"""

    class Meta:
        model = Transaction
        fields = ['budget', 'type', 'amount', 'description']
