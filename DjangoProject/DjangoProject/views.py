from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hello, This is my First Django Website");
   return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, This is my about Page");

def contact (request):
    return HttpResponse("Hello, This is my contact Page");


