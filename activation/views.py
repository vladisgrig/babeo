from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ActivateSertificateForm

from programs.models import Category
from .models import Sertificate

# Create your views here.
def activate_sertificate(request):
    if request.method == "POST":
        form = ActivateSertificateForm(request.POST)
        if form.is_valid():
            sert = form.save(commit=False)
            try:
                sertificate = Sertificate.objects.get(number = sert.number)
                if not sertificate.is_active:
                    sertificate.user = request.user
                    sertificate.activation_date = timezone.now()
                    sertificate.is_active = True
                    sertificate.save()
                    return redirect('success/')
                else:
                    return redirect('outdated/')
            except Exception as e:
                return redirect('unsuccess/')

    else:
        form = ActivateSertificateForm()
        categories = Category.objects.all();
    return render(request, 'activation/check_sertificate.html', {'form': form, 'categories': categories })

def return_success_message(request):
    categories = Category.objects.all();
    return render(request, 'activation/success.html', { 'categories': categories })

def return_unsuccess_message(request):
    categories = Category.objects.all();
    return render(request, 'activation/unsuccess.html', { 'categories': categories })

def return_outdated_message(request):
    categories = Category.objects.all();
    return render(request, 'activation/outdated.html', { 'categories': categories })
