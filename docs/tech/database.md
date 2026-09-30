# Схема базы данных

```mermaid
erDiagram
  ORGANIZATION ||--o{ PROJECT : "ведёт"
  ORGANIZATION ||--o{ USER : "включает"
  PROJECT ||--o{ SPRINT : "делится на"
  PROJECT ||--o{ TASK : "содержит"
  SPRINT ||--o{ TASK : "планирует"
  USER ||--o{ TASK : "исполняет"
  TASK ||--o{ COMMIT : "связана с"
  TASK ||--o{ REVIEW : "проходит"
  COMMIT ||--o{ PIPELINE_RUN : "запускает"
  RELEASE ||--|{ TASK : "включает"
  PROJECT ||--o{ RELEASE : "выпускает"
  RELEASE ||--o{ INCIDENT : "может вызвать"
  TASK {
    int id PK
    int project_id FK
    int sprint_id FK
    int assignee_id FK
    string title
    string status
    int estimate_sp
    datetime created_at
  }
  COMMIT {
    string sha PK
    int task_id FK
    datetime committed_at
  }
  PIPELINE_RUN {
    int id PK
    string commit_sha FK
    string result
    int duration_s
  }
  RELEASE {
    int id PK
    int project_id FK
    string version
    datetime deployed_at
  }
```

| Сущность | Описание |
|---|---|
| Организация, Пользователь | компания-клиент и её сотрудники с ролями |
| Проект, Спринт | единица работы команды и её итерации |
| Задача | карточка изменения; статус меняется по событиям |
| Коммит, Ревью | связь задачи с кодом и проверкой кода |
| Запуск пайплайна | результат сборки и автотестов |
| Релиз, Инцидент | выпуск в продуктив и возможные сбои после него |
