#http://codeforces.com/contest/754/problem/A

n, a = int(input()), list(map(int, input().split()))
x = next((i for i, ai in enumerate(a) if ai), None) # find index of first non-zero elements in a
if x is None:
    print('NO')
elif sum(a):
    print('YES', 1, '1 {}'.format(n), sep='\n')
else:
    print('YES', 2, '1 {}'.format(x + 1), '{} {}'.format(x + 2, n), sep='\n')
