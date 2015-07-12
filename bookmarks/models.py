from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    content = models.URLField()
    desc = models.TextField(null=True)
    
    def __unicode__(self):
        return self.title