from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from school.views import *

# Create your views here.
from user.forms import UserCreationForm
from user.models import User


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
            print(form.data['classroom'])
            classroom = Classroom.objects.get(pk=form.data['classroom'])
            user = User.objects.create(
                full_name=form.data['full_name'],
                username=form.data['username'],
                classroom=classroom
            )
            user.set_password(form.data['password'])
            user.save()
            # new_user.is_authenticated = True
            # print(new_user.is_authenticated)
            return HttpResponseRedirect("/salon/" + str(user.classroom.pk))
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })