from django.shortcuts import render,redirect

from django.views.generic import View

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from .forms import LoginForm

# Create your views here.

class LoginView(View):

    def get(self,request,*args,**kwargs):

        form = LoginForm()

        data ={'form': form}

        return render(request,'authentication/login.html',context=data)
    
    def post(self,request,*args,**kwargs):

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')

            password= form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)

            print(user)

            print(password)

            if user:

                login(request,user)

                role = user.role

                if role in ['admin','sales']:

            # print(user)

            # print(username,password)

                      return redirect('dashboard')
            
                elif role in ['academic counsellor','trainer']:

                    return redirect('students-list')
            
                elif role in ['student']:

                    return redirect('recordings')
            
            

            

            error= 'user does not exist'

            data={'form':form,'error':error}

            return render(request,'authentication/login.html',context=data)
            
class LogoutView(View):

    def get(self,request,*args,**kwargs) :

        logout(request)

        return redirect('login')    
