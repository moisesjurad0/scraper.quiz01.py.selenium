"""Modulo Util con decorator para logs."""


def log_method_call(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join(
            [f"{key}={repr(value)}" for key, value in kwargs.items()])
        params_str = ', '.join(filter(None, [args_str, kwargs_str]))

        print(f"CALL '{method_name}' --> ({params_str})")

        result = func(*args, **kwargs)

        print(f"END '{method_name}' --> returned {repr(result)}")

        return result

    return wrapper
