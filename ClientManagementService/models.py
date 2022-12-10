from django.db import models
from AuthenticationService.models import Role, UserCredentials


# Create your models here.
class Client(models.Model):
    ID = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=100)
    companyAddress = models.CharField(max_length=200)
    companyID = models.CharField(max_length=10, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(null=True)
    isEnabled = models.BooleanField(null=True)
    isEcommerce = models.BooleanField(null=True)
    isLite = models.BooleanField(default=False)
    isPro = models.BooleanField(default=False)
    subscription = models.CharField(max_length=60, null=True)
    class Meta:
        db_table = 'Client'


class ClientUser(models.Model):
    ID = models.ForeignKey(UserCredentials, on_delete=models.CASCADE)
    clientID = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='clientID')
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    isActive = models.BooleanField(null=True)
    createdDate = models.DateTimeField(null=True)
    updatedDate = models.DateTimeField(auto_now_add=True)
    roleID = models.ForeignKey(Role, default=3, on_delete=models.CASCADE, db_column='roleID')
    designation = models.CharField(max_length=20)
    class Meta:
        db_table = 'ClientUser'