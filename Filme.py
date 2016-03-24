# -*- coding: utf-8 -*-

class Filme:
    CRIANCAS = 2
    REGULAR = 0
    NOVA_RELEASE = 1
    _titulo = None
    _precoCod = None

    def __init__(self,titulo,precoCodigo):
        self._titulo = titulo
        self._precoCodigo = precoCodigo
    def getPrecoCodigo(self):
        return self._precoCodigo
    def setPrecoCodigo(self, arg):
        self._precoCodigo = arg
    def getTitulo(self):
        return self._titulo

if __name__ == '__main__':
    meuFilme = Filme('titanic',3)