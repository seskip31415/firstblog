from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKet('auth.User', on_delete = model.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = model.DateTimeField(blank = True, null = True)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    