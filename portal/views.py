from django.shortcuts import render

 

import sentry_sdk

def home(request):
    return render(request, 'portal/index.html')

def trigger_error(request):
    # Correction du bug : on ne fait plus de division par zéro
    return render(request, 'portal/index.html', {'success': True})
# Create your views here.
