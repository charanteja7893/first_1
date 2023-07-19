from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def charan(request):
    return HttpResponse('<h1><marquee>BE HAPPY....</marquee> </h1>')
