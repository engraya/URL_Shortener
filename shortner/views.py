from django.shortcuts import render, redirect
import uuid
from .models import UniformResourceLocator
from django.http import HttpResponse

# Create your views here.

def landingPage(request):
    return render(request, 'landingPage.html')

def shortenerPage(request):
    return render(request, 'index.html')

def createURL(request):
    if request.method == 'POST':
        url_Adress_link = request.POST['link']
        uid_code_id = str(uuid.uuid4())[:8]
        executed_url = UniformResourceLocator(link=url_Adress_link,uuid=uid_code_id)
        executed_url.save()
        return HttpResponse(uid_code_id)

def goTO_URL(request, pk):
    url_map_details = UniformResourceLocator.objects.get(uuidCodeFormat=pk)
    return redirect('https://'+url_map_details.linkAddress)