# Анализ логов
cli-приложение для формирования отчетов по логам.
## Добавление новых обработчиков.
Для добавления новых обработчиков нужно создать класс, реализующий интерфейс IReport и три метода: worker, merge_results, make_report.
- worker — собирает нужные данные из файла логов
- merge_results — соединяет данные
- make_report — выводит информацию на основе данных
Добавить новый класс в словарь reports_handler в файле main.py.
```
reports_handler: dict[str, type[IReport]] = {
  "handlers": Handler,
  "time_series": TimeSeries,
}
```
