from django.db import models


class Happening(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id) + ': [' + str(self.time) + '] ' + self.description

