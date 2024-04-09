from django.shortcuts import render
from rest_framework import generics, status,permissions
from knox.models import AuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Expense, Budget
from .serializers import ExpenseSerializer, BudgetSerializer, UserRegistrationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated




# Create your views here

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User registration successful!'}, status=status.HTTP_201_CREATED)
    
   
@permission_classes([IsAuthenticated])
class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    def get_permissions(self):
        return []
   

    
class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    def get_permissions(self):
        return []
   
@permission_classes([IsAuthenticated])
class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.filter(user=None)
    serializer_class = BudgetSerializer
    def get_permissions(self):
        return []
    

class BudgetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer 
    def get_permissions(self):
        return []

