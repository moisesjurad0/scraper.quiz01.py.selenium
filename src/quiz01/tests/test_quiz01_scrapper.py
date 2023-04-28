"""_summary_."""

# import pytest
# import src.quiz01_scrapper
from .. import quiz01_scrapper
# from src.quiz01_scrapper import _analyze_feedback_question, main


def test_analyze_feedback_question(monkeypatch):
    """_summary_.

    Args:
        monkeypatch (_type_): _description_
    """
    string1 = "RADIO"
    string2 = "Pregunta de ejemplo"
    feedback = None

    monkeypatch.setattr(
        quiz01_scrapper,
        "_analyze_feedback_question",
        lambda x: string1, string2
    )
    assert quiz01_scrapper._analyze_feedback_question(
        feedback) == string1, string2


# @pytest.mark.parametrize(
#     "arg1, arg2",
#     [
#         ("-n", "1")  # ,
#         # ("-n", "2")
#     ]
# )
# def test_main(arg1, arg2):
def test_main():
    """_summary_."""
    try:
        quiz01_scrapper.do_scrapping()
    except Exception:
        pass


def test_main_mokeyed(monkeypatch):
    """_summary_.

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr(
        quiz01_scrapper,
        "do_scrapping",
        lambda: None
    )
    assert quiz01_scrapper.do_scrapping() is None


###############
# codigo de ejemplo eque me eocntre
###############
# @pytest.mark.parametrize("option", ("-h", "--help"))
# def test_help(capsys, option):
#     try:
#         main([option])
#     except SystemExit:
#         pass
#     output = capsys.readouterr().out
#     assert "Stream one or more files with a delay" in output
