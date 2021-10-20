from collections import Counter
import pprint
from anytree import Node, RenderTree

def main() -> None:
    _list = []
    _codes = []
    
    text = '''Место для текста'''
    text = text.lower()
    chars = Counter(text)
    codes = sorted(chars)
    for i in codes:
        _codes.append([i, ''])
    _list = chars.most_common()

    print(text)
    
    while len(_list) != 2:
        _list = sorted(_list, key=lambda t: (t[1], len(t[0])), reverse=True)
        print(_list)
        t2 = _list.pop()
        t1 = _list.pop()
        t_new = ((t1[0], t2[0]), t1[1]+t2[1])
        _list.append(t_new)
    _list = sorted(_list, key=lambda t: (t[1], len(t[0])), reverse=True)

    print(_list)
    _list = [_list[0][0], _list[1][0]]
    print("\n", _list)

    root = Node("root")

    AddKeypart(_codes, _list[0], '0', root)
    AddKeypart(_codes, _list[1], '1', root)

    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

    pp = pprint.PrettyPrinter(indent = 1)
    pp.pprint(_codes)


def GetLetterList(list):
    '''Получить список букв переданного дерева'''
    letterList = []
    if isinstance(list, str):
        letterList.append(list)
    else:
        letterList += GetLetterList(list[0])
        letterList += GetLetterList(list[1])
    return letterList

def AddKeypart(list, lettersPairs, keypart, parent):
    '''Добавление части ключа буквам в переданном дереве'''
    if isinstance(lettersPairs, str):
        next(x for x in list if x[0] == lettersPairs[0])[1] += keypart
        lastKnot = Node(keypart, parent)
        Node([lettersPairs[0]], lastKnot)
    else:
        knot = Node(keypart, parent)
        AddKeypart(list, lettersPairs[0], '0', knot)
        AddKeypart(list, lettersPairs[1], '1', knot)
        lettersList = GetLetterList(lettersPairs)
        for i in range(len(lettersList)):
            next(x for x in list if x[0] == lettersList[i][0])[1] += keypart

if __name__ == '__main__':
    main()
