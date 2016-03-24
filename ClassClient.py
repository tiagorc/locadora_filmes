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


    #mandar esse metodo para a classe Alocacao e chama-lo de getCharge()
    def quantidadePara(self, alocacao):
        resultado = 0.0
        #Determinar valores para cada linha
        if alocacao.getMovie().getCodePrice() == typeMovieRegular:
            resultado = resultado + 2
            if alocacao.getRentedDays()>2:
                resultado = resultado + (alocacao.getRentedDays()-2)*1.5
        elif alocacao.getMovie().getCodePrice() == typeMovieNewRelease:
            resultado = resultado + 3
        elif alocacao.getMovie().getCodePrice() == typeMovieKids:
            resultado = resultado + 1.5
            if alocacao.getRentedDays()>3:
                resultado = resultado + (alocacao.getRentedDays()-3)*1.5

        return resultado

    def Expresao(self):
        totalQuantidade = 0.0
        pontosFrequenciaAlocacao = 0
        alocacoes = iter(self._alocacoes)
        resultado = 'Registro de Locação para : '+ self.getNome()+'\n'

        #while(alocacoes):
        for cada in alocacoes:
            estaQuantidade = 0.0
            #cada = next(alocacoes) #cada tipo alocacao
            #cada dever ser de tipo alocacao
            estaQuantidade = self.quantidadePara(cada)

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



# problemas
#
# resultado quantidadetotal errada
# 