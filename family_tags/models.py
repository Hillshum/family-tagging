from django.db import models


class Photo(models.Model):
    photo = models.FileField()
    caption = models.CharField(max_length=150)
    taken_date = models.DateTimeField('date taken')

    def __str__(self):
        return self.caption


class Ancestor(models.Model):
    given_names = models.CharField(max_length=128)
    last_name = models.CharField(max_length=40)

    photos = models.ManyToManyField(Photo, through="PictureRelationship")

    def __str__(self):
        return self.given_names + self.last_name


class PictureRelationship(models.Model):
    """Defining this here because I'll want to store info on it later"""
    ancestor = models.ForeignKey(Ancestor)
    photo = models.ForeignKey(Photo)
