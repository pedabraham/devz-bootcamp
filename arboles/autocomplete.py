words =  ['tea','to','ted','inn','ten']

trie = {}

def build(array):
    #crear un triess
    for element in array:
        element = element.lower()
        parent = trie
        for char in element:
            if not parent.get(char,None):
                parent[char] = {}
            parent = parent[char]
        if not parent.get('.',None):
            parent['.'] = {}


def get_current_node(prefix):
    parent = trie
    for char in prefix:
        parent = parent.get(char,None)
        if not parent:
            return []
    return parent

def get_next(prefix):

    #llegamos al nodo de la ultima letra de la palabra
    parent = get_current_node(prefix)
    if not parent:
        return []

    nexts = []
    for key in parent:
        nexts.append(key)
    return nexts



def get_autocomplete(prefix):

    #llegamos al nodo de la ultima letra de la palabra
    parent = get_current_node(prefix)
    if not parent:
        return []

    stack = []

    #forma primer nivel de la stack
    for key in parent:
        stack.append({'value':key , 'children': parent[key], 'level':0})

    word = prefix
    list_word = []
    prev_level = 0
    while stack:
        node = stack.pop()
        char = node['value']

        #compone stack
        for element in node['children']:
            new_node = {'value':element, 'children': node['children'][element], 'level':node['level']+1}
            stack.append(new_node)

        #elimina los chars que ya no coresponden a la palabra
        if prev_level > node['level']:
            n_pops = prev_level - node['level'] + 1
            n_pops *= -1
            word = word[:n_pops]

        #formamos palabra
        word += char
        if char == '.':
            #añadir palabra completa a la lista de palabras
            list_word.append(word[:-1])

        prev_level = node['level']

    return list_word

build(words)
print(get_next('t'))
print(get_autocomplete('te'))
