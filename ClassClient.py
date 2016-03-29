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
    _name = None
    _arrayOfRents = []

    def __init__(self, name):
        self._name = name
        self._arrayOfRents = []

    def newRent(self, rentType):
        self._arrayOfRents.append(rentType)

    def getName(self):
        return self._name

    def rentBonus(self, bonus):
        return bonus + 1

    def rentedReport(self):
        totalPrice = 0.0
        bonusRent = 0
        rents = iter(self._arrayOfRents)
        resultReport = 'Registro de Locação para : '+ self.getName()+'\n'

        for rent in rents:
            currentPrice = 0.0

            # currentPrice += rent.getCharge()
            currentPrice += rent.getCharge()

            #adicionar pontos de locador frequente
            bonusRent = self.rentBonus(bonusRent)
            #adicionar bonus para uma locação de dois dias para lançamentos
            if rent.getMovie().getCodePrice() == ClassMovie.typeMovieNewRelease and rent.getRentedDays()>1:
                bonusRent = bonusRent +1
            #mostrar informacoes para esta locacao
            resultReport = resultReport + ' '+rent.getMovie().getTitle()+' '+ str(currentPrice)+'\n'

            #calcular totalQuantidade
            totalPrice = totalPrice + rent.getMovie().getCodePrice()

        #adicionar rodape do relatorio
        resultReport = resultReport + "Quantia devida é "+ str(totalPrice)+"\n"
        resultReport = resultReport + 'Voce ganhou '+ str(bonusRent)+' pontos de locacao.'
        return resultReport

if __name__ == '__main__':
    myClient = ClassClient('Ruben')#init: nome
    print myClient.getName()
    newMovie = ClassMovie('Titanic',2) #init: (titulo, preco)
    firstRent = ClassRent(newMovie,5) #filme, dias locados #init: (Filme, diasAlocado)
    secondRent = ClassRent(newMovie,2) #filme, dias locados
    thirdRent = ClassRent(newMovie,1) #filme, dias locados

    myClient.newRent(firstRent)
    myClient.newRent(secondRent)
    myClient.newRent(thirdRent)

    print myClient.rentedReport()