from zlib import decompressobj
from django.shortcuts import render
from django.http import HttpResponse
from re import sub

# Create your views here.

def index(request):
  return render(request,'input.html')

def analyse(request):
  djtext = request.GET.get('text')
  removepunc = request.GET.get('removepunc')
  nospace = request.GET.get('nospace')
  noextraspace = request.GET.get('noextraspace')
  upper = request.GET.get('upper')
  lower = request.GET.get('lower')
  snake = request.GET.get('snake')
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


  if removepunc=='on':
    analyzed=""
    for char in djtext:
      if char not in punctuations:
        analyzed = analyzed + char
    djtext=analyzed


  if nospace=='on':
    analyzed=""
    analyzed = ''.join(djtext.split(' '))
    djtext=analyzed


  if noextraspace=='on':
    analyzed=""
    # for char in djtext:
    #   if char != ' ':
    #     analyzed = analyzed + char
    analyzed = ' '.join(djtext.split(' '))
    djtext=analyzed


  if upper=='on':
    analyzed=""
    for char in djtext:
      analyzed = analyzed + char.upper()
    djtext=analyzed


  if lower=='on':
    analyzed=""
    for char in djtext:
      analyzed = analyzed + char.lower()
    djtext=analyzed

    
  if snake=='on':
    analyzed=""
    analyzed = '_'.join(
      sub('([A-Z][a-z]+)', r' \1',
      sub('([A-Z]+)', r' \1',
      djtext.replace('-', ' '))).split()).lower()
    djtext=analyzed

  data = {'data':djtext}
  return render(request,'input.html',data)
  