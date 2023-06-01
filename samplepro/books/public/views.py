from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    user_id = request.session.get("uid")
    context = {'user_id': user_id}
    return render(request, 'index.html', context)

def failed(request):
    return render(request,'failed.html')   

def wrong(request):
    return render(request,'wrong.html')        


def reg(request):
    if request.method=="POST":
        ur=Register()
        ur.name=request.POST.get('name')
        ur.email=request.POST.get('email')       
        ur.password=request.POST.get('password')
        ur.save()
    return render(request,"register.html")

def log(request):
    if request.method=="POST":
        ur=Register.objects.filter(name=request.POST.get('name'),password=request.POST.get('password')).count()
        print(ur)
        if ur>0:
            us=Register.objects.filter(name=request.POST.get('name'),password=request.POST.get('password'),user_grand='Grand').count()
            print(us)
            if us>0: 
                usDtl=Register.objects.filter(name=request.POST.get('name'),password=request.POST.get('password'),user_grand='Grand')
                request.session["uid"]=usDtl[0].id
                return render(request,'index.html')
            else:
                return render(request,'failed.html')
        else:
            return wrong(request)  
     
    return render(request,'login.html') 

def logout(request):
    request.session.flush()
    return redirect('/')  

def btable(request):
    us=Books.objects.all()
    my_dict={
        'dt':us,
    }
    return render(request,'btable.html',context=my_dict)        
#  you can use the code given in below for selling products for users 
def addbooks(request):
    if request.method=="POST":
        ur=Books()
        ur.bname=request.POST.get('bname')
        ur.about=request.POST.get('about')       
        ur.price=request.POST.get('price')
        ur.author=request.POST.get('author')
        ur.quantity=request.POST.get('quantity')
        ur.save()
        
        return index(request)
    return render(request,"addbooks.html") 

# the above code is for show books in a table contans edit option and delete option

def bdelete(request):
    us=Books.objects.get(pk=request.GET["id"])
    us.delete()
    return btable(request)   # this is the function for delete book

def edit(request):
    us=Books.objects.filter(pk=request.GET["id"])
    my_dict={
        'data':us,
    }
    return render(request,'edit.html',context=my_dict) #this is the code for get the elements of books for edit

def bookedit(request):
    id=request.POST.get("id")
    bname=request.POST.get("bname")
    about=request.POST.get("about")
    price=request.POST.get("price")
    author=request.POST.get("author")
    quantity=request.POST.get("quantity")

    us=Books.objects.get(pk=id)
    us.bname=bname
    us.about=about
    us.price=price
    us.author=author
    us.quantity=quantity
    us.save()

    return btable(request)  #this is the code for edit the books 

def buy(request):
    bname = request.POST.get('b_name')
    quantity = int(request.POST.get('quantity', 0))
    total_price = float(request.POST.get('total_price', 0))

    book = Books.objects.get(bname=bname)

    return render(request, 'buy.html', {
        'book': book,
        'quantity': quantity,
        'total_price': total_price,
    })

def bookbuy(request):
    if request.method == 'POST':
        selected_books = request.POST.getlist('book')
        quantities = request.POST.getlist('quantity')
        user_id = request.session.get("uid")
        user = get_object_or_404(Register, id=user_id)

        for book_id, quantity in zip(selected_books, quantities):
            book = get_object_or_404(Books, id=book_id)
            quantity = int(quantity)

            if quantity > 0 and quantity <= book.quantity:
                purchased_quantity = min(quantity, book.quantity)

                total_price = book.price * purchased_quantity

                book.purchased_quantity += purchased_quantity
                book.quantity -= purchased_quantity
                book.save()


                buyBook = Buyer(name=user, bname=book,quantity=quantity)
                buyBook.save()


        return render(request, 'buy.html', {
            'book': book,
            'quantity': quantity,
            'total_price': total_price,
            
        })
    else:
        books = Books.objects.all()
        return render(request, 'bookbuy.html', {'books': books})   

def success(request):
    book_id = request.GET.get("id")
    book = get_object_or_404(Books, id=book_id)

    context = {
        'book': book,
    }
    return render(request, 'success.html', context)



def user_dashboard(request):
    user_id = request.session.get('uid')

    if user_id:
        user = Register.objects.get(id=user_id)
        purchased_books = Buyer.objects.filter(name=user)
        orders = Order.objects.filter(user=user)
        context = {
            'purchased_books': purchased_books,
            'orders': orders,
            'user':user
        }
        return render(request, 'user_dashboard.html', context)

    return render(request, 'login.html') 
    
    return render(request, 'user_dashboard.html', context)


def edit_password(request):
    if request.method == 'POST':
        user_id = request.session.get("uid")
        user = get_object_or_404(Register, id=user_id)
        new_password = request.POST['new_password']
        user.password = new_password
        user.save()

        return redirect('user_dashboard')
    else:
        return render(request, 'edit_password.html')

