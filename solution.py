def solution(xs):
    prod=1
    negs= [n for n in xs if n < 0]
    posi = [n for n in xs if n > 0]
    if len(negs) % 2 == 0:
        negs.sort()
    elif len(negs) % 2!=0:
        negs.sort()
        negs.pop()
    elif len(negs) or len(posi) == 1:
        return str(prod)
    a=posi+negs
    if a:
        for x in a:
            prod *= x
        print(prod)
    return '0'
solution()
