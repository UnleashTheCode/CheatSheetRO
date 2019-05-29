###DEFINIREA CLASEI
class Nume_clasa(): #definirea clasei
    pass    #blocul clasei

###ATRIBUTE/ATRIBUTE DINAMICE
#%%
class Persoana():
    specie="Om"

print(Persoana.specie)
Persoana.inViata=True #atribut clasa adaugat dinamic
print(Persoana.inViata)
print()

man=Persoana()
print(man.specie)#inherited
print(man.inViata) #inherited
print()

Persoana.inViata=False
print(man.inViata) #modificata automat
print()

man.nume='Dan' #atribut instanta adaugat dinamic
man.prenume='Teodor-Andrei'
print(man.prenume,man.nume)

###ARTRIBUTE IN UBRBA(ATTRIBUTE SHADOWING)
'''Daca nu se gasesc in instanta(obiect)
    Valorile se cauta in clasa'''
#%%
class Point():
    x=10
    y=7

p=Point()
print(p.x) #x-ul din clasa
print(p.y)
print()

p.x=12 #p.x este setat
print(p.x)
print(Point.x) #x-ul clasei nu este afectat
print()

del p.x #p.x este sters
print(p.x)#se cauita din nou in clasa
print()

p.z=3 #z este atribut de instanta
print(p.z)
#print(Point.z) #z nu exista in clasa Point


###SELF
#%%
class Square():
    side=8
    def area(self): #aici self face referire la obiectul in sine
        return self.side**2 #aici self face referire la atributul din obiect

sq=Square()
print(sq.area()) #side este luat din clasa
print(Square.area(sq)) #acelasi lucru cu cea de mai sus
print()

sq.side=10
print(sq.side) #side este gasit in obiect(instanta)

#%%
class Price():
    def final_price(self,vat,discount=0):
        return (self.net_price * (100+vat)/100)-discount

p1=Price() #initializare fara parametrii
p1.net_price=100 #seteaza net_price
print(Price.final_price(p1,20,10)) #p1 fiind self
print(p1.final_price(20,10)) #apelare fara self

#%%
class Rectangle():
    def __init__(self,sideA,sideB): #magic method// initieaza obiectul
        self.sideA=sideA    
        self.sideB=sideB
    def area(self):
        return self.sideA*self.sideB

r1=Rectangle(10,4)  #initializare cu parametrii
print(r1.sideA,r1.sideB)
print(r1.area())
r2=Rectangle(7,3)
print(r2.area())


###Inheritance and composition
'''La inheritance este o relatie de #Is-A#
La composition este o relatie de #Has-A#'''
#%%
class Engine(): #clasa parinte
    def start(self):
        pass
    def stop(self):
        pass

class ElectricEngine(Engine): #Is-A engine #Clasa copil
    pass

class V8Engine(Engine):
    pass

class Car():
    engine_cls= Engine
    def __init__(self):
        self.engine=self.engine_cls() #Has-A engine #clasa compusa
    def start(self):
        print('Starting engine {} for car {}...Wroom,wroom!!!'.format(
            self.engine.__class__.__name__,
            self.__class__.__name__))
        self.engine.start()
    def stop(self):
        self.engine.stop()

class RaceCar(Car):
    engine_cls=V8Engine

class CityCar(Car):
    engine_cls=ElectricEngine

class F1Car(RaceCar):
    engine_cls=V8Engine

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car]
for car in cars:
    car.start()

#%%
class Book():
    def __init__(self,title,publisher,pages):
        self.title=title
        self.publisher=publisher
        self.pages=pages

class Ebook(Book):
    def __init__(self,title,publisher,pages,format_):
        self.title=title
        self.publisher=publisher
        self.pages=pages
        self.format_=format_
    #Book.__init__(self, title, publisher, pages)
    # self.format_ = format_
    '''super().__init__(title, publisher, pages)
        self.format_ = format_'''

#Multipple inheritance
#%%
class Shape:
    geometric_type = 'Generic Shape'

    def are(self):
        raise NotImplementedError
    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self,ratio,topleft):
        print('Plotting at {}, ratio{}.'.format(topleft,ratio))

class Polygon(Shape,Plotter):
    geometric_type='Polygon'

class RegularPolygon(Polygon):
    geometric_type='Regular Polygon'

    def __init__(self,side):
        self.side=side

class RegularHexagon(RegularPolygon):
    geometric_type='Regular Hexagon'
    def area(self):
        return 1.5*(3**.5*self.side**2)

class Square1(RegularPolygon):
    geometric_type='Square'
    def area(self):
        return self.side**2

hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8,(75,77))

