# -*- coding: utf-8 -*-
from ClassMovie import ClassMovie

class ClassRent:
    def __init__(self,movie, rentedDays): #filme de tipo Filme
        self._movie = movie #Tipo filme
        self._rentedDays = rentedDays

    def getRentedDays(self):
        return self._rentedDays

    def getMovie(self):
        return self._movie

if __name__ == '__main__':
    myRent = ClassRent()