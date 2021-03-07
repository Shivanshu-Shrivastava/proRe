from django.db import models


# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=25)

    email = models.EmailField()
    phone = models.IntegerField()
    dateob = models.CharField(max_length=25)
    address = models.TextField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


class EducatModel(models.Model):
    degree = models.CharField(max_length=25,null=True)

    start_yr = models.CharField(max_length=25)
    end_yr = models.CharField(max_length=25)
    institute = models.CharField(max_length=25)
    score=models.IntegerField()

    # def __iter__(self):
    #     return [self.degree,
    #             self.start_yr,
    #             self.end_yr,
    #             self.institute,
    #             self.score,
    #             ]

class workModel(models.Model):
    profile = models.CharField(max_length=88)
    title = models.CharField(max_length=88)
    description = models.CharField(max_length=250)

class posModel(models.Model):
    first = models.CharField(default="Empty",blank=True,null=True, max_length=88)
    last = models.CharField(default="Empty",blank=True,null=True, max_length=88)
    handle = models.CharField(default="Empty",blank=True,null=True, max_length=250)

class proModel(models.Model):
    project=models.CharField(max_length=80)
    industrial=models.CharField(max_length=80)
    projlink=models.URLField(blank=True,null=True)

class acaModel(models.Model):
    academic = models.CharField(max_length=250)

class extraModel(models.Model):
    extra = models.CharField(max_length=250)


class additional(models.Model):
    add = models.CharField(max_length=250)




