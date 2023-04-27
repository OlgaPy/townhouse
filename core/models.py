from datetime import datetime

from django.db import models

from core.utils.util import get_file_path


class Source(models.Model):
    """whatsup, telegram, viber, vk, sarafan, marketing, web-site..."""
    name = models.CharField(max_length=1024, blank=False, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'source'


class Status(models.Model):
    """Status of processing client"""
    name = models.CharField(max_length=1024, blank=False, null=True)

    class Meta:
        db_table = 'status'


class Card(models.Model):
    """Card of client"""
    name = models.CharField(max_length=1024, blank=False, null=True)
    phone = models.CharField(max_length=1024, blank=False, null=True)
    email = models.CharField(max_length=1024, blank=False, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'card'


class Client(models.Model):
    """Person"""
    login = models.CharField(max_length=1024, blank=False, null=False, unique=True)
    nickname = models.CharField(max_length=1024, blank=False, null=True)
    link_conversation = models.CharField(max_length=4096, blank=False, null=True)

    name = models.CharField(max_length=1024, blank=True, null=True)
    surname = models.CharField(max_length=1024, blank=True, null=True)
    middle_name = models.CharField(max_length=1024, blank=True, null=True)

    source = models.ForeignKey(
        'Source', on_delete=models.DO_NOTHING, null=True, blank=False)

    manager = models.ForeignKey(
        'Manager', on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.ForeignKey(
        'Status', on_delete=models.DO_NOTHING, null=True, blank=True)
    object_property = models.ForeignKey(
        'TownHouse', on_delete=models.DO_NOTHING, null=True, blank=True)

    comment = models.CharField(max_length=4096, blank=True, null=True)

    class Meta:
        db_table = 'client'


class Manager(models.Model):
    login = models.CharField(max_length=1024, blank=False, null=False, unique=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    surname = models.CharField(max_length=1024, blank=True, null=True)
    middle_name = models.CharField(max_length=1024, blank=True, null=True)

    substitute = models.ForeignKey(
        'Manager', on_delete=models.DO_NOTHING, null=True, blank=True)
    level = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = 'manager'


class Document(models.Model):
    """All documents that need for deal"""
    name = models.CharField(max_length=1024, blank=True, null=True)
    file = models.FileField(upload_to=get_file_path, blank=False, null=False)
    client = models.ForeignKey(
        'Client', on_delete=models.DO_NOTHING, null=True)
    building = models.ForeignKey(
        'TownHouse', on_delete=models.DO_NOTHING, null=True)
    manager = models.ForeignKey(
        'Manager', on_delete=models.DO_NOTHING, null=True)
    date_add = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'document'


class TownHouse(models.Model):
    """The object of construction itself"""
    location = models.ForeignKey(
        'Locality', on_delete=models.DO_NOTHING, null=True)
    address = models.CharField(max_length=1024, blank=False, null=True)
    construction = models.ForeignKey(
        'Construction', on_delete=models.DO_NOTHING, null=True)
    owner = models.CharField(max_length=1024, blank=False, null=True)
    buyer = models.ForeignKey(
        'Client', on_delete=models.DO_NOTHING, null=True, blank=False)

    square_area = models.IntegerField(null=True, blank=True)

    price = models.IntegerField(null=True, blank=True)
    construction_stage = models.ForeignKey(
        'ConstructionStage', on_delete=models.DO_NOTHING, null=True, blank=False)
    manager = models.ForeignKey(
        'Manager', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = 'town_house'


class Construction(models.Model):
    """Type of construction of the building. Ex: Style, Mate, Gross, Family"""
    name = models.CharField(max_length=1024, blank=False, null=True)
    schema_path = models.CharField(max_length=1024, blank=False, null=True)
    floor = models.IntegerField(null=True, blank=False)
    rooms = models.IntegerField(null=True, blank=False)
    square_house = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'construction'


class Locality(models.Model):
    """Which of the building blocks, district"""
    name = models.CharField(max_length=1024, blank=False, null=True)

    class Meta:
        db_table = 'locality'


class ConstructionStage(models.Model):
    """Construction Stage. In the project, foundation laid, walls erected, fully prepared, under warranty..."""
    name = models.CharField(max_length=1024, blank=False, null=True)

    class Meta:
        db_table = 'construction_stage'
