from django import template

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':14})

register = template.Library()

@register.filter
def conta_respostas(valor1):
    contador = 0
    for valor in valor1:
        contador +=1
    return contador

@register.filter
def porcentagem(total_respotas, resposta_cliente):
    total = 0
    for i in total_respotas:
        total += 1
    detrator = 0
    promotor = 0
    for c in resposta_cliente:
        if((resposta_cliente == 'Insatisfeito') or (resposta_cliente == 'Muito insatisfeito') or (resposta_cliente == 'Neutro')):
            detrator +=1
        else:
            promotor +=1
    
    porcent_detrator = (detrator * 100) / total
    porcent_promotor = (promotor * 100) / total

    return porcent_detrator, porcent_promotor
