from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Q
from .forms import CommandeForm 
import json
import urllib
from .helpers import *




def index(request):
    context = context_help(request)
    nb_satisfied_clients = len(Commande.objects.all())+15    
    products = Product.objects.order_by('-id')[:6]
    context['nb_satisfied'] = nb_satisfied_clients
    context['products'] = products
    return render(request,"ricamo/index.html",context)
def search(request):
    context = context_help(request)
    if request.method == "POST":
        if request.POST.get('search'):
            searched = request.POST.get('search')
            categories = Category.objects.filter(name__contains=searched)
            products1=[]
            for cat in categories:
                prs = Product.objects.filter(category=cat)
                for pr in prs:
                    if pr not in products1:
                        products1.append(pr)
            
            products2 = Product.objects.filter(Q(name__contains=searched) | Q(types__contains=searched))# | Q(design=designs)
            products=[]
            for pr in products1:
                products.append(pr)
            for pr in products2:
                if pr not in products:
                    products.append(pr)
            context['products'] = products
            context['searched'] = searched

    return render(request,"ricamo/search.html",context)


def product(request, product_name):
    context = context_help(request)
    product = Product.objects.get(name=product_name)
    colors = Color.objects.filter(product=product)
    images = Product_images.objects.filter(product=product)
    context.update({'product':product,'images':images,'colors':colors})

    return render(request,"ricamo/product.html",context)



def checkout(request):
    context = context_help(request)    
    if request.method == "GET":
        if(request.GET.get('buy-now')):
            tab = json.loads(request.GET.get('buy-now'))
            print(tab)
            product = Product.objects.get(pk=tab[0])
            tab[0]=product
            context['tab']=[tab]
        elif(request.GET.get('cart')):
            tab = json.loads(request.GET.get('cart'))
            for t in tab:
                product = Product.objects.get(pk=t[0])
                t[0]=product
            print(tab)
            context['tab']=tab
        elif(request.GET.get('cart-final')):
            tab = json.loads(request.GET.get('cart-final'))
            total = 0
            for t in tab:
                product = Product.objects.get(pk=t[0])
                t[0]=product
                if product.discounted_price:
                    total = total+product.discounted_price*int(t[2])
                else:
                    total = total+product.price*int(t[2])
            print(tab)
            form = CommandeForm()
            shippings = Shipping_Price.objects.all()
            context['tab']=tab
            context['total']=total
            context['form']=form
            context['shipps']=shippings
        elif(request.GET.get('finalcart-total')):
            
            form = CommandeForm(request.GET)
            if form.is_valid():
                nom = request.GET.get('nom')
                prenom = request.GET.get('prénom')
                wilaya = request.GET.get('wilaya')
                ville = request.GET.get('ville')
                adresse = request.GET.get('adresse')
                numero = request.GET.get('numero')
                optionel = request.GET.get('optionel')
                the_tab = json.loads(request.GET.get('finalcart-total'))
                tab = the_tab[0]
                for t in tab:
                    product = Product.objects.get(pk=t[0])
                    t[0]=product
                total = int(the_tab[1])
                shipping_method = the_tab[2]
                print(wilaya)
                if shipping_method=="domicile":
                    shipping_method="à Domicile"
                    ship_price= int(Shipping_Price.objects.get(wilaya=wilaya).price_domicile)
                elif shipping_method=="bureau":
                    shipping_method="au Bureau"
                    ship_price= int(Shipping_Price.objects.get(wilaya=wilaya).price_bureau)
                else:
                    print("ni lun ni lautre")
                total = total+ship_price
                context.update({'tab':tab,'shipping_method':shipping_method,'total':total,'nom':nom,'prenom':prenom,'wilaya':wilaya,'ville':ville,'adresse':adresse,'numero':numero,'optionel':optionel})
            else:
                print(form.errors.as_data())

    elif (request.method == "POST"):
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url='https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if result['success']:
            the_tab = json.loads(request.POST.get('last-job-input'))
            tab = the_tab[0]
            shipping_method = the_tab[1]
            total = the_tab[2]
            nom = the_tab[3]
            prenom= the_tab[4]
            wilaya = the_tab[5]
            ville=the_tab[6]
            adresse=the_tab[7]
            numero=the_tab[8]
            optionel=the_tab[9]
            com = Commande()
            com.nom = nom
            com.prénom = prenom
            com.wilaya = wilaya
            com.ville = ville
            com.adresse = adresse
            com.numero = numero
            com.optionel = optionel
            com.selled = False
            if (shipping_method=="à domicile"):
                com.domicile = True
            elif(shipping_method=="au bureau"):
                com.domicile = False
            com.save()
            for t in tab:
                to_ord = To_order()
                product = Product.objects.get(pk=t[0])
                size = t[1]
                quantite = t[2]
                color = t[3]
                to_ord.product=product
                to_ord.commande=com
                to_ord.color=color
                to_ord.size=size
                to_ord.quantite=quantite
                to_ord.save()
            success="Votre Commande a été passée "+prenom+"."
            context['success']=success
        else:
            print('Recaptcha fail')



    return render(request,"ricamo/checkout.html",context)


def brand(request):
    context = context_help(request)
    return render(request,"ricamo/brand.html",context)
def category(request, category_name):
    context = context_help(request)
    if category_name != 'all':
        category = Category.objects.get(name=category_name)
        products = Product.objects.filter(category=category)
        context.update({'products':products,'category':category})
    else:
        products = Product.objects.order_by('-id')
        context['products']=products

    return render(request,"ricamo/all-of-category.html",context)

def categories(request, category_name, categories_name):
    context = context_help(request)
    category = Category.objects.get(name=categories_name)
    products = Product.objects.filter(types=category_name,category=category)
    context.update({'products':products,'category':category_name,'categories':categories_name})
    return render(request,"ricamo/all-of-category.html",context)


def mail_handle(request):
    context={}
    if request.method == "POST":
        if request.POST.get('email'):
            context = email(request,context)
    return redirect(index)

def customnotfound(request, exception):
    context = context_help(request)
    return render(request, "ricamo/404.html",context)
