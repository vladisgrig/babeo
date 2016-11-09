from django.shortcuts import render
from django.http import HttpResponse, Http404

from programs.models import Program, Category

# Create your views here.

def program_list(request, id):
    try:
        if id == None:
            category = Category.objects.first()
        else:
            category = Category.objects.get(pk = id)
    except Category.DoesNotExist:
        raise Http404
    programs = Program.objects.filter(category = category).order_by("title")
    categories = Category.objects.all();
    s = "Категория: " + category.name + "<br><br>"
    for program in programs:
        s = s + "(" + str(program.pk) + ")" + program.title + "<br>"
    # return HttpResponse(s)
    return render(request, "index.html", {'category': category, 'categories': categories, 'programs': programs})

def program(request, id):
    try:
        program = Program.objects.get(pk = id)
    except Program.DoesNotExist:
        raise Http404
    category = Category.objects.get(pk = program.category.id)
    categories = Category.objects.all();
    return render(request, "program.html", {'category': category, 'categories': categories, 'program': program})
