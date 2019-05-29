() #tuplet
[] or list() #lista
{} or set() #sets
frozenset()#set care nu poate fii modificat
dict(key=value) or {'key':'value'}#dictionar
nonlocal variabila#forteaza o variabila ca scope in enclosed dar nu in global
global variabila#forteaza o variabila in global dar nu si in enclosed

from collections import namedtuple#importa namedtuple
from collections import defaultdict#importa defaultdict
from collections import ChainMap#importa ChainMap=dict cu mapare usoara
from itertools import count#count numarala la nesfarsit
from itertools import compress#restrange in functie de selector
from itertools import permutations#permutari
from functools import reduce#reduce o lista
from operator import mul#functie care returneaza produsul
from math import sqrt#import radical

remainders = remainders[::-1]#reverse a tuple,list
divmod(Deimpartit,Impartitor)#returneaza un puplu de forma(Cat,Rest)
continue#sare peste blocul de cod si continua iteratia
break#iese din iteratie
count(start,step)#start este valoarea initiala si step pasul adaugat la fiecare iteratie
compress(data,selector)#foloseste un tuplet/lista si il restrange in functie de selector(0/1)
permutations(permutat,marimea)#fara marime face permutare completa(ABC,BCA...),cu marimea grupeaza
reduce(fuctia,lista)#functia care i se aplica listei pana ajunge un element
mul(a,b)#acelasi lucru ca a*b
lambda parametrii : functie
map(functie,structura)#aplica functia fiecarui element din structura
zip(struct,struct1)#compina doua structuri
filter(functie,structura)#filtreaza o structura dupa o functie data
yield#este folosit pentru generator

##ternary operator
code if cond else code
##for sequence
# %%
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):#range() +len()
    print(position, surnames[position])
# %%
for surname in surnames:
    print(surname)
# %%
for position, surname in enumerate(surnames):#alternativa la primul for
    print(position, surname)
# %%
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities=['Romania','Polonia','German','Russian']
for person, age in zip(people, ages):
    print(person, age)
#%%
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)
##While
while(cond):
    execute
else: #dupa ce while este executat se executa else,
#daca se iese fortat din while(break) else nu se mai executa
    exectue

#%%
for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ') # instead of newline, comma and space

#%%
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10
even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))
print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

#%%
print(list(permutations('ABC')))


#%%
###LISTA
a.append(args) #adauga la sfarsit
a.count(args)#numara cate elememte cu valoarea dintre paranteze
a.extend(*args)#mareste lista, args pot fii si un tuplu sau o lista
a.index(args)#returneaza pozitia elementului introdus
a.insert(poz,args)#adauga un element pe pozitia data
a.pop()#elimina SI returneaza ultima valoare
a.pop(args)#face pop la elementul de pe pozitia data
a.remove(args)#sterge elementul introdus
a.reverse()#rastoarna lista
a.sort()#sorteaza lista
a.clear()#sterge lista

min(list)#returneaza minimul
max(list)#returneaza maximul
sum(list)#returteaza suma tuturor elementelor
len(list)#returneaza lungimea
list+list#concatenare
list*2#dubleaza lista actuala
[x+5 for x in lisat]#modifica toate elementele din lista


###SETS
a.add(args)#adauga element
a.remove(args)#sterge elementul
a | b#uniune
a & b#intersectie
a - b#diferenta


###DICTIONARE
a = dict(A=1, Z=-1)
b = {'A': 1, 'Z': -1}
c = dict(zip(['A', 'Z'], [1, -1]))
d = dict([('A', 1), ('Z', -1)])
e = dict({'Z': -1, 'A': 1})
len(d)#lungimea dictionarului
del d[key]#sterge key si elementul ei
d.clear()#sterge dictionarul
d.keys()#afiseaza cheile
d.values()#afiseaza doar valorile
d.items()#afiseaza perechile key:value
d.popitem()#sterge un item random
d.pop(key)#sterge itemul cu cheia key
d.update(key=value)#adauga sau mofidifica
d.update({'key':'value'})
d.get(key,default)#returneaza valuarea d['key'], in caz ca nu exista key se afiseaza valuarea default
d.setdefault(item)#daca a lipseste returneaza valoare si adauga itemul


###NAMEDTUPLET
Vision = namedtuple('Vision',['left','right'])#initializeaza tipul VISION
Andrei = Vision(9.3,9.6)#Se creazaa tupletul Andrei
Andrei.right#se aceseaza o parte a tupletului


###DEFAULTDICT
dd = defaultdict(int)#initializeaza
dd['age']+=1#adauga 1 la nici o valoare
dd['age']=39


###CHAINMAP
default_connection = {'host': 'localhost', 'port': 4567}
connection = {'port': 5678}
conn = ChainMap(connection,default_connection)#map creation
conn.maps#vedem map


###FUNCTII
def nume_functie(input):
    code
    return optional

def functie(variabila_pozitionala,*args_tuplu,variabila_keyword_only,**kwargs_dictionar):
    print('pozitionala nu are nevoie de key se ia dupa poziite')
    print('''keyword, trebuie specificata key//nu poate fii pusa
    dupa (**) mai poate fii notata cu a,*,b(b fiind keyword-only''')


###COMPREHENSIONS
[n ** 2 for n in range(10)]#creeaza o lista cu patrate
[n ** 2 for n in range(10) if not n % 2]#creaza o lista cu toate patratele divizibile cu 2
#creeaza o lista cu 3 tuplete de forma de mai jos
mx=10
legs = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}


###GENERATORS
##FUNCTION
#%%
def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k += 1
for n in geometric_progression(2, 5):
    print(n)

##EXPRESION
#%%
cubes_gen = (k**3 for k in range(10))
print(list(cubes_gen))
print(list(cubes_gen))


###DECORATORS
#%%
def folosestefunc(functie,*args, **kwargs):
    functie(*args)
    print("cred ca merge")

def functiewow(str="WOW"):
    print(str)

folosestefunc(functiewow,"LOOOL")

#%%
from time import sleep, time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper

@measure
def f(sleep_time=0.1):
    """I'm a cat. I love to sleep! """
    sleep(sleep_time)

f(sleep_time=0.3)
print(f.__name__, ':', f.__doc__)
