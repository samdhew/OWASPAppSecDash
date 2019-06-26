from django.shortcuts import render
from django.forms.models import model_to_dict
from mapping.models import tbl_OAS_ERRORTYPES, tbl_OAS_ERRORDETAILS
import json
# Create your views here.


def layout(request):
    return render(request, 'mapping/layout.html')


def list(request):
    options = tbl_OAS_ERRORTYPES.objects.all()
    op_details = tbl_OAS_ERRORDETAILS.objects.all()
    print(op_details.values());
    props = { 
        'options' : options,
        'details' : op_details,
    }
    return render(request, 'mapping/list.html', props)


def add(request):
    options = tbl_OAS_ERRORTYPES.objects.all()
    props = { 
        'options' : options
    }
    return render(request, 'mapping/add.html', props)
