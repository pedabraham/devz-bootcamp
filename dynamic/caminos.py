def caminos(inicio,target):
    memo = {}
    def _caminos(inicio,target):
        if inicio == target:
            return 0
        if solo_un_camino(inicio,target):
            return 1
        x = inicio[0]
        y = inicio[1]
        coordenada_x = (x + 1, y)
        coordenada_y = (x, y + 1)

        arriba = memo.get(coordenada_y, None)
        if not arriba:
            arriba = _caminos(coordenada_y,target)
            memo[coordenada_y] = arriba

        derecha = memo.get(coordenada_x, None)
        if not derecha:
            derecha = _caminos(coordenada_x,target)
            memo[coordenada_x] = derecha

        total = arriba + derecha
        return total

    def solo_un_camino(inicio, target):
        if target[0] == inicio[0] or target[1] == inicio[1]:
            return True

        x_dif = target[0] - inicio[0]
        y_dif = target[1] - inicio[1]
        if x_dif + y_dif == 1:
            return True
        else:
            return False
    return _caminos(inicio,target)

print(caminos((0,5),(5,5)))
