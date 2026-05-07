# ML API для Fashion MNIST

FastAPI + PostgreSQL: обучение, тестирование и предсказание (CSV/изображение). Модель — логистическая регрессия на Fashion MNIST.

## Быстрый старт
```bash
pip install -r requirements.txt
python src/preprocess.py   # распаковка, split
python src/train.py        # обучение + scaler
uvicorn main:app --host 0.0.0.0 --port 8000
```

## База данных (PostgreSQL)
При каждом предсказании запись сохраняется в таблицу `predictions` (features, predicted_class, confidence, created_at).

**Переменные окружения** (можно задать в `.env`):
- `POSTGRESQL_USER` (по умолч. `postgres`)
- `POSTGRESQL_PASSWORD` (по умолч. `admin`)
- `POSTGRESQL_HOST` (по умолч. `localhost`)
- `POSTGRESQL_PORT` (по умолч. `5432`)
- `POSTGRESQL_DB` (по умолч. `mydb`)

Либо задайте полный `DATABASE_URL`.

**Инициализация**:
```python
from src.db.database import init_db
init_db()   # создаёт таблицы
```

## Docker (с PostgreSQL)
```bash
docker-compose up --build
```
Сервис `db` поднимает Postgres, `web` — приложение. Переменные окружения читаются из `.env`.

## Тесты и CI/CD
- Юнит-тесты: `coverage run -m src.unit_tests.test_preprocess`, `test_training`
- Jenkins: клон, сборка, запуск тестов, push в Docker Hub, подпись Cosign.

Конфиг: `config.ini`, логи: `logfile.log`.