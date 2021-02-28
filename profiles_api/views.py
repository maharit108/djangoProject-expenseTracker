from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# user profile view
class UserProfileViewSet(viewsets.ModelViewSet):
    """API ViewSet"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return models.UserProfile.objects.filter(id=user.id)

    

# login view
class UserLoginApiView(ObtainAuthToken):
    """Create User authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class ExpenseItemViewSet(viewsets.ModelViewSet):
    """Handle CRUD for expense Item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ExpenseItemSerializer
    queryset = models.ExpenseItem.objects.all()
    permission_classes = (permissions.UpdateOwnExpense, IsAuthenticated,)

    def perform_create(self, Serializer):
        """Set user_profile to logged in user"""
        Serializer.save(user_profile=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return models.ExpenseItem.objects.filter(user_profile=user.id)



class IncomeViewSet(viewsets.ModelViewSet):
    """CRUD for income"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.IncomeSerializer
    queryset = models.Income.objects.all()
    permission_classes = (permissions.UpdateOwnIncome, IsAuthenticated,)

    def perform_create(self, Serializer):
        """Set user_profile to logged in user"""
        Serializer.save(user_profile=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return models.Income.objects.filter(user_profile=user.id)



class BudgetViewSet(viewsets.ModelViewSet):
    """CRUD for budget"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.BudgetSerializer
    queryset = models.Budget.objects.all()
    permission_classes = (permissions.UpdateOwnBudget, IsAuthenticated,)

    def perform_create(self, Serializer):
        """Set user_profile to logged in user"""
        Serializer.save(user_profile=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return models.Budget.objects.filter(user_profile=user.id)