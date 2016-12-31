from django.db import models

# Create your models here.
class Light(models.Model):
	ip_address = models.CharField(max_length=20)
	name = models.CharField(max_length=64, default="unknown")
	current_state = models.BooleanField(default=False)
	auto_off_time_seconds = models.IntegerField(default=0)
	last_beacon_time = models.DateTimeField(auto_now=True)
	motion_trigger_state = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name