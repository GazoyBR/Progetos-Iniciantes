A = 112323
B = 231132
C = 323211

if A <= B  and A <= C:
    if B <= C:
        print("Ordem Crescente: {}, {}, {}".format(A,B,C))


elif B <= C:
    print("Ordem Crescente: {}, {}, {}".format(A,B,C))




else:
    print("Ordem Crescente: {}, {}, {}".format(A,C,B))



