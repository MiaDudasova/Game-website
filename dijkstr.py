def dijkstra(graf, start, koniec):
    a,vybavene,vzdialenosti = {},[],{i: 0 if i == start else 99999 for i in graf}
    while koniec not in vybavene:
        b,c,cesta = 99999,None,[koniec]
        for i in graf: 
            if i not in vybavene and vzdialenosti[i] < b: b, c = vzdialenosti[i], i
        for i, j in graf[c].items():
            k = vzdialenosti[c] + j
            if k < vzdialenosti[i]: vzdialenosti[i], a[i] = k, c
        vybavene.append(c)
    while cesta[-1] != start:
        cesta.append(a[cesta[-1]])
    return cesta
print(dijkstra({'a': {'b': 2, 'c': 4} ,'b': {'a': 2, 'c': 3, 'd': 8} ,'c': {'a': 4, 'b': 3, 'd': 2, 'e': 5} ,'d': {'b': 8, 'c': 2, 'e': 11, 'f': 22} ,'e': {'c': 5, 'd': 11, 'f': 1} ,'f': {'d': 22, 'e': 1}}, "a", "f")[::-1])