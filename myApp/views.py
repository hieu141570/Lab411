from django.shortcuts import render
from myApp import models
# Create your views here.
def getHumi(request):
    if(request.method == "GET"):
        humi = request.GET.get('humi')
        temp = request.GET.get('temp')
        h = models.Humi(humi=humi)
        h.save()
        t = models.Temp(temp=temp)
        t.save()
    return render(request, 'humi.html')
