from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Table
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def login(request):
    if request.user.is_authenticated():
        return ("<br>You're: " + request.user.username +
                "<br><a href='/admin/logout/'>Logout</a>")
    else:
        return ("<br>You aren't registred\n<a href='/admin/'>Login</a>")


def all(request):
    list = Table.objects.all()
    out = "<ul>\n"
    for i in list:
        out += "<li><a href=agenda/" + i.name + ">" + i.name + "</a></li>\n"
    out += "</ul>\n"
    out += login(request)
    return HttpResponse(out)


@csrf_exempt
def number(request, recurso):
    if request.method == "GET":
        list = Table.objects.filter(name=recurso)
        if not list:
            return notfound(request, recurso)
        out = " "
        for i in list:
            out += i.name + ": " + str(i.number)
    if request.method == "PUT":
        if request.user.is_authenticated():
            new = Table(name=recurso, number=request.body)
            new.save()
            out = ("Saved Page, check it with GET")
        else:
            out = ("You must be registred")
    out += login(request)
    return HttpResponse(out)


def notfound(request, recurso):
    out = ("Not found: " + recurso)
    out += login(request)
    return HttpResponseNotFound(out)
