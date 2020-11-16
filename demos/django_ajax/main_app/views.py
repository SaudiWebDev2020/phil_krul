from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Product

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        print('-*-'*20)
        print('request.method in create', request.method)
        print('request.POST in create', request.POST)
        print('-*-'*20)
        errors = Product.objects.validate(request.POST)
        if len(errors) > 0:
            print('have errors')
            print(errors)
            return JsonResponse(errors, status=500)
        else:
            Product.objects.create(title=request.POST['title'])
            context = {
                'products': Product.objects.all()
            }
            return render(request, '_products.html', context)
    
    return redirect('/')
