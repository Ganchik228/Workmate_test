import pytest
import os
from main import App, main

@pytest.fixture
def test_data(tmp_path):
    file1 = tmp_path / "test1.csv"
    file2 = tmp_path / "test2.csv"
    file1.write_text(
                    "student_name,subject,teacher_name,date,grade\n"
                    "Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5\n"
                    "Титов Владислав,География,Орлов Сергей,2023-10-12,4\n"
                    "Семенова Елена,Русский язык,Ковалева Анна,2023-10-10,2\n"
                    "Титов Владислав,История,Орлов Сергей,2023-10-12,5",
                    encoding='utf-8')
    file2.write_text(
                    "student_name,subject,teacher_name,date,grade\n"
                    "Иванов Алексей,Математика,Петрова Ольга,2023-09-10,5\n"
                    "Петрова Мария,Физика,Сидоров Иван,2023-09-12,4\n"
                    "Иванов Алексей,Английский язык,Петрова Ольга,2023-09-10,3\n"
                    "Петрова Мария,Математика,Сидоров Иван,2023-09-12,5",
                    encoding='utf-8')
    return [str(file1), str(file2)]

@pytest.fixture
def empty_data(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text("student_name,subject,teacher_name,date,grade\n", encoding='utf-8')
    return [str(file)]

def test_check_csv():
    assert App.check_csv("data.csv") == "data.csv"

def test_check_csv_invalid():
    with pytest.raises(Exception):
        App.check_csv("data.txt")

def test_read_files(test_data):
    app = App(test_data)
    rows = app.read_files()
    assert len(rows) == 8
    print(rows[0]['student_name'].strip())
    expected = [
        {'student_name': 'Семенова Елена', 'subject': 'Английский язык', 'teacher_name': 'Ковалева Анна', 'date': '2023-10-10', 'grade': '5'},
        {'student_name': 'Титов Владислав', 'subject': 'География', 'teacher_name': 'Орлов Сергей', 'date': '2023-10-12', 'grade': '4'},
        {'student_name': 'Семенова Елена', 'subject': 'Русский язык', 'teacher_name': 'Ковалева Анна', 'date': '2023-10-10', 'grade': '2'},
        {'student_name': 'Титов Владислав', 'subject': 'История', 'teacher_name': 'Орлов Сергей', 'date': '2023-10-12', 'grade': '5'},
        {'student_name': 'Иванов Алексей', 'subject': 'Математика', 'teacher_name': 'Петрова Ольга', 'date': '2023-09-10', 'grade': '5'},
        {'student_name': 'Петрова Мария', 'subject': 'Физика', 'teacher_name': 'Сидоров Иван', 'date': '2023-09-12', 'grade': '4'},
        {'student_name': 'Иванов Алексей', 'subject': 'Английский язык', 'teacher_name': 'Петрова Ольга', 'date': '2023-09-10', 'grade': '3'},
        {'student_name': 'Петрова Мария', 'subject': 'Математика', 'teacher_name': 'Сидоров Иван', 'date': '2023-09-12', 'grade': '5'},
    ]
    for actual, exp in zip(rows, expected):
        assert {key: value.strip() for key, value in actual.items()} == exp

def test_students_performance(test_data):
    app = App(test_data)
    performance = app.students_performance()
    expected_performance = [
        {'student_name': 'Титов Владислав', 'grade': 4.5},
        {'student_name': 'Петрова Мария', 'grade': 4.5},
        {'student_name': 'Иванов Алексей', 'grade': 4.0},
        {'student_name': 'Семенова Елена', 'grade': 3.5},
    ]
    actual = sorted([{ 'student_name': item['student_name'], 'grade': item['grade']} for item in performance], 
                    key=lambda x: x['grade'], reverse=True)
    assert actual == expected_performance

def test_empty_file(empty_data):
    app = App(empty_data)
    performance = app.read_files()
    assert performance == []

def test_main_no_files(capsys):
    with pytest.raises(SystemExit):
        main(['--report', 'students-performance'])
    captured = capsys.readouterr()
    assert "usage:" in captured.err

def test_main_no_report(capsys):
    with pytest.raises(SystemExit):
        main(['--files', 'data.csv'])
    captured = capsys.readouterr()
    assert "usage:" in captured.err
