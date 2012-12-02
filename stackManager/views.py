from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html')


def collections(request):
    return render_to_response('collections.html')


def items(request):
    return render_to_response('items.html')


def wishlist(request):
    return render_to_response('wishlist.html')
