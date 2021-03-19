def val_checker(fast_func):
    def _val_cheker(func):
        def try_check(*args):
            if not fast_func(args[0]):
                raise ValueError(f'Wrong val {args[0]}')
            else:
                return func(args[0])
        return try_check
    return _val_cheker


@val_checker(lambda x: x > 0)
def calc_cube (x):
    return x ** 3

print(calc_cube(5))
print(calc_cube(0.5))
print(calc_cube(-5))
