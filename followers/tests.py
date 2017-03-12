from django.test import TestCase

from .models import Man

class ManTestCase(TestCase):

    def setUp(self):
    	self.a = Man.objects.create(id = '1', name = 'a', )
    	self.b = Man.objects.create(id = '2', name = 'b', )
    	self.c = Man.objects.create(id = '3', name = 'c', )
    	self.d = Man.objects.create(id = '4', name = 'd', )
    	self.a.save()
    	self.b.save()
    	self.c.save()
    	self.d.save()


       
    def test_count_followings_with_two_followings(self):
    	self.a.followings.add(
    		self.b
    		self.c
    	)
    	self.assertEqual(self.a.count_followings(), 2)

    def test_count_followings_with_zero_following(self):
    	self.assertEqual(self.a.count_followings(), 0)


