from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import c_user
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
import crypt
from hmac import compare_digest as compare_hash
# Create your views here.


def ad_login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        password1=request.POST.get('password')
        #print(shopkeeper, password1)
        print('stored_password',password1)
        print(name)
        data_user = authenticate(username=name,password=password1)
        login(request, data_user)
        print('sssssssssssssssss',data_user)
        if data_user:
             return redirect('admin_page')
        else:  
            messages.error(request, 'Invalid username or password')
    return render(request,'admin_login.html')

def admin_page(request):
    return render(request, 'admin_page.html')

def user_list(request):
    cuser=c_user.objects.all()
    return render(request, 'user_list.html',{'cuser': cuser})

@login_required(login_url='admin_login')
def create_user(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=User.objects.make_random_password()
        password_hash = crypt.crypt(password)
        
        #hashed_password = crypt.crypt(password,password_hash)
        image=request.FILES.get('userimage')
        user,created =c_user.objects.get_or_create(c_name=name, c_email=email, c_image=image,c_password=password,c_encrpted=password_hash)
        user.save()
        # password=c_user.objects.make_random_password()
        # message = request.POST["message"]
        from_email = "<surabhi2996@gmail.com>"
        if name and email:
            subject = "New User registration"
            message = f"Name: {name}\nEmail: {email}\n Password:{password}"
            to_email = [email]
            send_mail(subject, message, from_email, to_email)
            messages.info(request, "Your Request Shared Successfully")
        else:
            messages.info(request, "something went wrong")
        logout(request)
    return render(request,'create_user.html')


def user_login(request):
      if request.method=='POST':
           name=request.POST.get('name')
           password=request.POST.get('password')
           try:
              s_name = c_user.objects.get(c_name=name)
              # Assuming 'password' field stores the hashed password
              s_password = c_user.objects.get(c_password=password)  # Adjust the field name as per your model
              if s_name and s_password:
                messages.info(request, "User exist")
              else:
                messages.info(request, "user doesnot exist")
              # Print statement for debugging
           except c_user.DoesNotExist:
                messages.info(request, "Invalid username and password")
      return render(request,'user_login.html')

  