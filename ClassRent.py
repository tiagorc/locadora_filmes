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

    def getCharge(self):
   		result = 0.0
   		if self.getMovie().getCodePrice() == ClassMovie.typeMovieRegular:
			result = result + 2
			if self.getRentedDays()>2:
				result = result + (self.getRentedDays()-2)*1.5
		elif self.getMovie().getCodePrice() == ClassMovie.typeMovieNewRelease:
			result = result + 3
		elif self.getMovie().getCodePrice() == ClassMovie.typeMovieKids:
			result = result + 1.5
			if self.getRentedDays()>3:
				result = result + (self.getRentedDays()-3)*1.5

		return result

if __name__ == '__main__':
    myRent = ClassRent()