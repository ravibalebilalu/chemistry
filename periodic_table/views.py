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

def details(request):
    template = loader.get_template('details.html')
    substance = Element.objects.filter(atomic_number = 1).values()[0]

    context = {
        "substance":substance
    }

    return HttpResponse(template.render(context,request))
