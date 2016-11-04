from django.shortcuts import render
from django.http import HttpResponse, Http404

from programs.models import Program, Category

# Create your views here.
def index(request, id):
    try:
        if id == None:
            category = Category.objects.first()
        else:
            category = Category.objects.get(pk = id)
    except Category.DoesNotExist:
        raise Http404
    programs = Program.objects.filter(category = category).order_by("title")
    s = "Категория: " + category.name + "<br><br>"
    for program in programs:
        s = s + "(" + str(program.pk) + ")" + program.title + "<br>"
    # return HttpResponse(s)
    return render(request, "index.html", {'category': category, 'programs': programs})

def program(request, id):
    try:
        program = Program.objects.get(pk = id)
    except Program.DoesNotExist:
        raise Http404
    s = program.title + "<br><br>" + program.category.name + "<br><br>" + program.description
    if not program.is_active:
        s = s + "<br><br>" + "Программа не действует!"
    return HttpResponse(s)
