from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from store.models import *
from django.template import loader
from django.contrib import messages

# Create your views here.
def home(request):    
    context ={
        'variable1':"This is sent"
    }
    return render(request, 'store/index.html',context)

def collections(request):
    Categories = Category.objects.filter(status=0)
    context = {
        'Categories': Categories,
    }
    return render(request, 'store/collections.html', context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Products.objects.filter(Category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context={
            'products':products,
            'category':category,
        }
        return render(request, "store/products/index.html",context)
    else:
        messages.warning(request,"No such category found")
        return redirect('colections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Products.objects.filter(slug=prod_slug, status=0)):
            products = Products.objects.filter(slug=prod_slug).first()            
            context={
                'products':products,           
            }
            return render(request, "store/products/view.html", context)
        else:
            messages.error(request,"No such category found")
            return redirect('colections')
    else:
        messages.error(request,"No such category found")
        return redirect('colections')
   