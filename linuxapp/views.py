from django.http import HttpResponse
from django.shortcuts import render

def sample1(request):
    return HttpResponse('hi google')
def sample2(request):
    return HttpResponse(' I AM SHAJIL')
def sample3(request):
    return render(request,'1st.html')    
