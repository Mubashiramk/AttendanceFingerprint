from django.http import HttpResponseRedirect
from django.shortcuts import render

from .devicetester import *


def launchwaiting(request):
    if test_device():
        return HttpResponseRedirect('/upload/')
    else:
        return render(request, 'laucherror.html', {'success': True})
