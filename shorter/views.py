from django.shortcuts import render, redirect
from .forms import LongUrl
from . import shorter_core
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def index(request):
    form = LongUrl()

    if request.method == 'POST':
        longurl = shorter_core.check(request.POST['longurl'])

        if not is_valid(longurl):
            return render(request, "index.html", {'form':form, 'err':'Неверный адрес'})

        shorturl = shorter_core.to_short(longurl)
        return render(request, "index.html", {'form':form, 'tmp':shorturl})
    else:
        return render(request, "index.html", {'form':form})

def go_to(request):
    site = shorter_core.get_longurl(shorter_core.HOST + request.path)
    if is_valid(site):
        form = LongUrl()
        return render(request, "index.html", {'form':form})
    return redirect(site)

def is_valid(url):
    val = URLValidator()
    try:
        val(url)
        return True
    except ValidationError:
        return False
