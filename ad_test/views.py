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
            return HttpResponseRedirect(resolve_url('home'))
    else:
        form = UserCreationForm()

    return render(request, 'sign_up.html', { 'form': form })

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(resolve_url('profile'))
        
    context = {'create_form': UserCreationForm(),
                'auth_form': AuthenticationForm()}

    return render(request, 'index.html', context)
    
def list_item(request, pk=None):
    if not request.is_ajax():
        return HttpResponseForbidden()
    
    if pk:
        pass
    else:
        pass
    
    return HttpResponse()

def profile(request):
    context = {}
    return render(request, 'profile.html', context) 

def shopping_list(request, pk=None):
    if not request.is_ajax():
        return HttpResponseForbidden()
    
    form = modelform_factory(ShoppingList)
    
    if pk:
        response = ''
    else:
        context = {
            'form': form(),
            'user': request.user
        }
        response = render_to_string('shopping.html', context=context)
    
    return HttpResponse(response)
