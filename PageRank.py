import copy
import numpy as np
import numpy.linalg as la


def pagerank(link_matrix, d, web_l, chosen_w):
    n = link_matrix.shape[0]
    r = 100 * np.ones(n) / n

    M = d * link_matrix + (1 - d) / n * np.ones(n)

    r_ = M @ r

    r_prev = copy.deepcopy(r_)
    r_next = M @ r_prev
    r_temp = 0

    while la.norm(r_prev - r_next) >= 0.01:
        r_temp = M @ r_next
        r_prev = r_next
        r_next = r_temp

    my_dict = {}
    k = -1
    for elm in r_next.real:
        my_dict[web_l[k+1]] = elm
        k += 1
    new_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
    print(chosen_w)
    for k, v in new_dict.items():
        if k != chosen_w:
            print(k)


a = int(input())
b = 0.5
input_string = input()
web_list = input_string.split()
Y = []
for i in range(a):
    x = []
    x.extend(map(float, input().split()))
    Y.append(x)
chosen_website = input()
M = np.array(Y)

pagerank(M, b, web_list, chosen_website)
