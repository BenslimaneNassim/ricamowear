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

def index(request):
    nb_satisfied_clients = len(Commande.objects.all())+15
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    

    products = Product.objects.order_by('-id')[:6]
    context = {'clo_categories':clo_categories,'acc_categories':acc_categories,'designs_link':designs,'nb_satisfied':nb_satisfied_clients,'products':products,'Cloths':'Cloths','Accessories':'Accessories'}
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)
    return render(request,"ricamo/index.html",context)
def search(request, searched):
    designs = Design.objects.filter(name__contains=searched).first()
    products = Product.objects.filter(Q(name__contains=searched) | Q(category__contains=searched) | Q(types__contains=searched) | Q(design=designs))
    context={'products':products,'searched':searched}
    print(products)
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories
    context['designs_link']=designs
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)
    return render(request,"ricamo/search.html",context)

def product(request, product_name):
    product = Product.objects.get(name=product_name)
    images = Product_images.objects.filter(product=product)
    context={'product':product,'images':images}

    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories
    context['designs_link']=designs
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)

    return render(request,"ricamo/product.html",context)

def checkout(request, product_name):
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)
        elif (request.POST.get('nom') == None) and request.POST.get('size') :
            print("2 is comin")
            form = CommandeForm()
            product = Product.objects.get(name=product_name)
            size = request.POST.get('size')
            shipping = Shipping_Price.objects.first()
            all_wilayas = WILAYAS
            wilayas = []
            for a_wilaya in all_wilayas:
                wilayas.append(a_wilaya[0])
            context={'product':product,'size':size,'form':form,'shipping':shipping,'wilayas':wilayas}
            context['clo_categories']= clo_categories
            context['acc_categories']=acc_categories
            context['designs_link']=designs
            return render(request,"ricamo/checkout.html",context)

        elif request.POST.get('price')== None:
            
            form = CommandeForm(request.POST)
            if form.is_valid():
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
                print("form is valid")

                if result['success']:
                    #####
                    print("success")
                    size = request.POST.get('size')
                    product = Product.objects.get(name=product_name)
                    nom = request.POST.get('nom')
                    prenom = request.POST.get('prénom')
                    wilaya = request.POST.get('wilaya')
                    ville = request.POST.get('ville')
                    adresse = request.POST.get('adresse')
                    numero = request.POST.get('numero')
                    optionel = request.POST.get('optionel')
                    print(wilaya)
                    
                    ship_price = Shipping_Price.objects.first()
                    if product.discounted_price :
                        price = int(product.discounted_price)
                    else:
                        price = int(product.price)
                    if wilaya != "06" and not product.free_shipping :
                        price = price + int(ship_price.price)
                    print(price)
                    context = {'price':price,'product':product,'size':size,'nom':nom,'prenom':prenom,'wilaya':wilaya,'ville':ville,'adresse':adresse,'numero':numero,'optionel':optionel}
                    context['clo_categories']= clo_categories
                    context['acc_categories']=acc_categories
                    context['designs_link']=designs
                    return render(request,"ricamo/checkout.html",context)
                    

                else:
                    print('ttnak')
            else:
                print(form.errors.as_data())
        else:
                    print("3")
                    size = request.POST.get('size')
                    product = Product.objects.get(name=product_name)
                    nom = request.POST.get('nom')
                    prenom = request.POST.get('prénom')
                    wilaya = request.POST.get('wilaya')
                    ville = request.POST.get('ville')
                    adresse = request.POST.get('adresse')
                    numero = request.POST.get('numero')
                    optionel = request.POST.get('optionel')
                    selled = request.POST.get('price')
                    com = Commande()
                    com.product = product
                    com.size = size
                    com.nom = nom
                    com.prénom = prenom
                    com.wilaya = wilaya
                    com.ville = ville
                    com.adresse = adresse
                    com.numero = numero
                    com.optionel = optionel
                    com.selled = selled
                    com.save()

                    success_message = 'Votre Commande a été passée'
                    context = {'success':success_message}
                    context['clo_categories']= clo_categories
                    context['acc_categories']=acc_categories
                    context['designs_link']=designs
                    return render(request,"ricamo/checkout.html",context)

    print("1")
    product = Product.objects.get(name=product_name)
    context={'product':product}
    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories
    context['designs_link']=designs
    return render(request,"ricamo/checkout.html",context)

def brand(request):
    context={}
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    
    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories
    context['designs_link']=designs
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)
    return render(request,"ricamo/brand.html",context)
def category(request, category_name):
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    
    products = Product.objects.filter(types=category_name)
    context={'products':products,'category':category_name}
    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories
    context['designs_link']=designs
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)

    return render(request,"ricamo/all-of-category.html",context)

def categories(request, category_name, categories_name):
    products = Product.objects.filter(types=category_name,category=categories_name)
    context={'products':products,'category':category_name,'categories':categories_name}
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories
    context['designs_link']=designs
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)
    
    return render(request,"ricamo/all-of-category.html",context)

def design(request):
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        print(product)
        designs.append([a_design,product])
    context = {'designs':designs}
    all_designs = Design.objects.order_by('-date_upload')
    designs = []
    for a_design in all_designs:
        product = Product.objects.filter(design=a_design)[0]
        designs.append([a_design,product])

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc_categories.append(acc.category)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            clo_categories.append(cloth.category)
    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories
    context['designs_link']=designs
    if request.method == "POST":
        if request.POST.get('email'):
            mail = Email()
            mail.email = request.POST.get('email')
            mail.save()
            mail_message = "Merci de vous avoir abonné !"
            context['mail_message'] = mail_message
        elif request.POST.get('search'):
            searched = request.POST.get('search')
            return redirect(search,searched)
    return render(request,"ricamo/all-of-category.html",context)


