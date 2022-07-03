from lab1.fibonacci_method import fibonacci_method
from lab2.stored.fletcher_reeves import fletcher_reeves
from lab2.stored.powell_method import powell_method
from lab2.stored.visualization import draw_lines


def f1(vec):
    x, y = vec
    return 4 * pow((x - 5), 2) + pow((y - 6), 2)


def f2(vec):
    x, y = vec
    return 2 * x ** 2 + x * y + y ** 2


def f3(x):
    x1, x2, x3, x4 = x
    return ((x1 + 10 * x2) ** 2 +
            5 * (x3 - x4) ** 2 +
            (x2 - 2 * x3) ** 4 +
            10 * (x1 - x4) ** 4)


if __name__ == '__main__':
    x0 = (-4, -4)
    eps = 0.05
    bounds = (-100, 100)
    vis_bounds = (-5, 5)
    f = f2
    res1 = (fletcher_reeves(x0=x0, e=eps, f=f, find__min_f=fibonacci_method, bounds=bounds))
    print(res1)
    draw_lines(f, vis_bounds, vis_bounds, res1[3])
    res2 = (powell_method(x0=x0, e=eps, f=f, find__min_f=fibonacci_method, bounds=bounds))
    print(res2)
    draw_lines(f, vis_bounds, vis_bounds, res2[3])
