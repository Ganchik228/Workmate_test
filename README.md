# Workmate_test

Для проекта я использовал пакетный менеджер UV, также есть обычный requirements.txt для pip.

Для синхронизации пакетов
```
uv sync
```
либо
```
pip install -r requirements.txt
```

Запускать так
```
uv run main.py --files .\test_data\students1.csv .\test_data\students2.csv --report students-performance
```

либо
```
python main.py --files .\test_data\students1.csv .\test_data\students2.csv --report students-performance
```


Для тестов либо
```
uv run pytest
```
```
pytest
```
Добавить флаги ```--cov --cov-report=term-missing``` для проверки покрытия
