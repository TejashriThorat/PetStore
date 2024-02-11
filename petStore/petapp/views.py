from django.shortcuts import redirect, render

from . models import CartItem, Pet

# Create your views here.
def index(req):
    products = Pet.objects.all()
    context ={}
    context['products'] = products
    return render(req,"index.html",context)

def productDetail(req,pid):
    products = Pet.objects.get(pet_id=pid)
    context = {}
    context['products']=products
    return render(req,"productDetail.html",context)


def viewCart(req):
    return render(req,"cart.html")

def viewCart(req):
    cart_item = CartItem.objects.all()
    context = {}
    context['items'] = cart_item
    total_price = 0
    for x in cart_item:
        print(x.pets.price,x.quantity)
        total_price += (x.pets.price * x.quantity)
        print(total_price)
    context['total'] = total_price
    length = len(cart_item)
    context["length"] = length
    return render(req,"cart.html",context)

def addCart(req,pid):
    products = Pet.objects.get(pet_id = pid)
    cart_items,created = CartItem.objects.get_or_create(pets = products)
    print(cart_items,created)
    if not created:
        cart_items.quantity += 1
    else:
        cart_items.quantity = 1
    cart_items.save()
    return redirect("/viewCart")

def remove(req,pid):
    products = Pet.objects.get(pet_id = pid)
    cart_items = CartItem.objects.get(pets = products)
    cart_items.delete()
    return redirect("/viewCart") 

def search(req):
    search = req.GET['search']
    products=Pet.objects.filter(pet_name__icontains=search)
    context={'products':products}
    return render(req,"search.html",context)

def range(req):
    if req.method == "GET":
        return redirect("/")
    else:
        min = req.POST["min"]
        max = req.POST["max"]
        if min !="" and max !="" and min is not None and max is not None:
            queryset = Pet.prod.get_price_range(min,max) #Using Custom Manager
            #queryset = Product.objects.filter(price__range = (min,max))
            context = {}
            context['products'] = queryset
            return render(req,"index.html",context)
        else:
            return redirect("/")
    
def catlist(req):
    if req.method == "GET":
        queryset = Pet.prod.catlist() #Using Custom Manager
        #queryset = Product.objects.filter(price__range = (min,max))
        context = {}
        context['products'] = queryset
        return render(req,"index.html",context)
    
def doglist(req):
    if req.method == "GET":
        queryset = Pet.prod.doglist() #Using Custom Manager
        #queryset = Product.objects.filter(price__range = (min,max))
        context = {}
        context['products'] = queryset
        return render(req,"index.html",context)
    

    
def priceOrder(req):
    queryset = Pet.objects.all().order_by('price')
    context = {}
    context['products'] = queryset
    return render(req,"index.html",context)

def descpriceOrder(req):
    queryset = Pet.objects.all().order_by('-price')
    context = {}
    context['products'] = queryset
    return render(req,"index.html",context)

def updateqty(req,uval,pid):
    products = Pet.objects.get(pet_id = pid)
    a = CartItem.objects.filter(pets= products)
    print(a)
    print(a[0])
    print(a[0].quantity)
    if uval == 1:
        temp = a[0].quantity + 1
        a.update(quantity = temp)
    else:
        temp = a[0].quantity - 1
        a.update(quantity = temp)
    return redirect("viewCart") 