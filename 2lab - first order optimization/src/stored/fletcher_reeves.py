import numpy as np
from scipy import optimize


def fletcher_reeves(x0, e, f: (), find__min_f: (), bounds):
    path = []
    x_cur = np.array(x0)
    path.append(x_cur)
    n = len(x0)
    k = 0
    grad = optimize.approx_fprime(x_cur, f, e ** 4)
    prev_grad = 1
    p_k = -1 * grad
    while np.linalg.norm(grad) > e:
        if k % n == 0:
            p_k = -1 * grad
        else:
            b_k = (np.linalg.norm(grad) ** 2) / (np.linalg.norm(prev_grad) ** 2)
            prev_pk = p_k
            p_k = -1 * grad + b_k * prev_pk
        a = find__min_f(bounds[0], bounds[1], e, lambda x: f(x_cur + p_k * x))[0]
        x_cur = x_cur + a * p_k
        path.append(x_cur)
        k += 1
        prev_grad = grad
        grad = optimize.approx_fprime(x_cur, f, e ** 4)
    return x_cur, f(x_cur), len(path), path
