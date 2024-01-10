from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Element
def table(request):
    template = loader.get_template('table.html')
    substance = Element.objects.all().values()

    data = {
        "substance":substance,
        
    }
    return HttpResponse(template.render(data,request))

def details(request,atomic_number):
    template = loader.get_template('details.html')
    substance = Element.objects.filter(pk = atomic_number).values()[0]
    electron_range = range(atomic_number)
    context = {
        "substance":substance,
        "electron_range":electron_range
    }

    return HttpResponse(template.render(context,request))
