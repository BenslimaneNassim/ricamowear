from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from PIL import Image
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


TYPES = (
    ('Cloths','Cloth'),
    ('Accessories','Accessorie'),
)
CATEGORIES = (
    ('Hoodie','Hoodie'),
    ('Sweater','Sweater'),
    ('Ensemble','Ensemble'),
    ('Bag','Bag'),
    ('T-Shirt','T-Shirt')
)
SEXES = (
    ('M','Men'),
    ('W','Women'),
    ('M/W','Mixte'),
)
WILAYAS = (
    ('01','Adrar'),
    ('02','Chlef'),
    ('03','Laghouat'),
    ('04','Oum El Bouaghi'),
    ('05','Batna'),
    ('06','Béjaïa'),
    ('07','Biskra'),
    ('08','Béchar'),
    ('09','Blida'),
    ('10','Bouira'),
    ('11','Tamanrasset'),
    ('12','Tébessa'),
    ('13','Tlemcen'),
    ('14','Tiaret'),
    ('15','Tizi Ouzou'),
    ('16','Alger'),
    ('17','Djelfa'),
    ('18','Jijel'),
    ('19','Sétif'),
    ('20','Saïda'),
    ('21','Skikda'),
    ('22','Sidi Bel Abbès'),
    ('23','Annaba'),
    ('24','Guelma'),
    ('25','Constantine'),
    ('26','Médéa'),
    ('27','Mostaganem'),
    ('28',"M'Sila"),
    ('29','Mascara'),
    ('30','Ouargla'),
    ('31','Oran'),
    ('32','El Bayadh'),
    ('33','Illizi'),
    ('34','Bordj Bou Arreridj'),
    ('35','Boumerdès'),
    ('36','Tarf'),
    ('37','Tindouf'),
    ('38','Tissemsilt'),
    ('39','El Oued'),
    ('40','Khenchela'),
    ('41','Souk Ahras'),
    ('42','Tipaza'),
    ('43','Mila'),
    ('44','Aïn Defla'),
    ('45','Naâma'),
    ('46','Aïn Témouchent'),
    ('47','Ghardaïa'),
    ('48','Relizane'),
    ('49','Timimoun'),
    ('50','Bordj Badji Mokhtar'),
    ('51','Ouled Djellal'),
    ('52','Béni Abbès'),
    ('53','In Salah'),
    ('54','In Guezzam'),
    ('55','Touggourt'),
    ('56','Djanet'),
    ('57',"El M'Ghair"),
    ('58','El Meniaa'),
)


class Design(models.Model):
    name = models.CharField(max_length=30)
    date_upload = models.DateField(auto_now_add=True, blank=True,null=True)
    image = models.ImageField(upload_to="designs/",blank=True,null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    design = models.ForeignKey(Design, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="product-images-display/")
    description = models.TextField(max_length=900,null=True,blank=True)
    note = models.TextField(max_length=900,null=True,blank=True)
    care = models.TextField(max_length=900,null=True,blank=True)
    category = models.CharField(choices = CATEGORIES, max_length=8)
    sexe = models.CharField(choices = SEXES, max_length=3)
    types = models.CharField(choices = TYPES, max_length=11)
    price = models.IntegerField(default=2000)
    discounted_price = models.IntegerField(default=None,null=True,blank=True)
    s_size = models.IntegerField(default=0)
    m_size = models.IntegerField(default=0)
    l_size = models.IntegerField(default=0)
    xl_size = models.IntegerField(default=0)
    xxl_size = models.IntegerField(default=0)
    standart_size = models.IntegerField(default=0)
    free_shipping = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product_images(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    image = models.ImageField(upload_to="product-images/")

class Commande(models.Model):
    product = models.ForeignKey(Product, on_delete = models.PROTECT)
    size = models.CharField(max_length=3)
    nom = models.CharField(max_length=50)
    prénom = models.CharField(max_length=50)
    wilaya = models.CharField(choices= WILAYAS,max_length=2)
    ville = models.CharField(max_length=30)
    adresse = models.TextField(max_length=100)
    numero = PhoneNumberField(region="DZ")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    optionel = models.TextField(max_length=100,null=True,blank=True)
    selled = models.DecimalField(max_digits=7,decimal_places=0)

class Email(models.Model):
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.email

class Shipping_Price(models.Model):
    price = models.IntegerField(default=400)
    def __str__(self):
        return str(self.price) + " DA"
    
    def save(self, *args, **kwargs):
        if not self.pk and Shipping_Price.objects.exists():
            raise ValidationError("Il ne peut y avoir qu'un seul prix de livraison à la fois. La3iyid 0552 79 66 23 ")
        return super(Shipping_Price, self).save(*args, **kwargs)