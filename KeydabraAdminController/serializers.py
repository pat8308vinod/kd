from rest_framework import serializers
from KeydabraAdminController.models import KeydabraUser

class KeydabraUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeydabraUser
        fields = (
            'ID', 'firstName', 'lastName', 'isActive', 'roleID', 
            'createdDate', 'updatedDate', 'designation'
        )