#! /usr/bin/env/python3

def memorized_cut_rod_aux(p, n, r, s):
    if r[n]>= 0: 
        return r[n]
    r[n] = 0
    for i in range(1, n+1):
        ret = p[i] + memorized_cut_rod_aux(p, n-i, r, s)
        if r[n] < ret: 
            # record larger revenue
            r[n] = ret
            s[n] = i        
    return r[n]

def cut_rod(p, n):
    r = [-1 for _ in range(n+1)]
    s = [i for i in range(n+1)]
    memorized_cut_rod_aux(p, n, r, s)
    # the max revenue
    rev = r[n]
    subs = []
    # print path
    while n > 0:
        subs.append(s[n])
        n -= s[n]
    return rev, subs


def test():
    p = [0,1,5,8,9,10,17,17,20,24,30]
    n = 9
    rev,subs = cut_rod(p, n)
    print(n, rev, subs)

test()
