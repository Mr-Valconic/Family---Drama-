from django.db import models
from django.contrib.auth.models import User



class FamilyMember(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    name = models.CharField(
        max_length=100
    )


    relation = models.CharField(
        max_length=50
    )


    image = models.ImageField(
        upload_to="family/",
        blank=True,
        null=True
    )



    def __str__(self):

        return self.name






class Story(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    title = models.CharField(
        max_length=200
    )


    description = models.TextField()



    image = models.ImageField(
        upload_to="stories/",
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):

        return self.title