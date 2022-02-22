from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import Product
from . forms import *
from django.contrib import messages

# Create your views here.


def index(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'products/index.html', context)


def product_post(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product Added')
            return redirect('/addproduct')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Please Verify forms fields')
            return render(request, 'products/addproduct.html', {
                'form': form
            })

    context = {
        'form': ProductForm
    }
    return render(request, 'products/addproduct.html', context)


def category_post(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Category Added Successfully')
            return redirect('/addcategory')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Please Verify forms fields')
            return render(request, 'products/addcategory.html', {
                'form': form
            })

    context = {
        'form': CategoryForm
    }
    return render(request, 'products/addcategory.html', context)
