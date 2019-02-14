from django.http import JsonResponse
from django.shortcuts import render
import numpy as np


# Create your views here.
def index(request):
    return render(request, 'home.html')


def feature_1(request):
    return render(request, 'feature_1.html')


def json(request):
    x = np.random.randn(1000)
    return JsonResponse({'x': x.tolist()})


def feature_2(request):
    return render(request, 'feature_2.html')
