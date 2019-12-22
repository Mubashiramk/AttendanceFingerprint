from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def home_page(request):
    # return HttpResponse("this is the homepage")
    response = TemplateResponse(request, 'index.html', {})
    # Register the callback
    # response.add_post_render_callback(my_render_callback)
    # Return the response
    return response


def student_login(request):
    return HttpResponse("this is the student login page")
