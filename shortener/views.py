from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.core.urlresolvers import reverse

import base64
import hashlib

from shortener.models import Link

def redirect(request, lid):
    l = get_object_or_404(Link, short_name=lid)
    l.times_visited += 1
    l.save()
    return HttpResponseRedirect(l.destination)

def stats(request, lid):
    l = get_object_or_404(Link, short_name=lid)
    return render(request, 'stats.html', {
            'visits': l.times_visited,
            'shortname': l.short_name,
            'lastvisit': l.last_visit,
            'destination': l.destination,
            })

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Index goes here")

def add(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request.  Missing POST data.')
    else:
        dest = request.POST['dest_url']
        short = short_hash(dest)
        l = Link.objects.create(
                destination = dest,
                short_name = short,
                times_visited = 0
            )
        return render(request, 'added.html', {
                'shorturl': short,
                'destination': dest,
                'link': reverse('link', kwargs={'lid':short.decode('utf-8')}),
                })

def short_hash(destination_url):
    attempt = 0
    found_unique = False
    short = ""
    while not found_unique:
        if attempt > 0:
            destination_url += "try number {n}".format(n=attempt)

        destination_utf8 = destination_url.encode('utf-8')
        hash_bin = hashlib.md5(destination_utf8).digest()
        short = base64.b64encode(hash_bin)[:10]

        if Link.objects.filter(short_name=short):
            # Found collision. Try again.
            attempt += 1
            if attempt > 50:
                raise Exception("Unable to find unique shortname! D:")
        else:
            found_unique = True

    if short == "" or short == None:
        raise Exception("Something went wrong! Empty short name!")

    return short
