'''
Created on 2 Mar 2016

@author: mariopersonal
'''
from django.http.response import HttpResponseServerError, HttpResponseNotFound

def error_500(request):
    return HttpResponseServerError()

def error_404(request):
    return HttpResponseNotFound()