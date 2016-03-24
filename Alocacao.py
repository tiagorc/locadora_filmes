# -*- coding: utf-8 -*-
from ClassMovie import ClassMovie

class Alocacao:
    def __init__(self,filme, diasAlocado): #filme de tipo Filme
        self._filme = filme #Tipo filme
        self._diasAlocados = diasAlocado
    def getDiasAlocados(self):
        return self._diasAlocados
    def getMovie(self):
        return self._filme

if __name__ == '__main__':
    minhaAlocacao = Alocacao()