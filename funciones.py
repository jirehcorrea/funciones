print("--ejemplo de funciones--")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print(f"chat {mensa}")
    
def ellacontesta(mensa):
    print(f"chat ella: {mensa}")
    
def escribenombre(ap,n):
    print(f"Tu nombre completo es : {n} {ap}")
    
def suma(a,b):
    s=a+b
    return s

# llamadas a funnciones
hola()
chat("que bonita esta ")
ellacontesta("gracias")
escribenombre("correa","jireh")
print("--Operaciones basicas--Suma--")
c1=int(input("ingresa un numero"))
c2=int(input("ingresa un numero"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

def resta(c,d):
    s=c-d
    return s

print("--Resta--")
c3=int(input("ingresa un numero"))
c4=int(input("ingresa un numero"))
dameresta=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {dameresta}")

def multiplicacion(e,f):
    s=e*f
    return s

print("--Multiplicacion--")
c5=int(input("ingresa un numero"))
c6=int(input("ingresa un numero"))
damemultiplicacion=multiplicacion(c5,c6)
print(f"La multiplicacion de {c5} * {c6} = {damemultiplicacion}")

def divicion(g,h):
    s=g/h
    return s

print("--Divicion--")
c7=int(input("ingresa un numero"))
c8=int(input("ingresa un numero"))
damedivicion=divicion(c7,c8)
print(f"La divicion de {c7} / {c8} = {damedivicion}")