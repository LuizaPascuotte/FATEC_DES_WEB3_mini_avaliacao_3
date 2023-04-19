from django.http import HttpResponse
from django.shortcuts import render
from core.models import FeriadoModel
from datetime import datetime

def get_data(request):
    data_atual = datetime.date(day = 25, month = 12, yaer = datetime.date.year())
    try:
        feriados = FeriadoModel.objects.get(dia=data_atual.day, mes=data_atual.month)
        return render(request,)
    except:
        feriado = "Não é feriado"
