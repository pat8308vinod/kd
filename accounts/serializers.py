from rest_framework import serializers

from accounts.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('UserId', 'UserName', 'Password',
                  'FirstName', 'LastName', 'Email')