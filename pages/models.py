from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField('name', max_length=100)
    createdAt = models.DateTimeField('created at', auto_now_add=True)
    updatedAt = models.DateTimeField('updated at', auto_now=True)    

    def __str__(self):
        return f"{self.name}"

class Child(models.Model):
    name = models.CharField('name', max_length=100)
    createdAt = models.DateTimeField('created at', auto_now_add=True)
    updatedAt = models.DateTimeField('updated at', auto_now=True)
    
    pai = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name='pai',
        blank=True, 
        null=True
    )

    mae = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name='mae',
        blank=True, 
        null=True
    )

    # def add_parent(self, pais):
    #     if self.pais_set.count() >= 2:
    #         raise Exception("Too many parents")
    #     self.pais_set.add(pais)

    def __str__(self):
        return f"{self.name}"
