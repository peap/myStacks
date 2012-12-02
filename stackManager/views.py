from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import (render_to_response, redirect)
from django.core.context_processors import csrf

from stackManager.models import Collection
from stackManager.forms import CollectionForm


def home(request):
    return render_to_response('home.html')


def collections(request):
    context = {}
    user = request.user
    if user.is_authenticated():
        collections = list(Collection.objects.filter(owner=request.user))
        context.update({'collections': collections})
    return render_to_response('collections.html', context)


def create_collection(request):
    context = {}
    context.update(csrf(request))

    if request.POST:
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Created new collection.')
        else:
            messages.add_message(request, message.ERROR, 'Error creating new collection.')
        return redirect('collections')

    context.update({'form': CollectionForm})

    return render_to_response('create_collection.html', context)


def items(request):
    return render_to_response('items.html')


def wishlist(request):
    return render_to_response('wishlist.html')
