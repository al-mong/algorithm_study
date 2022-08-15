T = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B_idx = []
C = sorted(B)
C.reverse()
for i in C:
    B_idx.append(B.index(i))
sum = 0
for j in range(T):
    sum += A[j]*B[B_idx[j]]

print(sum)

    