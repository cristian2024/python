


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
    j=n//10%100;
    for i in range(j,n):
        if mcd(i,n)==1:

            return i;

def inversa(n,mod):
    



print(alg_euclides_extendido(300,55))
print(mcd(97,300))
print(indicatriz_euler(40))