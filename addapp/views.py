from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    x=request.GET["t1"]
    y=request.GET["t2"]
    i=int(x)
    j=int(y)
    return HttpResponse("<html><body bgcolor=red><center><h1>sum is :"+str(i+j)+"</h1></center></body></html>")