from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.main.models import Product, Category
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'index.html', {'product':product, 'category':category})


def info(request, id):
    info = Product.objects.get(id = id)
    return render(request, 'info.html', {'info':info})

@login_required(login_url='login')
def add_to_cart(request, id):
    cart_session = request.session.get('cart_session1', [])
    cart_session.append(id)
    request.session['cart_session1'] = cart_session
    print(cart_session)
    return HttpResponseRedirect('/')

@login_required(login_url='login')
def cart(request):
    cart_session = request.session.get('cart_session1', [])
    amount = len(cart_session)
    products = Product.objects.filter(id__in = cart_session)
    total_price = 0
    for i in products:
        i.count = cart_session.count(i.id)
        i.sum = i.count * i.price
        total_price += i.sum
    context = {'products':products, 'amount':amount, 'total_price':total_price}
    return render(request, 'cart.html', context)

def remove(request, id):
    cart_session = request.session.get('cart_session1', [])
    g = cart_session
    g.remove(id)
    print(g)
    request.session['cart_session'] = g
    return HttpResponseRedirect('/')

def search(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        product_model = Product.objects.filter(title__contains = product)
        return render(request, 'search.html', {'product': product_model})

def tel(request):
    tel = Product.objects.filter(category=1)
    return render(request, 'tel.html', {'tel':tel})
    
def nout(request):
    nout = Product.objects.filter(category=2)
    return render(request, 'nout.html', {'nout':nout})

def planshety(request):
    planshety = Product.objects.filter(category=3)
    return render(request, 'planshety.html', {'planshety':planshety})
