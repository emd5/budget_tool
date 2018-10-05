from django.contrib.auth.models import User
from rest_framework import serializers
from ..budget_app.models import Budget, Transaction


class UserSerializer(serializers.ModelSerializer):
    """This class serializes the password to send"""
    password = serializers.CharField(write_only=True)

    class Meta:
        """Users within the Django authentication system are represented by this
        model. """
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        """Overriding by creating the User object to validate data """
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    """Class for handling Budget model integrations through the API"""
    owner = serializers.ReadOnlyField(source='user.username')
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        """Users within the Django authentication system are represented by this model. """
        model = Budget
        fields = ('user', 'name', 'description', 'total_amount')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    """Class for handling Transaction model integrations through the API"""
    category = serializers.HyperlinkedRelatedField(view_name='category-api', read_only=True)

    class Meta:
        """Users within the Django authentication system are represented by this model. """
        model = Transaction
        fields = ('user', 'name', 'description', 'total_amount')
