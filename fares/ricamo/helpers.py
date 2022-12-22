from .models import *
import json
from django.shortcuts import render, redirect
from .views import *

def context_help(request):
    context={}

    accessories = Product.objects.filter(types='Accessories')
    acc_categories = []
    for acc in accessories:
        if acc.category not in acc_categories:
            acc = Category.objects.get(name=acc.category)
            acc_categories.append(acc)

    cloths = Product.objects.filter(types='Cloths')
    clo_categories = []
    for cloth in cloths:
        if cloth.category not in clo_categories:
            cat = Category.objects.get(name=cloth.category)
            clo_categories.append(cat)

    context['clo_categories']= clo_categories
    context['acc_categories']=acc_categories

    checkout_products=[]
    if request.COOKIES.get("cart"):
        cookie = request.COOKIES.get("cart")
        liss = json.loads(cookie)
        for li in liss:
            prdct = Product.objects.get(pk=int(li[0]))
            checkout_products.append([prdct,li[1],li[2],li[3]])
    context['checkout_products'] = checkout_products
    return context


def email(request,context):      
    mail = Email()
    mail.email = request.POST.get('email')
    mail.save()
    mail_message = "Merci de vous avoir abonné !"
    context['mail_message'] = mail_message
    return context
