from django.db import models

# Create your models here.
class SocialMediaPost(models.Model):
    platform = models.CharField(max_length=50)
    post_id = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.IntegerField()
    shares = models.IntegerField()
    comments = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.platform} - {self.post_id}'