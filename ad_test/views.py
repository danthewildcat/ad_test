from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import (
    HttpResponse, HttpResponseForbidden, HttpResponseRedirect
)
from django.forms import modelform_factory
from django.shortcuts import render, resolve_url
from django.template.loader import render_to_string

from shopping.models import ShoppingList, ListItem

import pdb

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'])
            auth_login(request, user)
            return HttpResponseRedirect(resolve_url('index'))
    else:
        form = UserCreationForm()
    
    context = {
        'title': 'Sign Up',
        'form': form
    }

    return render(request, 'sign_up.html', context)

def index(request):
    if request.user.is_authenticated():
        list_form = modelform_factory(ShoppingList, fields=(
                                    'label', '_date', ))
        context = {
            'shopping_form': list_form()
        }
    else:
        context = {
            'title': 'Welcome',
            'create_form': UserCreationForm(),
            'auth_form': AuthenticationForm()
        }

    return render(request, 'index.html', context)

def profile(request):
    context = { 'title': 'Profile' }
    return render(request, 'profile.html', context)
