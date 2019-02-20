# -*- coding: utf-8 -*-

import datetime

dia_de_nasc = datetime.date(day=21, year=1998, month=8)

def calcular_dias_de_vida(data):
    if data is None:
        error='tared'
        return error


    hoje = datetime.date.today()
    dias_de_vida = hoje - data
    return dias_de_vida

retorno = calcular_dias_de_vida(dia_de_nasc)
print(retorno)




