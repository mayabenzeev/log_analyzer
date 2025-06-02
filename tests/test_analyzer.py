# test implementation goes here
import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analyzer import analyze_log, main

@pytest.fixture(scope="session", autouse=True)
def logs_file_setup():
    logs_file = "sample.log"  # Path relative to project root
    return logs_file

@pytest.fixture(scope="session", autouse=True)
def empty_logs_file_setup():
    logs_file = "newlog.log"  # Path relative to project root
    return logs_file

def test_command_line_interface(monkeypatch, capsys, logs_file_setup):
    """Test command line interface"""
    monkeypatch.setattr('sys.argv', ['main.py', '--input', logs_file_setup, '--report', 'summary'])  # Use the fixture value
    
    main.main()
    
    captured = capsys.readouterr()
    assert captured.out != ""  # Check that something was printed to stdout


def test_generate_report_summary(capsys, logs_file_setup):
    """Test for generating report summary"""
    anlzr = analyze_log.LogAnalyzer(logs_file_setup, "summary")
    anlzr.generate_report()

    captured = capsys.readouterr()
    assert "Total log entries = 15" in captured.out


def test_generate_report_top_user(capsys, logs_file_setup):
    """Test for generating report top-user (as that user has the most logs)"""
    anlzr = analyze_log.LogAnalyzer(logs_file_setup, "top-user")
    anlzr.generate_report()

    captured = capsys.readouterr()
    assert "Top user = bob" in captured.out


def test_generate_report_common_error(capsys, logs_file_setup):
    """Test for generating report common-error (as that error has the most logs)"""
    anlzr = analyze_log.LogAnalyzer(logs_file_setup, "common-error")
    anlzr.generate_report()

    captured = capsys.readouterr()
    assert "Common error = Invalid password" in captured.out
    assert captured.out != ""  # Check that something was printed to stdout

def test_generate_report_no_logs(capsys, empty_logs_file_setup):
    """Test for generating report common-error (as that error has the most logs)"""
    anlzr = analyze_log.LogAnalyzer(empty_logs_file_setup, "common-error")
    anlzr.generate_report()

    captured = capsys.readouterr()
    assert "No logs found in the file" in captured.out
    assert captured.out != ""  # Check that something was printed to stdout