# JSON Config Parser
* [Описание библиотеки](#chapter-0)
* [Примеры](#chapter-1)
* [Документация](#chapter-2)

<a id="chapter-0"></a>
## Описание библиотеки
Класс для работы с json объектами\
Основанный на словаре

<a id="chapter-1"></a>
## Примеры
**cfg = ConfigJson(<_CONFIG_FILENAME_>)** - Определение экземпляра класса\
Если _CONFIG_FILENAME_ - None, то json объект не создается, а хранится в атрибуте класса

- **cfg(key='value')** - Создание словаря
- **cfg['key']** - Обращение к словарю по ключу
- **help(cfg)** - Помощь по классу

```python
from configjson import ConfigJson
cfg = ConfigJson()
cfg(val1=1, val2=2, val3=3)
print(cfg['val1'])  # 1
```

<a id="chapter-2"></a>
## Документация
| Метод                                          | Возвращаемый тип   | Действие                 
| :-------------:                                | :----------------:  |:------------
| `cfg(key=value...)`                            | self               | Создает словарь             
| `cfg.upd(dict)`                                | self               | **Обновляет** словарь новым словарем   
| `cfg.set(dict)`                                | self               | Создает словарь             
| `cfg.get()`                                    | dict               | Возвращает словарь
| `print(cfg)`                                   | str                | Выводит строковое представление словаря
| `cfg[key]`                                     | Any                | Возвращает значению по ключу
| `cfg[key] = value`                             | None               | Устанавливает значение по ключу
| `del cfg[key]`                                 | None               | Удаляет ключ в словаре
| `~cfg`                                         | dict               | Меняет местами ключи и значения. Бросает _RepetitionsError_, если в ключах есть повторения
| `len(cfg)`                                     | int                | Возвращает длину словаря
| `len(cfg)`                                     | int                | Возвращает длину словаря
| `cfg.pop(key, default=None)`                   | Any                | Возвращает и удаляет значение по ключу, если ключа нет в словаре возвращает _default_, если _default_ None, бросает _KeyError_
| `cfg.sorted_by_keys(key=func, reverse=bool)`   | dict               | Возвращает отсортированный словарь по **ключам**, _key_ - функция сортировки, _reverse_ - булево значение развернутости. Бросает _NotSameTypeError_ если ключи разного типа
| `cfg.sorted_by_values(key=func, reverse=bool)` | dict               | Возвращает отсортированный словарь по **значениям**, _key_ - функция сортировки, _reverse_ - булево значение развернутости. Бросает _NotSameTypeError_ если значения разного типа, Бросает _RepetitionsError_, если в значениях есть повторения
| `cfg.filtered_by_keys(key=func)`               | dict               | Возвращает фильтрованный словарь по **ключам**, _key_ - функция сортировки
| `cfg.filtered_by_values(key=func)`             | dict               | Возвращает фильтрованный словарь по **значениям**, _key_ - функция сортировки. Бросает _RepetitionsError_, если в ключах есть повторения

<h1 align="center"><a href="#top">▲</a></h1>
