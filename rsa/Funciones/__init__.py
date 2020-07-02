import random



def max_min(a,b):
    if a > b:
        return [a, b]
    return [b,a]


def alg_euclides_extendido(a, b):

    #primero se ordenan los dos valores del mayor al menor#
    ord = max_min(a,b)

    #los primeros datos en los arreglos siempre seran los mismos#
    pri=[ord[0],0,1,0]
    seg=[ord[1],ord[0]//ord[1],0,1]


    #se necesitan modificar los datos de ambos arreglos, uno a la vez
    # val sirve para definir a cual de los dos modificar
    val=True

    #Cuando alguno de los arreglos llegue a cero en la primera posicion,
    # se acabo la ejecucion#
    while pri[0]!=0 and seg[0]!=0:
        if val:
            pri[0] = pri[0] % seg[0]
            pri[2] = pri[2] - (seg[1] * seg[2])
            pri[3] = pri[3] - (seg[1] * seg[3])

            #debemos asegurarnos de no dividir por cero
            if pri[0] != 0 and seg[0] != 0:
                pri[1]=(seg[0] // pri[0])

            #se modifica la variable val para que ahora modifique el otro


            val = False
        else:
            seg[0] = seg[0] % pri[0]
            seg[2] = seg[2] - (pri[1] * pri[2])
            seg[3] = seg[3] - (pri[1] * pri[3])


            if seg[0] != 0 and pri[0] != 0:
                seg[1]=(pri[0] // seg[0])


            val = True

    if val:
        return [pri[0],pri[2],pri[3]]
    else:
        return [seg[0],seg[2],seg[3]]

# si bien el algoritmo extendido de euclides puede hacer el calculo del mcd, es menos eficiente ya que ademas de este calcula otros valores, si no son necesarios en la operacion
# a realizar, es preferible usar la version especifica del mcd, tambien conocido como "algoritmo de euclides"


def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)

def fi(a,b):
    return (a-1)*(b-1)

def indicatriz_euler(n):
    # usare j para definir el valor minimo para el coprimo del valor
    #esta funcion se puede mejorar

    #j=n//10%100
    while True:
        i=get_primo_2(20,50)
        if mcd(i,n)==1:
            return i


def inversa(n,mod):
    ord=alg_euclides_extendido(n,mod)
    if ord[0]==1:
        if ord[2]<0:
            return ord[2]+mod
        return ord[2]
    return 0

def val_n(p,q):
    return p*q


def val_d(e,p,q):
    valFi = fi(p,q)
    return 1








def is_primo(a):
    if a%2==0:
        return False
    for i in range(3,a//2,2):
        if a%i==0:
            return False
    return True

#deseo generar primos aleatorios
def get_primo(fro_m):
    i=random.randrange(fro_m,1000)
    while True:
        if is_primo(i):
            return i
        i=i+1

def get_primo_2(fro_m,top):
    i=random.randrange(fro_m,top)
    while True:
        if is_primo(i):
            return i
        i=i+1

def get_publica(p,q):
    n=val_n(p,q)
    fi_1=fi(p,q)
    e=indicatriz_euler(fi_1)

    return [e,n]

def get_privada(e,p,q):
    d=inversa(e,fi(p,q))
    return [d,val_n(p,q)]


def comprobar(e,p,q):

    fi_1=fi(p,q)

    i=0
    j=0
    v=True
    while(v):
        i=i+1
        j=(1+(i*fi_1))/e
        if(j%1==0):
            v=False

    return [i,j]

def int_char(char):
    c=ord(char)
    if 65<=c<=90:
        return c-64
    elif 97<=c<=122:
        return c-96
    return 0

def char_int(int):
    if int==0:
        return '.'
    return chr(int+96)

def binario(e):
    j=[]
    return 1


def encriptar(mensaje,e,n):
    bi=str(bin(e))[2:]
    j=[]


    for i in range(len(mensaje)):
        acum=1
        h=0

        for k in reversed(range(len(bi))):
            if bi[k] == '1':
               acum=acum*(int_char(mensaje[i])**(2**h)%n)

            h=h+1

        j.append(acum%n)


    return j


def desencriptar(mensaje,d,n):
    bi=str(bin(d))[2:]
    j=[]

    for i in range(len(mensaje)):

        acum=1
        h=0
        for k in reversed(range(len(bi))):
            if bi[k]=='1':
                acum=acum*(mensaje[i]**(2**h)%n)
            h=h+1


        j.append(char_int(acum%n))

    return j







print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))

#print(encriptar("mensaje"))

print(str(bin(7))[2:])

p=get_primo(200)
q=get_primo(201)

r=get_publica(p,q)

j=get_privada(r[0],p,q)

print(inversa(j[0],fi(p,q)))
print(r[0],r[1])

k=encriptar("hola.mundo.",r[0],r[1])
h=desencriptar(k,j[0],j[1])
print(encriptar("hola.mundo.",r[0],r[1]))
print(h)




print("".join(h))

