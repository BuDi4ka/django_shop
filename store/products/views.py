from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'title': 'Test Title',
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)

def products(request):
    return render(request, 'products/products.html')
