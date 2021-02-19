from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect


from django.contrib.auth.models import User

def index(request):
    return render (request,"index.html")
def about(request):
    return render (request,"about.html")
def resume(request):
    return render (request,"index.html")

def myexpereinces_college(request):
    return render(request , "college.html")
def myexpereinces_ssb(request):
    return render (request,"ssb.html")
def handlesignup(request):
    #return render(request,'signup.html')

    if request.method == 'POST':
        if request.method == 'POST':
            username = request.POST.get('username')
            firstname = request.POST.get('firstname')
            secondname = request.POST.get('secondname')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')

            # check the ambious inputs

            # create user

            user = User.objects.create_user(username=email,email=email,password=pass1)
            user.save()
            messages.success(request,"done")
            return redirect('/home')



#return render(request, 'auth/register.html', {'form': form})

