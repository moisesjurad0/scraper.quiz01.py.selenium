"""Modulo Util con decorator para logs."""
import logging
import time


def log_method_call_no_params(func):
    """Custom logger decorator to mark begin and end timestamps.

    Args:
        func (_type_): Function to be logged
    """
    def wrapper(*args, **kwargs):
        method_name = func.__name__

        in_str = f"CALL '{method_name}' --> NO PRINTING PARAMS"
        print(in_str)
        logging.info(in_str)

        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        # ms_elapsed = (end_time - start_time) * 1000
        ms_ns_elapsed = (end_time - start_time)
        microseconds = ms_ns_elapsed / 1e3
        milliseconds = microseconds / 1e3
        seconds = milliseconds / 1e3

        # out_str = f"END '{method_name}' in {ms_elapsed:.2f} ms --> NO PRINTING PARAMS "
        out_str = f"END '{method_name}' in {seconds:.6f} s --> NO PRINTING PARAMS "
        print(out_str)
        logging.info(out_str)

        return result

    return wrapper


def log_method_call(func):
    """Custom logger decorator to mark begin and end timestamps.

    Args:
        func (_type_): Function to be logged
    """
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join(
            [f"{key}={repr(value)}" for key, value in kwargs.items()])
        params_str = ', '.join(filter(None, [args_str, kwargs_str]))

        in_str = f"CALL '{method_name}' --> ({params_str})"
        print(in_str)
        logging.info(in_str)

        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        # ms_elapsed = (end_time - start_time) * 1000
        ms_ns_elapsed = (end_time - start_time)
        microseconds = ms_ns_elapsed / 1e3
        milliseconds = microseconds / 1e3
        seconds = milliseconds / 1e3

        # out_str = f"END '{method_name}' in {ms_elapsed:.2f} ms --> {repr(result)} "
        out_str = f"END '{method_name}' in {seconds:.6f} s --> {repr(result)} "
        print(out_str)
        logging.info(out_str)

        return result

    return wrapper
