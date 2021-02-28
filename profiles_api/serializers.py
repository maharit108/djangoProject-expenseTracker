from rest_framework import serializers
from profiles_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile data"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'nick_name')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            nick_name=validated_data['nick_name']
        )

        return user

    def update(self, instance, validated_data):
        """Update user account"""
        """when update data is sent, look for 'password', if present hash it before passing it to UserProfile model."""
        """No need to hash in create function, as it does so in model"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ExpenseItemSerializer(serializers.ModelSerializer):
    """Serializes expense item"""

    class Meta:
        model = models.ExpenseItem
        fields = ('id', 'user_profile', 'expense_item', 'expense_amount', 'expense_tag', 'date', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }


class IncomeSerializer(serializers.ModelSerializer):
    """Serialize income"""

    class Meta:
        model = models.Income
        fields = ('id', 'user_profile', 'income_amount', 'income_details', 'date', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }