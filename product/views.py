from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def getProducts(request):
	print(*dir(request), sep='\n')
	print("____")
	print("is_ajax: ", request.is_ajax())
	print("____")
	print(request.user)
	data = {}
	data['info'] = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam, magnam."
	data ['goods']= Good.objects.all()
	return render(request, "product/index.html", context=data)

def getPro(request):
	inf = {}
	inf['pro'] = "Lorem ipsum dolor sit amet."
	return render(request, "product/index1.html", context=inf)
