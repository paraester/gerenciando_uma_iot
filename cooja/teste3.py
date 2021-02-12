import os
import subprocess
import tkMessageBox

from Tkinter import *
class Janela:
    def __init__(self,toplevel):
        print "Inicio"
        toplevel.title('Trabalho 4 - Projeto e Gerenciamento de uma IoT')
        toplevel.geometry("400x450")

        self.fr2 = Frame(toplevel, pady=5)
        self.fr2.pack()
        self.botao12 = Label(self.fr2, text='Trabalho 4 - Projeto e Gerenciamento de uma IoT', background='black', fg='white', font=('Times','14'))
        self.botao12.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=15)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='STATUS ATUAL', background='green', font=('Times','14'), command=clicado)
        self.botao2.pack(side=RIGHT)

        self.fr2 = Frame(toplevel, pady=15)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='ACENDER TUDO', background='green', font=('Times','14'), command=acender)
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=15)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text=' APAGAR TUDO ', background='green', font=('Times','14'), command=apagar)
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=10)
        self.fr2.pack()
        self.botao2 = Label(self.fr2, text='          QUAL ACENDER        ', background='BLACK', fg='white', font=('Times','14'))
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=5)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='2', background='gray', font=('Times','12'), command=lampada1)
        self.botao2.pack(side=RIGHT)

        self.botao3 = Button(self.fr2, text='3', background='gray', font=('Times','12'), command=lampada2)
        self.botao3.pack(side=RIGHT)

        self.botao4 = Button(self.fr2, text='4', background='gray', font=('Times','12'), command=lampada3)
        self.botao4.pack(side=RIGHT)

        self.botao5 = Button(self.fr2, text='5', background='gray', font=('Times','12'), command=lampada4)
        self.botao5.pack(side=RIGHT)

        self.botao6 = Button(self.fr2, text='6', background='gray', font=('Times','12'), command=lampada5)
        self.botao6.pack(side=RIGHT)

        self.botao7 = Button(self.fr2, text='7', background='gray', font=('Times','12'), command=lampada6)
        self.botao7.pack(side=RIGHT)

        self.fr2 = Frame(toplevel, pady=5)
        self.fr2.pack()
        self.botao2 = Label(self.fr2, text='          QUAL APAGAR?        ', background='black', fg='white', font=('Times','14'))
        self.botao2.pack(side=LEFT)

        self.fr2 = Frame(toplevel, pady=10)
        self.fr2.pack()
        self.botao2 = Button(self.fr2, text='2', background='gray', font=('Times','12'), command=lampada11)
        self.botao2.pack(side=RIGHT)

        self.botao3 = Button(self.fr2, text='3', background='gray', font=('Times','12'), command=lampada21)
        self.botao3.pack(side=RIGHT)

        self.botao4 = Button(self.fr2, text='4', background='gray', font=('Times','12'), command=lampada31)
        self.botao4.pack(side=RIGHT)

        self.botao5 = Button(self.fr2, text='5', background='gray', font=('Times','12'), command=lampada41)
        self.botao5.pack(side=RIGHT)

        self.botao6 = Button(self.fr2, text='6', background='gray', font=('Times','12'), command=lampada51)
        self.botao6.pack(side=RIGHT)

        self.botao7 = Button(self.fr2, text='7', background='gray', font=('Times','12'), command=lampada61)
        self.botao7.pack(side=RIGHT)

  
def clicado():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ledstatus-all.py', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Status de todas as luzes <-----', retornoScript)

def acender():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/toggle2-lightup.py', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('Ligando todas as luzes', retornoScript)

def apagar():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/toggle2-lightdown.py', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('Desligando todas as luzes', retornoScript)

def escolher():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/teste4.py', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('Escolhendo qual luz ligar', retornoScript)
def lampada1():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py', '2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada2():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada3():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada4():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py', '5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada5():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py', '6'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada6():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py', '7'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)


def lampada11():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/desligand.py', '2'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> desLigando <-----', retornoScript)

def lampada21():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/desligand.py', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> desLigando <-----', retornoScript)

def lampada31():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/desligand.py', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> desLigando <-----', retornoScript)

def lampada41():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/desligand.py', '5'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> desLigando <-----', retornoScript)

def lampada51():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/desligand.py', '6'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> desLigando <-----', retornoScript)

def lampada61():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/desligand.py', '7'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> desLigando <-----', retornoScript)

raiz=Tk()
Janela(raiz)
raiz.mainloop() 
