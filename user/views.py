from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from school.views import *

# Create your views here.
from user.forms import UserCreationForm


def login_frontend(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/salon/' + str(user.classroom.pk))
            else:
                # Return a 'disabled account' error message
                print('disabled account')
                return HttpResponseRedirect("/login/")
        else:
            # Return an 'invalid login' error message.
            print('error message')
            return HttpResponseRedirect("/login/")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })