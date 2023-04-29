# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Userroles(models.Model):
    id = models.UUIDField(primary_key=True)
    userid = models.ForeignKey(
        'Users', models.DO_NOTHING, db_column='userid', blank=True, null=True)
    roleid = models.ForeignKey(
        Roles, models.DO_NOTHING, db_column='roleid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userroles'


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    secondlastname = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=400)
    image = models.CharField()
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
