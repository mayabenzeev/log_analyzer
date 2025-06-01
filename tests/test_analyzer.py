# test implementation goes here
import pytest
from analyzer import main, analyzer

@pytest.fixture(scope="session", autouse=True)
def logs_file_setup():
    logs_file = "../sample.log"
    return logs_file

def test_command_line_interface(monkeypatch, capsys):
    """Test command line interface"""
    monkeypatch.setattr('sys.argv', ['main.py', '--input', '../sample.log', '--report', 'summary'])
    
    main.main()
    
    captured = capsys.readouterr()
    assert captured.out != ""  # Check that something was printed to stdout


def test_generate_report_summary(capsys):
    """Test for generating report summary"""
    anlzr = analyzer.LogAnalyzer(str(logs_file_setup), "summary")
    anlzr.generate_summary_report()

    # Should print the summary report to the console
    captured = capsys.readouterr()
    assert "Total log entries = 15" in captured.out



def test_generate_report_top_user(capsys):
    """Test for generating report top-user (as that user has the most logs)"""
    anlzr = analyzer.LogAnalyzer(str(logs_file_setup), "top-user")
    anlzr.generate_top_user_report()

    captured = capsys.readouterr()
    assert "Top user = bob" in captured.out


def test_generate_report_common_error(capsys):
    """Test for generating report common-error (as that error has the most logs)"""
    anlzr = analyzer.LogAnalyzer(str(logs_file_setup), "common-error")
    anlzr.generate_common_error_report()

    captured = capsys.readouterr()
    assert "Common error = Invalid password" in captured.out
    assert captured.out != ""  # Check that something was printed to stdout
