from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'accounts/index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('loginpage')


        context = {'form':form}
        return render(request,'accounts/register.html',context)



def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Something went wrong!')

            
        return render(request,'accounts/login.html')


def logoutpage(request):
    logout(request)
    return redirect('loginpage')


@login_required(login_url='loginpage')
def home(request):
    return render(request,'accounts/home.html')
