from __future__ import unicode_literals

from django.db import models

class Man(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=32)
    #follow_ids = models.TextField()

    followings = models.ManyToManyField(      
        'self', 
        blank = True,
        symmetrical = False,
        related_name = 'followers',   
    )

    def count_followings(self):
        return self.followings.count()


    def count_followers(self):
        return self.followers.count()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'man_man'
