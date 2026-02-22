tpl = (3, 5, 1, 6, 7, 3, 4, 7)

def tpl_sort(tpl):
    check = None
    for i in tpl:
        check = isinstance(i, int)
    lst = sorted(list(tpl)) if check else None
    if check:
        tpl = tuple(lst)
        print(tpl)
    else:
        print(tpl)

tpl_sort(tpl)

