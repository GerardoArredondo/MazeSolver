class Estado:
    def __init__(self, e):
        self.e = e

    def get_proximos(self):
        if self.e[0] == 0:
            e = self.e[:]
            e[0], e[1] = e[1], e[0]
            e1 = Estado(e)
            e = self.e[:]
            e[0], e[3] = e[3], e[0]
            e2 = Estado(e)
            return [e1, e2]

    def __eq__(self, other):
        return self.e == other.e

    def __str__(self):
        s = ''
        for e in self.e:
            s += str(e) + ' '
        return s

def bfs(e_i, e_f):
    visitados = {}
    cola = []
    actual = e_i
    cola.append(e_i)

    while actual != e_f:
        actual = cola.pop(0)
        if actual.e not in visitados:
            visitados[actual.e] = True
            hijos = actual.get_proximos()
            for h in hijos:
                cola.append(h)

if __name__ == '__main__':
    inicial = [8, 7, 6, 5, 4, 3, 2, 1, 0]
    e = Estado(inicial)
    print(e)

    final = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    e_final = Estado(final)

    bfs(e, e_final)

