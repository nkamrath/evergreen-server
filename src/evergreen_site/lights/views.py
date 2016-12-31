from django.shortcuts import render
from django.http import HttpResponse
from lights.models import Light
from lights.forms import LightForm
import datetime
from django.utils import timezone
from django.http import HttpResponseRedirect
import udp_send

def index(request):
	lightList = Light.objects.order_by('name')
	currentLights = []
	for x in range(0, len(lightList)):
		if lightList[x].last_beacon_time > timezone.now()-datetime.timedelta(seconds=5):
			currentLights.append(lightList[x])
	context_dict = {'lights':currentLights}
	return render(request,'lights/index.html', context_dict)

def light_info(request, lightIpAddress):
	context_dict = {}
	if request.method == 'POST':
		form = LightForm(request.POST)
		light = Light.objects.get(ip_address=lightIpAddress)
		if form.is_valid():
			data = form.cleaned_data
			light.name = data['name']
			light.save()
			return HttpResponseRedirect('/lights/')
	else:
		try:
			light = Light.objects.get(ip_address=lightIpAddress)
			context_dict['light_info'] = light
			form = LightForm()
			form.fields["name"].initial = light.name
			form.fields["ip_address"].initial = light.ip_address

			context_dict['form'] = form
		except Light.DoesNotExist:
			pass
	return render(request, 'lights/light_info.html', context_dict)

#handle commands in http post format to manipulating lights
def light_command(request):
	if(request.method == 'POST'):
		rawCommand = request.POST['command']
		lightIpAddress = rawCommand.split(',')[0]
		lightCommand = rawCommand.split(',')[1]
		print "POST: ", lightIpAddress, lightCommand
		udp_send.udpSendTo(lightIpAddress, 50008, lightCommand)
		#send lightCommand to lightIp via correct udp port
	return render(request,'lights/index.html')
