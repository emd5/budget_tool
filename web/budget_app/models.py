from django.contrib.auth.models import User
from django.db import models


class Budget(models.Model):
    """A budget class that creates attributes in the database"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()

    def __repr__(self):
        """A representation of the Budget object"""
        return '<Budget: {} | {}>'.format(self.name, self.total_budget)

    def __str__(self):
        """A string representation of the budget object"""
        return '{} | ${}'.format(self.name, self.total_budget)

    @property
    def get_remaining_budget(self):
        return self.total_budget


class Transaction(models.Model):
    """A transaction class that creates attributes in the database"""
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transaction')

    CHOICES = (
        ('withdrawal', 'Withdrawal'),
        ('deposit', 'Deposit'),
    )

    type = models.CharField(
        max_length=15,
        choices=CHOICES,
        default='Deposit'
    )
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __repr__(self):
        """A representation of the Transaction object"""
        return '<Transaction: {} | {} | {} >'.format(self.type, self.amount, self.description)

    def __str__(self):
        """A string representation of the Transaction object"""
        return '{} {} {}'.format(self.type, self.amount, self.description)



