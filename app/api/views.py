from django.shortcuts import render
from django.http import HttpResponse

from api.models import Record


def index(request):
    records = Record.objects.all()
    return HttpResponse(f'<p>{len(records)}</p>')
