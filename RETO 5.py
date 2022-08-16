#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para el funcionamiento de las librería csv y json respectivamente
import csv, json
"""NOTAS: 
    - PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    - LA CONSOLA TE DIRÁ SI TU SOLUCIÓN ES CORRECTA O NO
    - NO olvidar evaluar tu solución
"""

"""Inicio espacio para programar funciones propias"""
#En este espacio podrás programar las funciones que deseas usar en la función solución (ES OPCIONAL)

import pandas as pd
from collections import Counter

"""Fin espacio para programar funciones propias"""

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    
    # abrimos globant
    lect = pd.read_csv('GLOBANT.csv')

    # pasamos el archivo a dataframe
    globant = pd.DataFrame(lect)

    # creamos el dataframe de analisis
    analisis = pd.DataFrame()
    
    #Llmamos los datos de Fecha de analisis con los datos de Date de globant 
    analisis['Fecha'] = globant['Date']
    #llamos los datos de comportamiento restando open - close y fijando condicion
    analisis['Comportamiento de la accion'] = globant.apply(lambda x: 'SUBE' if x.Close - x.Open > 0 else 
                                                                    'BAJA' if x.Close - x.Open < 0 else 'ESTABLE', axis=1)
    #llamamos los datos para puntp medio h-l/2
    analisis['Punto medio HIGH-LOW'] = (globant['High'] - globant['Low'])/ 2
    #convertimos a csv separado por tabulacion
    analisis.to_csv('analisis_archivo.csv', sep='\t', index=False)
    
    dat = {'date_lowest_price': [],
        'lowest_price': [],
        'date_highest_price': [],
        'highest_price': [],
        'cantidad_veces_sube': [],
        'cantidad_veces_baja': [],
        'cantidad_veces_estable': [],}

    contar = Counter(list(zip(analisis['Comportamiento de la accion'])))
    dat["date_lowest_price"] = ''.join(list(globant.loc[globant['Low'] == globant['Low'].min()]['Date']))
    dat["lowest_price" ] = globant['Low'].min()
    dat["date_highest_price"] = ''.join(list(globant.loc[globant['High'] == globant['High'].max()]['Date']))
    dat["highest_price" ] = globant['High'].max()
    dat["cantidad_veces_sube" ] = contar['SUBE',]
    dat["cantidad_veces_baja" ] = contar['BAJA',]
    dat["cantidad_veces_estable" ] = contar['ESTABLE',]
    
    with open('detalles.json', 'w') as new:
        json.dump(dat, new)