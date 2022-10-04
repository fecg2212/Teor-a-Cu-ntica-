def nomoduloCplx(cplx):
    # Saca el modulo de un complejo representado como una tupla
    module = ((cplx[0] ** 2 + (cplx[1] ** 2)))
    return module

def normaVector(v):
    suma = []
    for i in range(len(v)):
        mod = nomoduloCplx(v[i])
        suma.append(mod)
    return sum(list(map(int, suma)))

def superposition(vec, pos):
    c = nomoduloCplx(vec[pos])
    norma = normaVector(vec)
    super = c / norma
    return round(super, 6)

vec = [(-3, 1), (0, -2), (0, 1), (2, 0)]
print(superposition(vec, 2))

def prob(vec1, vec2):
    pro_int = np.inner(vec1, vec2)
    print(pro_int)
    n1 = 0
    n2 =0
    for i in range(len(vec1)):
        n = abs(vec1[i])
        n1 += n
    for i in range(len(vec2)):
        n = abs(vec2[i])
        n2 += n
    normas = n1 * n2
    return pro_int / normas

def amplitud(v1, v2):
    vec_conj1 = []
    for i in range(len(v1)):
        a = np.normaVector(v1[i])
        vec_conj1.append(a)
    vec_daga1 = np.array(vec_conj1)
    vec_daga1 = np.array([vec_daga1])
    vec_daga1 = (vec_daga1.T)
    norma1 = np.dot(v1, vec_daga1)
    norma1 = norma1.real
    norma1 = math.sqrt(norma1)


