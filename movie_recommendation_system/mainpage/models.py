from __future__ import unicode_literals

from djongo import models

class movielist(models.Model):
    movie_name = models.CharField(max_length = 200, null = True)
    thumbnail = models.CharField(max_length = 2000, null = True)
    imdb = models.CharField(max_length = 20, null = True)
    sypnosis=models.CharField(max_length = 2000, null = True)
            
    def __str__(self):
        return self.movie_name

