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

    if request.method == 'POST':
        #request_getdata = request.POST.get('apartment_type', None)
        flattype = request.GET['apartment_type']

         #GET FORM VALUES
        #encoded_search_term = urllib.parse.quote(flatform.cleaned_data['search_term'])
        #encoded_flatId = urllib.parse.quote(flatform.cleaned_data['flatid'])
        #encoded_flatValue = urllib.parse.quote(flatform.cleaned_data['flatval'])

        print("**********INSIDE FILTER APARTMENTS USING AJAX************:::",flattype)

        ''' context = {
            'apartment_types': apartment_types,
            'block_types_Filter': block_types_Filter,
            'Floor_choices_Filter': Floor_choices_Filter
         }'''
    return JsonResponse({"myajax":"OK AJAX CALL"})
    #return JsonResponse(context)
    #return render(request, 'apartments/flat.html', context)
