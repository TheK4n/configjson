from json import load as json_load, dump as json_dump
from src.exceptions import *
from typing import Optional, Callable, ItemsView, Iterable, Union, Any


class ConfigJson:
    """
    configjson(self, json_filename=None, indent=2, ensure_ascii=False)

    if the variable 'json_filename' is None, then the dictionary is not written to the file,
    but stored in the instance attribute
    """

    def __init__(self, json_filename: Optional[str] = None, *, indent: Optional[int] = 2,
                 ensure_ascii: Optional[bool] = False):

        self.__json_filename = json_filename  # Если self.__json_filename - None, то dict не записывается
        self.__indent = indent  # в файл,а хранится в атрибуте экземпляра класса
        self.__ensure_ascii = ensure_ascii

        self.__dictionary = {}
        self.__save_json()

    def __load_from_file(self):  # вызывается для обновления атрибута __dictionary из json объекта
        """Loads json object to dictionary"""
        if self.__json_filename is None:
            return
        try:
            with open(self.__json_filename, 'r') as file:
                self.__dictionary = json_load(file)
        except FileNotFoundError:
            self.__dictionary = {}

    def __save_json(self):
        """Dumps dictionary to config"""
        if self.__json_filename is None:
            return
        with open(self.__json_filename, 'w') as file:
            json_dump(self.__dictionary, file, indent=self.__indent, ensure_ascii=self.__ensure_ascii)

    def __call__(self, **params):
        """self(key = value, other_key = other_value, ...)
        Manually updates config from key arguments
        """
        self.__dictionary.update(params)
        self.__save_json()
        return self

    def upd(self, dictionary_: dict):
        self.__load_from_file()
        self.__dictionary.update(dictionary_)
        self.__save_json()
        return self

    def set(self, dictionary_: dict):
        self.__load_from_file()
        self.__dictionary = dictionary_
        self.__save_json()
        return self

    def get(self) -> dict:
        self.__load_from_file()
        return self.__dictionary.copy()

    def __str__(self):
        self.__load_from_file()
        return repr(self.__dictionary)

    def __getitem__(self, key: Any) -> Any:
        self.__load_from_file()
        return self.__dictionary[key]

    def __setitem__(self, key: Any, val: Any):
        self.__load_from_file()
        self.__dictionary[key] = val
        self.__save_json()

    def __delitem__(self, key: Any):
        self.__load_from_file()
        del self.__dictionary[key]
        self.__save_json()

    @staticmethod
    def __is_are_repetitions_in_values(dictionary_: dict) -> bool:
        """
        Returns True if repetitions in dict values
        """
        dict_values = list(dictionary_.values())
        while dict_values:
            i = dict_values.pop(0)
            if i in dict_values:
                return True
        return False

    @staticmethod
    def __inverted(dictionary_: dict) -> dict:
        """
        Returns dictionary replaced keys with values and values with keys
        """
        return {v: k for k, v in dictionary_.items()}  # генератор словарей

    def __invert__(self) -> dict:
        """~self
        Returns dictionary replaced keys with values and values with keys
        """
        self.__load_from_file()
        if self.__is_are_repetitions_in_values(self.__dictionary):
            raise RepetitionsError(self.__dictionary, 'Config cannot be inverted')
        return self.__inverted(self.__dictionary)

    def pop(self, key: Any, default: Optional[Any] = None) -> Any:
        """self.pop(self, key, default = None)
        Returns value from dict and deletes key from config
        if KeyError - returns default
        """
        self.__load_from_file()
        if default is not None:
            try:
                res = self.__dictionary.pop(key)
                self.__save_json()
            except KeyError:
                res = default
        else:
            res = self.__dictionary.pop(key)
            self.__save_json()
        return res

    @staticmethod
    def __is_all_keys_same_type(_dictionary: dict) -> bool:
        """__is_all_keys_same_type(_dictionary)
        Returns False if dict keys not same type
        """
        dict_values = list(_dictionary.keys())
        while len(dict_values) > 1:
            zero = dict_values.pop(0)
            for i in dict_values:
                if not isinstance(zero, type(i)):
                    return False
        return True

    @staticmethod
    def __is_all_values_same_type(_dictionary: dict) -> bool:
        """__is_all_values_same_type(_dictionary)
        Returns False if dict values not same type
        """
        dict_values = list(_dictionary.values())
        while len(dict_values) > 1:
            zero = dict_values.pop(0)
            for i in dict_values:
                if not isinstance(zero, type(i)):
                    return False
        return True

    @staticmethod
    def __sorted_dict(dictionary_: dict, key: Optional[Callable] = None, reverse: Optional[bool] = False) -> dict:
        """self.__sorted_dict(dictionary_, key=None, reverse=False)
        Returns sorted dict by keys
        """
        srt = sorted(dictionary_.keys(), key=key, reverse=reverse)
        return {i: dictionary_[i] for i in srt}

    def sorted_by_keys(self, key: Optional[Callable] = None, reverse: Optional[bool] = False) -> dict:
        """self.sorted_by_keys(self, key=None, reverse=False)
        Returns sorted config by keys
        :raises NotSameTypeError: if keys not same type
        """
        self.__load_from_file()
        if not self.__is_all_keys_same_type(self.__dictionary):
            raise NotSameTypeError(self.__dictionary, 'Config cannot be sorted')

        return self.__sorted_dict(self.__dictionary, key=key, reverse=reverse)

    def sort_by_keys(self, key: Optional[Callable] = None, reverse: Optional[bool] = False):
        """self.sort_by_keys(self, key=None, reverse=False)
        Sorts config by keys
        :raises NotSameTypeError: if keys not same type
        """
        if not self.__is_all_keys_same_type(self.__dictionary):
            raise NotSameTypeError(self.__dictionary, 'Config cannot be sorted')

        self.__dictionary = self.sorted_by_keys(key=key, reverse=reverse)
        self.__save_json()
        return self

    def sorted_by_values(self, key: Optional[Callable] = None, reverse: Optional[bool] = False) -> dict:
        """self.sorted_by_values(self, key=None, reverse=False)
        Returns sorted config by values
        :raises NotSameTypeError: if values not same type
        :raises RepetitionsError: if values has repetitions
        """
        self.__load_from_file()
        if not self.__is_all_values_same_type(self.__dictionary):
            raise NotSameTypeError(self.__dictionary, 'Config cannot be sorted')
        if self.__is_are_repetitions_in_values(self.__dictionary):
            raise RepetitionsError(self.__dictionary, 'Config cannot be sorted')

        srt = self.__sorted_dict(self.__inverted(self.__dictionary), key=key, reverse=reverse)
        return self.__inverted(srt)

    def sort_by_values(self, key: Optional[Callable] = None, reverse: Optional[bool] = False):
        """self.sort_by_values(self, key=None, reverse=False)
        Sorts config by values
        :raises NotSameTypeError: if values not same type
        :raises RepetitionsError: if values has repetitions
        """
        if not self.__is_all_values_same_type(self.__dictionary):
            raise NotSameTypeError(self.__dictionary, "Config cannot be sorted")
        if self.__is_are_repetitions_in_values(self.__dictionary):
            raise RepetitionsError(self.__dictionary, 'Config cannot be sorted')

        self.__dictionary = self.sorted_by_values(key=key, reverse=reverse)
        self.__save_json()
        return self

    @staticmethod
    def __filtered_dict(dictionary_: dict, key: Optional[Callable] = None) -> dict:
        """self.__filtered_dict(dictionary_, key=None)
        Returns filtered dict by keys
        """
        filtered = filter(key, dictionary_.keys())
        return {i: dictionary_[i] for i in filtered}

    def filtered_by_keys(self, key: Optional[Callable] = None) -> dict:
        """self.filtered_by_keys(self, key=None, reverse=False)
        Returns filtered config by keys
        """
        self.__load_from_file()
        return self.__filtered_dict(self.__dictionary, key=key)

    def filter_by_keys(self, key: Optional[Callable] = None):
        """self.filter_by_keys(self, key=None)
        Filter config by keys
        """
        self.__dictionary = self.filtered_by_keys(key=key)
        self.__save_json()
        return self

    def filtered_by_values(self, key: Optional[Callable] = None) -> dict:
        """self.filtered_by_values(self, key=None)
        Returns filtered config by values
        :raises RepetitionsError: if values has repetitions
        """
        self.__load_from_file()
        if self.__is_are_repetitions_in_values(self.__dictionary):
            raise RepetitionsError(self.__dictionary, 'Config cannot be filtered')
        filtered = self.__filtered_dict(self.__inverted(self.__dictionary), key=key)
        return self.__inverted(filtered)

    def filter_by_values(self, key: Optional[Callable] = None):
        """self.filter_by_values(self, key=None)
        Filter dict by values
        :raises RepetitionsError: if values has repetitions
        """
        self.__dictionary = self.filtered_by_values(key=key)
        self.__save_json()
        return self

    def __len__(self) -> int:
        """len(self)
        Returns length of dictionary

        """
        self.__load_from_file()
        return len(self.__dictionary)

    def __iter__(self) -> Iterable:
        """for i in self:
        Returns tuple of (key, value) every iteration

        """
        self.__load_from_file()
        return iter(self.__dictionary.items())

    def __contains__(self, item: Any) -> bool:
        """if item in self:
        Returns True if config contains key
        """
        if item in self.__dictionary.keys():
            return True
        else:
            return False

    def items(self) -> ItemsView:
        """self.items()
        Returns list of tuples with (key, value), ex:
        [(key1, value1), (key2, value2)]
        """
        return self.__dictionary.items()

    def __add__(self, other: Union[tuple[Any, Any], list[Any, Any]]) -> dict:
        """self + tuple(key, value)
        Returns updated dict with tuple(key, value)"""
        self.__load_from_file()
        new_dict = self.__dictionary.copy()
        new_dict.update({other[0]: other[1]})
        return new_dict

    def __iadd__(self, other: Union[tuple[Any, Any], list[Any, Any]]):
        """self += tuple(key, value)
        Update config with tuple(key, value)"""
        self.__load_from_file()
        self.__dictionary.update({other[0]: other[1]})
        self.__save_json()
        return self

    def __and__(self, other: dict) -> dict:
        """self & dict
        Returns dict with values in self.__dictionary and in new dict"""
        self.__load_from_file()
        return {i: self.__dictionary[i] for i in other if i in self.__dictionary}

    def __or__(self, other: dict) -> dict:
        """self | dict
        Returns updated dict"""
        self.__load_from_file()
        new_dict = self.__dictionary.copy()
        new_dict.update(other)
        return new_dict
