from tkinter import *

dados = { 'cli01':'1234', 'cli02':'5555', 'cli03':'6789', 'admin':'abcd'}


janela = Tk()
janela.title('Login')
janela.geometry('800x640')

caixaLogin = Frame(janela)
caixaResp = Frame(janela)

lbuser = Label(caixaLogin,text='Usuário:')
entuser = Entry(caixaLogin)
lbpass = Label(caixaLogin, text='Senha:')
entpass = Entry(caixaLogin)
lbresult = Label(caixaResp,text='Resposta da aplicação',fg='red')


def funcvalid():
    usuario = entuser.get()
    senha = entpass.get()
    resposta =''
    dados[usuario] = senha
    if (usuario in dados):
        if (dados[usuario] != senha):
            resposta = 'Credenciais inválidas.'
            print('Senha errada.')
        else:
            print('Logado.')
        if (dados[usuario] == senha):
            print('usuario/senha ok')
            resposta = f'Entrando... Bem-vindo, {usuario}.'
            print(dados)
        else:
            print('senha errada')
            resposta = 'Credenciais inválidas.'
    else:
        print('usuario errado')
        resposta = 'Usuário inválido.'
    
    
    


    lbresult.config(text=resposta)

btValidar = Button(janela,text='Validar',command=funcvalid)


lbuser.grid(row=0,column=0,pady=20)
entuser.grid(row=0,column=1)
lbpass.grid(row=1,column=0,pady=20)
entpass.grid(row=1,column=1)

lbresult.pack()


caixaLogin.pack(side='top',pady=50)
btValidar.pack()
caixaResp.pack(side='bottom',pady=10)


janela.mainloop()