from django.shortcuts import  render, redirect
from .forms import NewUserForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("base:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	page = 'register'
	return render (request=request, template_name="accounts/register.html", context={"register_form":form, "page_title":page})

def login_request(request):
	if request.method == "POST":
		form = UserLoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"You are now logged in as {username}.")
				return redirect("base:home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = UserLoginForm()
	page = 'login'
	return render(request=request, template_name="accounts/login.html", context={"login_form":form, "page_title":page})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("base:home")
	