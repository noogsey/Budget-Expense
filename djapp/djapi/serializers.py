from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense,Budget
from django.contrib.auth import get_user_model
        
        
User = get_user_model
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model= User
        fields = ('username', 'email', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])
        return user
    

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'
        