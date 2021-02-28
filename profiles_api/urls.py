from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
"""queryset provided in views son base_name not required"""
router.register('profile', views.UserProfileViewSet)
router.register('expenses', views.ExpenseItemViewSet)
router.register('incomes', views.IncomeViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
