import sys
from os import path
from django.db import models
#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

#------------------ Gene Model ------------------
class Gene(models.Model):
    Chromosome = models.CharField(max_length=2)
    Start = models.IntegerField()
    End = models.IntegerField()
    Symbol = models.CharField(max_length=50)
    Disease = models.ManyToManyField('Disease', null=True, blank=True)
    Variant = models.ManyToManyField('Variant', null=True, blank=True)

    def __str__(self):
        return self.Symbol

#---------------- Disease Model -----------------
class Disease(models.Model):
    Name = models.CharField(max_length=500, unique=True)
    Inheritance = models.CharField(max_length=30)
    Gene = models.ManyToManyField('Gene', null=True, blank=True)

    def __str__(self):
        return self.Name

#----------------- Variant Model ----------------
class Variant(models.Model):
    Chromosome = models.CharField(max_length=2)
    Position = models.IntegerField()
    Code = models.CharField(max_length=50, unique=True)
    Reference = models.CharField(max_length=50, null=True, blank=True)
    Alternative = models.CharField(max_length=50, null=True, blank=True)
    Gene = models.ForeignKey('Gene', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Code

