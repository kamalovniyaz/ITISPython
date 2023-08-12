def add(tree, value):
    """добавление элемента"""
    def rec_conv(now, tp):
        if tp == list:
            now = list(now)
        if now[1] is not None:
            now[1] = rec_conv(now[1], tp)
        if now[2] is not None:
            now[2] = rec_conv(now[2], tp)
        return tuple(now) if tp == tuple else now

    if tree is None:
        return value, None, None

    list_tree = rec_conv(tree, list)
    now = list_tree
    while True:
        if value >= now[0] and now[2] is not None:
            now = now[2]
        elif now[1] is not None:
            now = now[1]
        else:
            if value > now[0]:
                now[2] = [value, None, None]
            else:
                now[1] = [value, None, None]
            break
    return rec_conv(list_tree, tuple)


def contains(tree, value):
    """проверка на наличие элемента"""
    if tree is None:
        return False

    now = tree
    while True:
        if value > now[0] and now[2] is not None:
            now = now[2]
        elif value < now[0] and now[1] is not None:
            now = now[1]
        else:
            return value in now


def tree_length(tree):
    """глубина дерева"""
    def rec_circ(now, leng):
        if now is None:
            return leng

        return max(rec_circ(now[1], leng + 1), rec_circ(now[2], leng + 1))

    return rec_circ(tree, 0)


my_tree = (5, (3, None, (4, (1, None, None), None)), (6, None, None))
value = 5
print(add(my_tree, value))
value = 2
print(add(my_tree, value))
print(contains(my_tree, 3))
print("Глубина дерева", tree_length(my_tree))
