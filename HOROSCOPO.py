
class Horoscopo:
    #def para iniciarlizar las instancias
    def __init__(self, año):
        self.año = año
    
    def mi_animal(self):
        #in para verificar si un valor está presente en una lista
        if self.año in [2020, 2008, 1996, 1984, 1972, 1960]:
            print("Su animal del horóscopo chino es la Rata")
        elif self.año in [2021, 2009, 1997, 1985, 1973, 1961]:
            print("Su animal del horóscopo chino es el Buey")
        elif self.año in [2022, 2010, 1998, 1986, 1974, 1962]:
            print("Su animal del horóscopo chino es el Tigre")
        elif self.año in [2023, 2011, 1999, 1987, 1975, 1963]:
            print("Su animal del horóscopo chino es el Conejo")
        elif self.año in [2024, 2012, 2000, 1988, 1976, 1964]:
            print("Su animal del horóscopo chino es el Dragón")
        elif self.año in [2025, 2013, 2001, 1989, 1977, 1965]:
            print("Su animal del horóscopo chino es la Serpiente")
        elif self.año in [2026, 2014, 2002, 1990, 1978, 1966]:
            print("Su animal del horóscopo chino es el Caballo")
        elif self.año in [2027, 2015, 2003, 1991, 1979, 1967]:
            print("Su animal del horóscopo chino es la Cabra")
        elif self.año in [2028, 2016, 2004, 1992, 1980, 1968]:
            print("Su animal del horóscopo chino es el Mono")
        elif self.año in [2029, 2017, 2005, 1993, 1981, 1969]:
            print("Su animal del horóscopo chino es el Gallo")
        elif self.año in [2030, 2018, 2006, 1994, 1982, 1970]:
            print("Su animal del horóscopo chino es el Perro")
        elif self.año in [2031, 2019, 2007, 1995, 1983, 1971]:
            print("Su animal del horóscopo chino es el Cerdo")
        else:
            print("No se encontró un animal correspondiente para el año ingresado")
        

fecha = input("Ingrese su fecha de nacimiento dd/mm/aaaa: ")
#map sirve para aplicar una función a cada elemento y devolver el iterable con los resultados
#divide la cadena fecha en partes utilizando el separador'/' 
dia, mes, año = map(int, fecha.split('/'))
#creamos un objeto y pasamos el valor de la variable "año"
horoscopo = Horoscopo(año)
#llamamos al metodo
horoscopo.mi_animal()
