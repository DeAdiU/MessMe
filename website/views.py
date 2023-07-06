from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records=Record.objects.all()
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have be looged in")
            return redirect('home')
        else:
            messages.success(request,"There is error")
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have be logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
			# Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def mess_meu(request,pk):
    if request.user.is_authenticated:
        mess_meu=Record.objects.get(id=pk)
        return render(request, 'record.html', {'mess_meu':mess_meu})
    else:
        messages.success(request,"dekho dekhoo")
        return redirect('home')
    
def delete_menu(request,pk):
    if request.user.is_authenticated:
        delete_mar=Record.objects.get(id=pk)
        delete_mar.delete()
        messages.success(request,"uda diyaaaa")
        return redirect('home')

def add_menu(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_menu.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
def menuee(request):
     records=Record.objects.all()
     return render(request,'menu.html',{})