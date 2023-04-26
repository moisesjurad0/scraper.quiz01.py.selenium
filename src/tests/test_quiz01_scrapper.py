"""_summary_."""

# import pytest
# import src.quiz01_scrapper
from src import quiz01_scrapper
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
#     """_summary_.

#     Args:
#         arg1 (_type_): _description_
#         arg2 (_type_): _description_
#     """
#     try:
#         src.quiz01_scrapper.main([arg1, arg2])
#     except SystemExit:
#         pass


def test_main2(monkeypatch):
    """_summary_.

    Args:
        monkeypatch (_type_): _description_
    """
    monkeypatch.setattr(
        quiz01_scrapper,
        "main",
        lambda: None
    )
    assert quiz01_scrapper.main() is None


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
