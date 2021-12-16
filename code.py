import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

# Note the matplot tk canvas import
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# VARS CONSTS:
_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False}

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def drawChart():
    _VARS['pltFig'] = plt.figure()
    dataXY = ([0],[0])
    plt.plot(dataXY[0], dataXY[1], '.k')
        
    plt.legend(loc = 'upper left')

    plt.minorticks_on()
    plt.grid(which='major', color = 'k', linewidth = '1')
    plt.grid(which='minor', color = 'k', linestyle = ':')

    plt.title("Сравнение значений моды, медианы и среднего")
    plt.xlabel("Значения ряда")
    plt.ylabel("Отсчеты")

    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

def calculate (fig, inputSeries):
    _VARS['fig_agg'].get_tk_widget().forget()

    x = [int(s) for s in inputSeries.split()]
    c = len(x)
    sr_z = sum(x)/c
    x_sorted = sorted(x)

    if c%2 == 1:
        mediana = x_sorted[c//2]
    else:
        mediana = (x_sorted[c//2]+x_sorted[c//2-1])/2

    k = 0

    def count_x(lst,x): # функция, которая найдет число вхождений элемента
        count = 0
        for i in lst:
            if (i == x):
                count+=1
        return count

    lst_for_uniq = []
    for i in x_sorted:
        lst_for_uniq.append(count_x(x_sorted,i)) # новый список с числом вхождений
    m = max(lst_for_uniq) #  максимальное значение списка

    for i in range(c): #по достижению первого макисмального значения- дроп
        if lst_for_uniq[i] == m:
            k = i  # с запоминанием индекса
            break
        
    moda = x_sorted[k]

    x_x = []

    for i in range(c):
        x_x.append(i+1)
        
    
    # plt.close("all")
    plt.clf()
    plt.plot(x,x_x,'ro')
    # минимальное значение по оси Y для красивой сетки

    if x_sorted[0] >= 1:
        plt.vlines(mediana, 0, x_sorted[c-1], color = 'k' ,linestyles = '--',label = 'Медиана') #вместо многоточия - значение по оси абсцисс.
        plt.vlines(moda, 0, x_sorted[c-1], color = 'g',linestyles = '--',label = 'Мода')
        plt.vlines(sr_z, 0, x_sorted[c-1], color = 'm',linestyles = '--',label = 'Среднее значение')
        plt.ylim([0, x_sorted[c-1]])
    else:
        plt.vlines(mediana, x_sorted[0], x_sorted[c-1], color = 'k' ,linestyles = '--',label = 'Медиана') #вместо многоточия - значение по оси абсцисс.
        plt.vlines(moda, x_sorted[0], x_sorted[c-1], color = 'g',linestyles = '--',label = 'Мода')
        plt.vlines(sr_z, x_sorted[0], x_sorted[c-1], color = 'm',linestyles = '--',label = 'Среднее значение')
        plt.ylim([x_sorted[0]-1,x_sorted[c-1]])
        
    plt.legend(loc = 'upper left')

    plt.minorticks_on()
    plt.grid(which='major', color = 'k', linewidth = '1')
    plt.grid(which='minor', color = 'k', linestyle = ':')

    plt.title("Сравнение значений моды, медианы и среднего")
    plt.xlabel("Значения ряда")
    plt.ylabel("Отсчеты")

    _VARS['fig_agg'] = draw_figure(_VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

if __name__ == "__main__":
    layout = [
        [sg.Text('Enter series'), sg.InputText()],
        [sg.Canvas(key='figCanvas')],
        [sg.OK(), sg.Cancel()] 
    ]

    _VARS['window'] = sg.Window('Series analysis',
                            layout,
                            finalize=True,
                            resizable=True,
                            element_justification="right")

    fig = plt.figure()
    drawChart()
    while True:
        event, values = _VARS['window'].read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        calculate(fig, values[0])
    _VARS['window'].close()
