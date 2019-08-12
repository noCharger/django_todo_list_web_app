from django.shortcuts import render
from django.http import HttpResponse

import datetime

def index(request):
  message = "大宝爱小宝: {}".format(datetime.datetime.now())
  return HttpResponse(message)


