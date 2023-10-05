"""Modulo Util con decorator para logs."""
from functools import wraps
import logging
import os
import time


def log_method_call_no_params(func):
    """Custom logging decorator to mark begin and end timestamps.

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
    """Custom logging decorator to mark begin and end timestamps.

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


def timely(func):
    """_summary_.

    Args:
        func (_type_): _description_

    Returns:
        _type_: _description_
    """
    func_name = func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):

        logging.info(f"***** Start:{func_name} *****")

        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start

        logging.info(f"***** End:{func_name} ***** "
                     f"| Elapsed Time:{round(duration, 2)}")

        return result

    return wrapper


def getLog(logger_name: str) -> logging.Logger:
    """_summary_.

    Args:
        logger_name (str): _description_
    """
    # https://docs.python.org/3/howto/logging.html

    # create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    # formatter = logging.Formatter(
    #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(levelname)s|%(name)s|%(asctime)s|'
                                  '%(filename)s:%(lineno)d|%(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger


def set_default_logger():

    DEFAULT_LOG_LEVEL = logging.INFO

    if "LOG_LEVEL" in os.environ:
        # For Lambda
        log_level = logging.INFO  # os.environ["LOG_LEVEL"]
    else:
        log_level = DEFAULT_LOG_LEVEL  # Set default log level for local

    root = logging.getLogger()
    if len(logging.getLogger().handlers) > 0:
        # For Lambda
        for handler in root.handlers:
            root.removeHandler(handler)
            logging.basicConfig(
                level=log_level,
                format='[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(module)s] [%(funcName)s] [L%(lineno)d] [P%(process)d] [T%(thread)d] %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')
    else:
        # For Local
        l_name = os.getcwd() + '/' + 'count_mac_module.log'
        logging.basicConfig(
            filename=l_name,
            level=log_level,
            format='[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(module)s] [%(funcName)s] [L%(lineno)d] [P%(process)d] [T%(thread)d] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger(__name__)
    logger.debug(
        f"************* logging set for Lambda {os.getenv('AWS_LAMBDA_FUNCTION_NAME') } *************")
