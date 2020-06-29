

def max_min(a,b):
    if a > b:
        p = a
        m = b
    else:
        p = b
        m = a
    return [p,m];

def alg_euclides_extendido(a, b):

    #primero se ordenan los dos valores del mayor al menor#
    ord = max_min(a,b);

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



val= True
print(alg_euclides_extendido(300,55))