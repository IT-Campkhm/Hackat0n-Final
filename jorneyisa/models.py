from django.db import models
        
class Events(models.Model):
    title = models.TextField()
    time = models.TextField()
    description = models.TextField()
    cout_people = models.BigIntegerField()
    place = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Івенти'
    