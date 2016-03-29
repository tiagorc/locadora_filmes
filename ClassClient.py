# -*- coding: utf-8 -*-
#import java.util.Enumeration;
#import java.util.Vector;
from ClassMovie import ClassMovie
from ClassRent import ClassRent
import itertools

typeMovieRegular = 0
typeMovieNewRelease = 1 
typeMovieKids = 2

class ClassClient():
    _nome = None
    _alocacoes = []

    def __init__(self, nome):
        self._nome = nome
        self._alocacoes = []
    def addicionarAlocacao(self, arg): # arg de tipo alocacao
        self._alocacoes.append(arg)
    def getNome(self):
        return self._nome

    def calculaPontosAlocacao(self, pontos):
        return pontos + 1

    def Expresao(self):
        totalQuantidade = 0.0
        pontosFrequenciaAlocacao = 0
        alocacoes = iter(self._alocacoes)
        resultado = 'Registro de Locação para : '+ self.getNome()+'\n'

        for cada in alocacoes:
            estaQuantidade = 0.0

            # estaQuantidade += cada.getCharge()
            estaQuantidade += cada.getCharge()

            #adicionar pontos de locador frequente
            pontosFrequenciaAlocacao = self.calculaPontosAlocacao(pontosFrequenciaAlocacao)
            #adicionar bonus para uma locação de dois dias para lançamentos
            if cada.getMovie().getCodePrice() == ClassMovie.typeMovieNewRelease and cada.getRentedDays()>1:
                pontosFrequenciaAlocacao = pontosFrequenciaAlocacao +1
            #mostrar informacoes para esta locacao
            resultado = resultado + ' '+cada.getMovie().getTitle()+' '+ str(estaQuantidade)+'\n'

            #calcular totalQuantidade
            totalQuantidade = totalQuantidade + cada.getMovie().getCodePrice()

        #adicionar rodape do relatorio
        resultado = resultado + "Quantia devida é "+ str(totalQuantidade)+"\n"
        resultado = resultado + 'Voce ganhou '+ str(pontosFrequenciaAlocacao)+' pontos de locacao.'
        return resultado

if __name__ == '__main__':
    meuCliente = ClassClient('Ruben')#init: nome
    print meuCliente.getNome()
    fil01 = ClassMovie('Titanic',2) #init: (titulo, preco)
    alo01 = ClassRent(fil01,5) #filme, dias locados #init: (Filme, diasAlocado)
    alo02 = ClassRent(fil01,2) #filme, dias locados
    alo03 = ClassRent(fil01,1) #filme, dias locados

    meuCliente.addicionarAlocacao(alo01)
    meuCliente.addicionarAlocacao(alo02)
    meuCliente.addicionarAlocacao(alo03)

    print meuCliente.Expresao()