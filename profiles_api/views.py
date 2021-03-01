from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


# Base model
class BaseModelViewSet(viewsets.ModelViewSet):
    queryset = ''
    serializer_class = ''
    permission_classes = (AllowAny,)

    permission_classes_by_action = {
        'create': permission_classes,
        'list': permission_classes,
        'retrieve': permission_classes,
        'update': permission_classes,
        'destroy': permission_classes,
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            if self.action:
                action_func = getattr(self, self.action, {})
                action_func_kwargs = getattr(action_func, 'kwargs', {})
                permission_classes = action_func_kwargs.get('permission_classes')
            else:
                permission_classes = None

            return [permission() for permission in (permission_classes or self.permission_classes)]



# user profile view
class UserProfileViewSet(BaseModelViewSet):
    """API ViewSet"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes_by_action = {
        'create': (AllowAny,),
        'list': (IsAuthenticated, IsAdminUser,),
        'retrieve': (IsAuthenticated, permissions.UpdateOwnProfile,),
        'update': (IsAuthenticated, permissions.UpdateOwnProfile,),
        'destroy': (IsAuthenticated, permissions.UpdateOwnProfile,)
    }

    def get_queryset(self):
        user = self.request.user
        return models.UserProfile.objects.filter(id=user.id)

    

# Login view
class Login(ObtainAuthToken):
    """Create User authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })



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