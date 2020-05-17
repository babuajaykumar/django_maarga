from django.shortcuts import render
from maargars.choices import apartment_types,Floor_choices,block_types,block_types_Filter, Floor_choices_Filter
from django.http import  Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
import urllib
from .models import FlatType,  Carousel, BlockType, \
    FloorRangeAllocation, FlatTypeDetail, BlockBaseImage, UnitFlat


# Create your views here.
def apartment(request):
    flatType = FlatType.objects.all().order_by('id')
    blockType = BlockType.objects.all().order_by('id')
    context = {
        'apartment_types': flatType,
        'Floor_choices': Floor_choices,
        'block_types': blockType
    }

    return render(request, 'apartments/flat.html', context)


def apartmentsFilter(request):

    flatvalue = request.GET['flatid']

    print("**********INSIDE FILTER APARTMENTS FLAT FIRST VALYE******^^^^^^^^^",flatvalue, flush=True)
    

    return JsonResponse({"myajax":flatvalue})
