from typing import *


class NotSameTypeError(Exception):
    """NotSameTypeError(dictionary_, message)
Checks dict for different types
Raises manually if dict have different types in values

arg:          type:   default:
:dictionary_  dict
:message      str     None"""
    def __init__(self, dictionary_: dict, message: Optional[str] = None):
        self.dictionary_ = dictionary_
        self.message = message

        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)

    def find_other_type(self) -> tuple:
        dict_values = self.dictionary_.values()
        types = [type(i) for i in dict_values]

        less_common_type = Counter(types).most_common()[-1][0]

        val = list(dict_values)[list(types).index(less_common_type)]

        key = '[NF]'
        for k, v in self.dictionary_.items():
            if v == val:
                key = k
                break

        return less_common_type, key, val

    def __str__(self):
        t, k, v = self.find_other_type()
        if self.message is not None:
            return f'{self.message}, find other type {t} with key <{k}: {v}>'
        else:
            return f'Find other type {t} with key <{k}: {v}>'


class RepetitionsError(Exception):
    """RepetitionsError(dictionary_, message)
Check dict for repetitions
Raises manually if dict has repetitions in invert, by_values methods

arg:          type:   default:
:dictionary_  dict
:message      str     None"""
    def __init__(self, dictionary_: dict, message: Optional[str] = None):
        self.dictionary_ = dictionary_
        self.message = message

        # переопределяется конструктор встроенного класса `Exception()`
        super().__init__(self.message)

    def find_repetitions(self) -> list:

        count_reps = Counter(self.dictionary_.values()).most_common()
        return [f'Value <{i[0]}> repeated {i[1]} times' for i in count_reps if i[1] > 1]

    def __str__(self):
        lst = self.find_repetitions()
        if self.message is not None:
            return f'{self.message}, {". ".join(lst)}'
        else:
            return ". ".join(lst)