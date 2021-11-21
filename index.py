import PySimpleGUI as sg

def janela_login():
    sg.theme('DarkTeal2')
    layout = [
        [sg.Text('Nome', size=(5,0)), sg.Input(size=(40, 0), key='nome')],
        [sg.Text('idade', size=(5, 0)), sg.Input(size=(40, 0), key='idade')],
        [sg.Text('Qual e-mail você vai cadastrar?')],
        [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('senai',key='senai')],
        [sg.Text('Aceita cartão')],
        [sg.Radio('Sim','cartoes', key='aceitaCartao'), sg.Radio('Não' ,'cartoes', key='naoAceitaCartao')],
        [sg.Slider(range=(0,225),default_value=0,orientation='h',size=(30,20), key='sliderVelocidade')],
        [sg.Button('Enviar dados')],
        [sg.Output(size=(40,30))]  
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_pedido():
    sg.theme('DarkTeal2')
    layout =[
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)
    
janela1, janela2 = janela_login(), None


while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Enviar dados':
        janela2 = janela_pedido()
        janela1.hide()

    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
           
            sg.popup('Foram solicitados uma Pizza Pepperoni e uma Pizza Catupiry c/ Frango') 
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza Pepperoni')

        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza Catupiry c/ Frango')
    
        else:
            sg.popup('Você não selecionou um produto para o pedido.')