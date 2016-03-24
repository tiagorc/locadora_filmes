# -*- coding: utf-8 -*-

class ClassMovie:
    typeMovieRegular = 0
    typeMovieNewRelease = 1 
    typeMovieKids = 2

    _title = None
    _codePrice = None

    def __init__(self,title,codePrice):
        self._title = title
        self._codePrice = codePrice

    def getCodePrice(self):
        return self._codePrice

    def setCodePrice(self, newCodePrice):
        self._codePrice = newCodePrice
    
    def getTitle(self):
        return self._title

if __name__ == '__main__':
    myMovie = ClassMovie('titanic',3)