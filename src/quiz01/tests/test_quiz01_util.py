"""_summary_."""

# import pytest
# import src.quiz01_scrapper
from .. import quiz01_util
# from src.quiz01_scrapper import _analyze_feedback_question, main


def test_decorator():
    """_summary_."""

    @quiz01_util.log_method_call
    def hello(who: str):
        retuned_string: str = f'hello {who}'
        print(retuned_string)
        return retuned_string

    # Call the decorated function
    result = hello('m01')

    # Assert that the decorator worked as expected
    assert result == 'hello m01'
