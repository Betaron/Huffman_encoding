def main() -> None:
    print('Вводите пары: "символ-колличество"')
    print('Для завершения ввода введите "!Q"')
    _list = []
    _codes = []
    inp = input()

    while inp != "!Q":
        split = inp.split('-')
        tpl = ((split[0]), int(split[1]))
        _codes.append([split[0], ""])
        _list.append(tpl)
        inp = input()
    
    
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

    AddKeypart(_codes, _list[0], '0')
    AddKeypart(_codes, _list[1], '1')

    print(_codes)

def GetLetterList(list):
    letterList = []
    if isinstance(list, str):
        letterList.append(list)
    else:
        letterList += GetLetterList(list[0])
        letterList += GetLetterList(list[1])
    return letterList

def AddKeypart(list, lettersPairs, keypart):
    if isinstance(lettersPairs, str):
        next(x for x in list if x[0] == lettersPairs[0])[1] += keypart
    else:
        AddKeypart(list, lettersPairs[0], '0')
        AddKeypart(list, lettersPairs[1], '1')
        lettersList = GetLetterList(lettersPairs)
        for i in range(len(lettersList)):
            next(x for x in list if x[0] == lettersList[i][0])[1] += keypart

if __name__ == '__main__':
    main()
