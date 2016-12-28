from django.db import models

# Create your models here.
class Light(models.Model):
	ipAddress = models.CharField(max_length=20)
	name = models.CharField(max_length=64)
	currentState = models.CharField(max_length=10)
	autoOffTimeSeconds = models.IntegerField(default=0)
	lastBeaconTime = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.name