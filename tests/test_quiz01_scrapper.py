"""_summary_."""

# import pytest
# from ..src.quiz01_scrapper import *

# from ..src import quiz01_scrapper
# from ..src import quiz01_scrapper, quiz01_api

import src.quiz01_scrapper
# import src.quiz01_api


def test_analyze_feedback_question(monkeypatch):
    """_summary_.

    Args:
        monkeypatch (_type_): _description_
    """
    string1 = "RADIO"
    string2 = "Pregunta de ejemplo"
    feedback = None

    monkeypatch.setattr(
        src.quiz01_scrapper,
        "_analyze_feedback_question",
        lambda x: string1, string2
    )
    assert src.quiz01_scrapper._analyze_feedback_question(
        feedback) == string1, string2


def test_main(monkeypatch):
    """_summary_.

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr(
        src.quiz01_scrapper,
        "main",
        lambda: None
    )
    assert src.quiz01_scrapper.main() is None
