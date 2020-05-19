from django.shortcuts import render, HttpResponse


def send_hi(req):
    return HttpResponse('<h1>Hello world</h1>')
