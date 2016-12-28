from django.shortcuts import render
from django.http import HttpResponse
from lights.models import Light
import udp_send

def index(request):
	if(request.method == 'POST'):
		rawCommand = request.POST['command']
		lightIpAddress = rawCommand.split(',')[0]
		lightCommand = rawCommand.split(',')[1]
		print "POST: ", lightIpAddress, lightCommand
		udp_send.udpSendTo(lightIpAddress, 50008, lightCommand)
		#send lightCommand to lightIp via correct udp port

	lightList = Light.objects.order_by('name')
	context_dict = {'lights':lightList}
	return render(request,'lights/index.html', context_dict)

