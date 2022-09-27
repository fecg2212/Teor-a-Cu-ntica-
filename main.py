def nomoduloCplx(c1):
    # Saca el modulo de un complejo representado como una tupla
    module = ((c1[0] ** 2 + (c1[1] ** 2)))
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

def trasnsition(vec1, vec2):
    pro_int = np.inner(vec1, vec2)
    print(pro_int)
    norma1 = 0
    norma2 =0
    for i in range(len(vec1)):
        n = abs(vec1[i])
        norma1 += n
    for i in range(len(vec2)):
        n = abs(vec2[i])
        norma2 += n
    normas = norma1 * norma2
    return pro_int / normas

# PRUEBAS



