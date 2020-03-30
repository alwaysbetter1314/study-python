def powerset(items):
    n= len(items)
    res = []
    for i in range(2**n):
        combo =[]
        for j in range(n):
            if (i>>j) % 2 ==1:
                combo.append(items[j])
        res.append(combo)
    return res

if __name__ == '__main__':
    print(powerset(['1','2','3']))
