from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def front(request):
    context={}
    return render(request,'index.html')