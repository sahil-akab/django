from django.shortcuts import render
from django.http import Http404
#from recom.models import Item
from utilities_dir.p1 import *
# Create your views here.

def index(request):
	return render(request,'recom/index.html',{'ucur':us_canada_user_rating,})