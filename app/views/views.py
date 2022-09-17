from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('auth:login')
    return render(request, 'index.html')

@login_required(redirect_field_name='auth:login')
def playstation5(request):
    product_type = ProductType.objects.get(name_of_type='Ps5')
    products = Product.objects.filter(product_type_key=product_type)
    if request.method == "POST":
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = Product.objects.create(
                product_type_key=product_type,
                photo=form.cleaned_data['photo'],
                is_exists=False,
                slug_product=form.cleaned_data['slug_product']
            )
            new_product.save()
            return redirect('main_app:playstation5')
    else:
        form = CreateProductForm()
    context = {
        'products' : products,
        'form' : form
    }
    return render(request, 'ps5page.html', context)

@login_required(redirect_field_name='auth:login')
def xbox(request):
    product_type = ProductType.objects.get(name_of_type='Xbox')
    products = Product.objects.filter(product_type_key=product_type)
    if request.method == "POST":
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = Product.objects.create(
                product_type_key=product_type,
                photo=form.cleaned_data['photo'],
                is_exists=False,
                slug_product=form.cleaned_data['slug_product']
            )
            new_product.save()
            return redirect('main_app:xbox')
    else:
        form = CreateProductForm()
    context = {
        'products' : products,
        'form' : form
    }
    return render(request, 'xboxpage.html', context)

@login_required(redirect_field_name='auth:login')
def switch(request):
    product_type = ProductType.objects.get(name_of_type='Nintendo')
    products = Product.objects.filter(product_type_key=product_type)
    if request.method == "POST":
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = Product.objects.create(
                product_type_key=product_type,
                photo=form.cleaned_data['photo'],
                is_exists=False,
                slug_product=form.cleaned_data['slug_product']
            )
            new_product.save()
            return redirect('main_app:switch')
    else:
        form = CreateProductForm()
    context = {
        'products' : products,
        'form' : form
    }
    return render(request, 'nintendopage.html', context)

@login_required(redirect_field_name='auth:login')
def donate(request):
    return render(request, 'donate.html')

@login_required(redirect_field_name='auth:login')
def about(request):
    return render(request, 'about.html')

@login_required(redirect_field_name='auth:login')
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(f'main_app:index')
