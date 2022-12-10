from rest_framework import serializers

from AuthenticationService.models import Role, UserCredentials

class RoleSerializer(serializers.ModelSerializer):    
    class Meta:
        models = Role
        fields = (
            'ID', 'roleName', 'roleDescription'
        )


class UserCredentialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserCredentials
        fields = (
            'ID', 'userID', 'Email', 'username', 'password', 'secretKey', 
            'createdDate', 'updatedDate'
        )