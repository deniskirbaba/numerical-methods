import numpy as np
from scipy import optimize


def powell_method(x0, e, f: (), find__min_f: (), bounds):
    path = []
    x_cur = np.array(x0)
    x_prev = x_cur
    t_vec = [x_cur]
    path.append(x_cur)
    n = len(x0)
    k, i = 0, 0
    d_vec = np.eye(n).tolist()
    d_vec.append(d_vec[0])
    d_vec = np.array(d_vec)
    while True:
        a = find__min_f(bounds[0], bounds[1], e, lambda x: f(t_vec[i] + d_vec[i] * x))[0]
        t_vec.append(t_vec[i] + d_vec[i] * a)
        if i == n - 1:
            if np.linalg.norm(t_vec[0] - t_vec[n]) < e:
                x_cur = t_vec[n]
                path.append(x_cur)
                return x_cur, f(x_cur), path
            i += 1
        elif i == n:
            x_cur = t_vec[n + 1]
            path.append(x_cur)
            if np.linalg.norm(t_vec[1] - t_vec[n + 1]) < e:
                return x_cur, f(x_cur), len(path), path
            else:
                if np.linalg.norm(x_cur - x_prev) < e:
                    return x_cur, f(x_cur), len(path), path
                k += 1
                i = 0
                rank = np.linalg.matrix_rank(d_vec)
                if rank == n:
                    d_vec[0] = d_vec[n] = t_vec[n + 1] - t_vec[1]
                    for k in range(1, n - 1):
                        d_vec[k] = d_vec[k + 1]
                t_vec.clear()
                t_vec.append(x_cur)
        else:
            i += 1
