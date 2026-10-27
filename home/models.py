from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


def story_expiry_time():
    return timezone.now() + timedelta(hours=24)


class Story(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stories'
    )

    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    expires_at = models.DateTimeField(
        default=story_expiry_time
    )

    def is_expired(self):
        return timezone.now() >= self.expires_at

    def __str__(self):
        return self.title