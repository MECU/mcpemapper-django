from django.conf import settings
from django.db import models


class World(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    public = models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published')
    create_date = models.DateTimeField('date created')
    
    def __str__(self):
        return self.name

