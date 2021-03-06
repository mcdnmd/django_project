from django.shortcuts import render
from django.http import HttpResponse

from api.models import Record


def index(request):
    records = Record.objects.all()
    result = '<h1>Records in DB</h1>'

    for rec in records:
        result += f'\n<h3>ID:{rec.id}</h3>\n\t<p>{rec.text}</p>'

    return HttpResponse(result)
