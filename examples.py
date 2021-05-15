if __name__ == '__main__':
    from ConfigJSON import *

    CONFIG_FILENAME = None
    # CONFIG_FILENAME = 'test.json'
    cfg = configjson(CONFIG_FILENAME)

    g = cfg(
        z=2,
        a=1,
        pin=3,
        hash=3,
        xuy=16).get()

    print(type(g))  # <class 'dict'>
    print(cfg)

    try:
        print(~cfg)
    except RepetitionsError as e:
        print(f'[X] {type(e).__name__}: {e}')

    try:
        print(cfg.sorted_by_keys())
    except NotSameTypeError as e:
        print(f'[X] {type(e).__name__}: {e}')
    except RepetitionsError as e:
        print(f'[X] {type(e).__name__}: {e}')

    try:
        print(cfg.sorted_by_values())
    except NotSameTypeError as e:
        print(f'[X] {type(e).__name__}: {e}')
    except RepetitionsError as e:
        print(f'[X] {type(e).__name__}: {e}')
