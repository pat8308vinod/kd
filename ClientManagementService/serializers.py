from rest_framework import serializers

from ClientManagementService.models import Client, ClientUser


class ClientSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Client
        fields = (
            'ID', 'companyName', 'companyAddress', 'createdDate',
            'isActive', 'isEnabled', 'isEcommerce', 'subscription'
        )


class ClientUserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ClientUser
        fields = (
            'ID', 'clientID', 'firstName', 'lastName', 'isActive', 
            'createdDate', 'updatedDate', 'roleID', 'designation'
        )