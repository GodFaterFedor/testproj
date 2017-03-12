from __future__ import unicode_literals

from django.db import models

class Man(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=32)
    follow_ids = models.TextField()

    def following(self): 
        g = tuple( (i, i) for i in self.follow_ids.split())
        return g

    def count_followings(self):
        return len(self.follow_ids.split())


    def count_followers(self):
        count = 0
        for man in Man.objects.all():
            count += man.follow_ids.split().count(str(self.id))
        return count

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'man_man'
