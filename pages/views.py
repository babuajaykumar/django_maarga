from django.shortcuts import render
from django.http import HttpResponse
from apartments.models import Carousel,FlatType



# Create your views here.
def index(request):

    carousel = Carousel.objects.all()
    context ={
        'carousel': carousel,
    }

    return render(request, 'pages/index.html',context)


def about(request):
    # Get all Realtors
    #realtors = Realtor.objects.order_by('-hire_date')

    #GET MVP- Seller of the month
    #mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    #context={
    #    'realtors': realtors,
     #   'mvp_realtors': mvp_realtors
    #}

    #return render(request, 'pages/about.html',context)
    return render(request, 'pages/about.html')
