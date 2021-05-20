def saltos(array):
    memo = {}
    def min_saltos(inicio):
        if inicio >= len(array) - 1:
            return 0
        saltos = 1
        max_foward = array[inicio]
        if inicio + max_foward + 1 < len(array):
            limite = inicio + max_foward +  1
        else:
            limite = len(array)
        min_p_saltos = len(array)
        for i in range(inicio + 1, limite):
            p_saltos = memo.get(i,None)
            if not p_saltos:
                p_saltos = min_saltos(i)
                memo[i] = p_saltos
            if p_saltos == 'fail':
                continue
            if p_saltos < min_p_saltos:
                min_p_saltos = p_saltos
        if inicio + 1 == limite:
            return 'fail'
        saltos += min_p_saltos
        return saltos
    mins = min_saltos(0)
    return mins

print(saltos([4, 2, 0, 3, 2, 0, 1, 8]))
