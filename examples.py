if __name__ == '__main__':
    from ConfigJson import *

    CONFIG_FILENAME = None
    # CONFIG_FILENAME = 'test.json'
    cfg = configjson(CONFIG_FILENAME)

    g = cfg(
        z=2,
        az=3123,
        b=121243,
        a=1,
        pin=3,
        hash='asd',
        xuy=16).get()

    print(type(g))  # <class 'dict'>
    print(cfg, '- cfg')

    print(cfg.sorted_by_keys(lambda x: x[-1]), '- sorted by last letter')

    try:
        print(~cfg, '- inverted')
    except RepetitionsError as e:
        print(f'[X] {type(e).__name__}: {e}')

    try:
        print(cfg.sorted_by_keys(), '- sorted by keys')
    except NotSameTypeError as e:
        print(f'[X] {type(e).__name__}: {e}')
    except RepetitionsError as e:
        print(f'[X] {type(e).__name__}: {e}')

    try:
        print(cfg.sorted_by_values(), '- sorted by values')
    except NotSameTypeError as e:
        print(f'[X] {type(e).__name__}: {e}')
    except RepetitionsError as e:
        print(f'[X] {type(e).__name__}: {e}')

    print(cfg.filtered_by_keys(lambda x: x[0] == 'a'))
    print(cfg.filtered_by_values(lambda x: str(x)[0] == '1'))

    print(cfg + ('test+', 1))

    print(cfg & {'z': 2, 'az': 3123, 'a': 1, 'pin': 3, 'new_test': 1245125})

    print(cfg | {'z': 2, 'az': 3123, 'a': 1, 'pin': 3, 'new_test': 1245125})

    cfg += ['+=', 1]
    print(cfg)
