from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категорії'
        
class Events(models.Model):
    title = models.TextField(blank=True)
    time = models.TextField(blank=True)
    description = models.TextField(blank=True)
    cout_people = models.BigIntegerField()
    place = models.TextField(blank=True)
    location = 0
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Івенти'
    