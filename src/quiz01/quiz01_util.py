"""Modulo Util con decorator para logs."""
import logging


def log_method_call(func):
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join(
            [f"{key}={repr(value)}" for key, value in kwargs.items()])
        params_str = ', '.join(filter(None, [args_str, kwargs_str]))

        in_str = f"CALL '{method_name}' --> ({params_str})"
        print(in_str)
        logging.info(in_str)

        result = func(*args, **kwargs)

        out_str = f"END '{method_name}' --> returned {repr(result)}"
        print(out_str)
        logging.info(out_str)

        return result

    return wrapper
