from django.db import models
from ClientManagementService.models import Client
from AuthenticationService.models import Role

# Create your models here.
class User(models.Model):
    ID = models.AutoField(primary_key=True)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientID')
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    password = models.CharField(max_length=20, default='password123')
    secretKey = models.CharField(max_length=30, default='secretKey1234')
    isActive = models.BooleanField(null=True)
    createdDate = models.DateTimeField(null=True)
    updatedDate = models.DateTimeField(auto_now_add=True)
    roleID = models.ForeignKey(Role, default=3, on_delete=models.CASCADE, db_column='roleID')
    designation = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=12)
    email = models.EmailField()
    editFlag = models.BooleanField(null=False)
    isDevelopment = models.BooleanField(default=False)
    class Meta:
        db_table = 'User'