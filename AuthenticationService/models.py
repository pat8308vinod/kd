from django.db import models

# Create your models here.
class Role(models.Model):
    ID = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=20)
    roleDescription = models.CharField(max_length=25)

    class Meta:
        db_table = 'Role'


class UserCredentials(models.Model):
    ID = models.AutoField(primary_key=True)
    userID = models.IntegerField()
    Email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    secretKey = models.CharField(max_length=30)
    createdDate = models.DateTimeField(null=True)
    updatedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'UserCredentials'