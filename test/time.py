from timeit import timeit

from src.ConfigJson import *


cfg = ConfigJson()


def main():
    print(timeit("cfg = ConfigJson()", number=100_000, globals=globals()))
    print(timeit("cfg(z=2, az=3123, b=121243, a=1, pin=3, hash=1124, xuy=16)", number=100_000, globals=globals()))
    print(timeit("cfg.get()", number=100_000, globals=globals()))
    print(timeit("cfg", number=100_000, globals=globals()))
    print(timeit("cfg['hash']", number=100_000, globals=globals()))
    print(timeit("cfg.pop('xuy', default=1)", number=100_000, globals=globals()))
    print(timeit("~cfg", number=100_000, globals=globals()))
    print(timeit("cfg.sorted_by_keys()", number=100_000, globals=globals()))
    print(timeit("cfg.sort_by_keys()", number=100_000, globals=globals()))
    print(timeit("cfg.sorted_by_values()", number=100_000, globals=globals()))
    print(timeit("cfg.sort_by_values()", number=100_000, globals=globals()))
    print(timeit("cfg.items()", number=100_000, globals=globals()))
    print(timeit("len(cfg)", number=100_000, globals=globals()))


if __name__ == '__main__':
    main()
