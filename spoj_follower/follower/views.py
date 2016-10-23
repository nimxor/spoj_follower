from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from urllib import quote_plus



def index(request):
	context = {}
	return render(request,"index.html",context)