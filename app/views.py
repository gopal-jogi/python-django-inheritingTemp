from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def second(request):
    return render(request,'second.html')

def third(request):
    return render(request,'third.html')