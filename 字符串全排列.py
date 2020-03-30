# 字符串全排列
def permu(s=''):
    if len(s) <=1:
        return [s]
    res = []
    for i in range(len(s)):
        for j in permu(s[0:i]+s[i+1:]):
            #print(s[i],':',j)
            res.append(s[i]+j)
    return res

if __name__ == '__main__':
    r = permu('abcd')
    print(r)
