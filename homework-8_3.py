from functools import wraps

def type_logger(func):

    @wraps(func)
    def typer(*args):
        print(f'Имя функции внутри декоратора: {func.__name__}')
        print(f'Тип аргументов: {[f"{i}: {type(i)}" for i in args]}')
        print(f'Тип значения: {type(func(*args))}')
        return func(*args)
    return typer

@ type_logger
def empty_func(*args):
    return len(args)

print(f'Работа декоратора замаскирована: {empty_func}')
print(f'Результат работы функции с 2 аргументами: {empty_func(5, 6)}')
