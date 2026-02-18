import json
from pathlib import Path
from main import bandit_annotations, run_bandit, bandit_run_check, bandit_error


def test_errors():
    results = json.loads(Path("tests/bandit.error.json").read_text())
    errors = [bandit_error(error) for error in results["errors"]]
    assert errors[0]["path"] == "LICENSE"
    # The error message format changed in Python 3.11+
    assert errors[1]["path"] == "tests/py2.py"
    assert errors[1]["start_line"] == 2
    assert errors[1]["end_line"] == 2
    assert errors[1]["annotation_level"] == "failure"
    assert "Missing parentheses in call to 'print'" in errors[1]["message"]


def test_annotations():
    results = json.loads(Path("tests/bandit.json").read_text())
    annotations = bandit_annotations(results)
    assert annotations[0]["path"] == "canary.py"
    assert annotations[0]["start_line"] == 3


def test_run_bandit():
    results = run_bandit(["canary.py"])
    assert "results" in results


def test_run_check():
    results = json.loads(Path("tests/bandit.json").read_text())
    run_check_body = bandit_run_check(results)
    assert run_check_body["conclusion"] == "failure"
