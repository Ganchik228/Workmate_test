# Workmate_test

Для проекта я использовал пакетный менеджер UV, также есть обычный requirements.txt для pip.

Для синхронизации пакетов
```
uv sync
```
{https://github.com/Ganchik228/Workmate_test/blob/main/screens/uv_run.png}
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
Добавить флаги ```--cov``` для проверки покрытия
