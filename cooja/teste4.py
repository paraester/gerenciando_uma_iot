import os
import subprocess
import tkMessageBox

from Tkinter import *
class Janela:
    def __init__(self,toplevel):
        print "Inicio"
        toplevel.title('------>LIGANDO LAMPADAS <------')
        toplevel.geometry("300x400")



        self.botao2 = Button(self.fr2, text='1', background='green', font=('Times','14'), command=lampada1)
        self.botao2.pack(side=RIGHT)

        self.botao3 = Button(self.fr2, text='2', background='green', font=('Times','14'), command=lampada2)
        self.botao3.pack(side=RIGHT)

        self.botao4 = Button(self.fr2, text='3', background='green', font=('Times','14'), command=lampada3)
        self.botao4.pack(side=RIGHT)

        self.botao5 = Button(self.fr2, text='4', background='green', font=('Times','14'), command=lampada4)
        self.botao5.pack(side=RIGHT)

        self.botao6 = Button(self.fr2, text='5', background='green', font=('Times','14'), command=lampada5)
        self.botao6.pack(side=RIGHT)

        self.botao7 = Button(self.fr2, text='6', background='green', font=('Times','14'), command=lampada6)
        self.botao7.pack(side=RIGHT)

  
def lampada1():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py 2', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada2():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py 3', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada3():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py 4', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada4():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py 5', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada5():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py 6', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)

def lampada6():
    pastaDoScript = os.path.dirname(os.path.realpath(__file__))
    x = subprocess.Popen(['python3', pastaDoScript + '/ligand.py 7', '4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retornoScript, erros = x.communicate()
    if erros:
        print "Ocorreu algum erro.\nErro:" + erros
    print "antes "

    print retornoScript
    print "clicado"
    tkMessageBox.showinfo('----> Ligando <-----', retornoScript)


raiz=Tk()
Janela(raiz)
raiz.mainloop() 
