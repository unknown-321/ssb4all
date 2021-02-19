from django.shortcuts import render,redirect
from django.contrib.auth.admin import User
from django.contrib import messages
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
            firstname=firstname
            secondname=secondname

            user.save()
            messages.success(request,"done")
            #return redirect('home/')



