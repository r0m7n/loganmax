from django.shortcuts import render
from django.utils import timezone
from .models import Infodate

def index(request):
#	primer1 = Infodate.objects.all().filter(conder = 'нет')
	return render(request, 'Infodate/index.html',{})
	
def primer(request):
    primer1 = Infodate.objects.all().filter(conder = 'нет')
    return render(request, 'Infodate/primer.html',{'primer1':primer1})
	
#	def index(request):
#	infodates = Infodate.objects.all().filter(conder = 'нет')
#	return render(request, 'Infodate/index.html',{'infodates': infodates})
	


#def primer(request):
#    primer1 = Infodate.objects.all().order_by('date_publish')
# 	return render(request, 'Infodate/primer.html',{'primer1':primer1})
# Create your views here.
