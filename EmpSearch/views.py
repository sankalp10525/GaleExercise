from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Employee, Project


# Create your views here.
def home(request):
    return render(request, 'home.html')


def search(request):
    if request.method == 'POST':
        srch = request.POST['src']

        if srch:
            match = Employee.objects.filter(Q(efirstname__iexact=srch))

            if match:

                return render(request, 'result.html', {'sr': match})
            else:
                return render(request, 'validation.html')
        else:
            return HttpResponseRedirect('/search')

    return render(request, 'home.html')
