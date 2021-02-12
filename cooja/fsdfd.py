import os
import subprocess

from Tkinter import *
class Janela:
    def __init__(self,toplevel):
        print "Inicio"
        toplevel.title('Trabalho de IOT')
        toplevel.geometry("800x600")

        self.fr2 = Frame(toplevel, pady=30)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='Lampada 1!', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=RIGHT)

        self.fr2 = Frame(toplevel, pady=30)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='Lampada 2!', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=30)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='Lampada 3!', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=30)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='Lampada 4!', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=30)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='Lampada 5!', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=25)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='Lampada 6!', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=25)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='Lampada 7!', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=LEFT)
	
def clicado():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ledstatus-all.py', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"

raiz=Tk() 
Janela(raiz) 
raiz.mainloop() 
