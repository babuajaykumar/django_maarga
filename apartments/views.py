from django.shortcuts import render
from maargars.choices import apartment_types,Floor_choices,block_types,block_types_Filter, Floor_choices_Filter
from django.http import  Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
import urllib



# Create your views here.
def apartment(request):
    context = {
        'apartment_types': apartment_types,
        'Floor_choices': Floor_choices,
        'block_types': block_types
    }

    return render(request, 'apartments/flat.html', context)


def apartmentsFilter(request):
    #request_getdata=request.GET['apartment_type']
    #request_getdata = request.GET['apartment_type']
    #request_getdata = request.POST.get('flatid', None)
    flatvalue = request.GET['flatid']

    print("**********INSIDE FILTER APARTMENTS FLAT FIRST VALYE******^^^^^^^^^",flatvalue, flush=True)
    #print("**********INSIDE FILTER APARTMENTS USING AJAX VALUEs************:::***",request_getdata, flush=True)


    return JsonResponse({"myajax":flatvalue})
    #return JsonResponse(context)
    #return render(request, 'apartments/flat.html', context)
