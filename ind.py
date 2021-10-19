#!/usr/bin/env python3
# -*- coding: utf-8 -*-Результаты выполнения программы:

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    # Определим исходные множества
    A = {'a', 'e', 'f', 'i'}
    B = {'a', 'b', 'k', 'n',}
    C = {'e', 'f', 'n', 'o', 'w', 'x'}
    D = {'a', 'd', 'e', 'o', 'p', 't', 'u'}

    X = (A.union(B)).intersection(D)
    print(f'X = {X}')

    An = u.difference(A)
    Bn = u.difference(B)
    Y = (An.intersection(Bn)).difference(C.union(D))
    print(f'Y = {Y}')