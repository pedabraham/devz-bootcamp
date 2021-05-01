pid = [1,3,5,10]
ppid = [3,0,3,5]
kill = 3

def kill_process(pip,ppid,kill):
    class node(object):
        def __init__(self, value = None):
            self.value = value
            self.children = []

    nodes_ht = {}

    for i in range(len(pid)):
        hijo_val = pid[i]
        padre_val = ppid[i]
        node_padre = nodes_ht.get(padre_val, None)

        node_hijo = nodes_ht.get(hijo_val, None)
        if not node_hijo:
            node_hijo = node(hijo_val)

        if not node_padre:
            new_node = node(padre_val)
            new_node.children.append(node_hijo)
            nodes_ht[padre_val] = new_node
            nodes_ht[hijo_val] = node_hijo
        else:
            node_padre.children.append(node_hijo)
            nodes_ht[hijo_val] = node_hijo


    node_to_kill = nodes_ht.get(kill, None)
    if node_to_kill:
        stack = []
        out_list = []

        stack.append(node_to_kill)

        while stack:
            top = stack.pop()
            out_list.append(top.value)

            for child in top.children:
                stack.append(child)

        return out_list

    else:
        return None

print(kill_process(pid,ppid,5))
