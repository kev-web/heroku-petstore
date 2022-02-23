from django.shortcuts import render

from . models import CodingPics, DogInfo


# Create your views here.


def homeView(request):
    code_pics = CodingPics.objects.all()
    dogs = DogInfo.objects.all()

    context = {
        'code_pics' : code_pics,
        'dogs': dogs 
    }

    return render(request, 'simbapp/index.html', context)


def aboutView(request):
    return render(request, 'simbapp/about.html')


def contactView(request):
    return render(request, 'simbapp/contact.html')
