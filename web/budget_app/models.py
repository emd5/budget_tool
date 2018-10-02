from django.contrib.auth.models import User
from django.db import models


class Budget(models.Model):
    """A budget class that creates attributes in the database"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget')
    name = models.CharField(max_length=180, default='Untitled')
    total_budget = models.FloatField()
    remaining_budget = models.FloatField()

    def __repr__(self):
        """A representation of the Budget object"""
        return '<Budget: {}>'.format(self.name)

    def __str__(self):
        """A string representation of the budget object"""
        return '{}'.format(self.name)


class Transaction(models.Model):
    """A transaction class that creates attributes in the database"""
    budget = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    name = models.CharField(max_length=180, default='Untitled')

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
        return '<Transaction: {} | {} | {}>'.format(self.budget, self.name, self.type)

    def __str__(self):
        """A string representation of the Transaction object"""
        return '{} {} {}'.format(self.budget, self.name, self.type)


@property
def get_remaining_budget(self):
    """Instantly updates the remaining budget"""
    return self.remaining_budget
