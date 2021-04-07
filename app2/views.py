from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to Index of app2</h1>")

def sample(request):
    return render(request,"sample2.html")

def sample_view(request):
    return render(request,"sample2_app2.html")

def carry_data(request,data):
    return HttpResponse(f'<h1>The city is : {data}</h1>')
# Create your views here.
