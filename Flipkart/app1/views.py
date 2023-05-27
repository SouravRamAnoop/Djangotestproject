from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    return HttpResponse("Hello World")

def test_fun(request):
    return render(request,'test.html')