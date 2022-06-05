# fastapi-starter
This is a fastapi boilerplate template for quick start.

This project is based on SQLAlchemy 1.4+ in order to utilize async connections.

## requirements
* FastAPI
* SQLAlchemy[asyncio]
* aiosqlite
* uvicorn

## `app/conf/secret.json`
`secret.json` file has to be located in `app/conf.`. The following is the sample secret settings:

```json
{
    "DEBUG": true,
    "RELOAD": true,
    "HOST": "127.0.0.1",
    "PORT": 8000,
    "SQLALCHEMY": {
        "DATABASE_URI": "sqlite+aiosqlite:///db.sqlite3",
        "CONNECT_ARGS": {
            "check_same_thread": false
        }
    }
}
```

## Run
```
$ python app/main.py
```

SQLAlchemy 2.0 migration must be considered for consistent development, so you may enable all of SQLAlchemy warings as follows:

```
$ SQLALCHEMY_WARN_20=1 python -W always::DeprecationWarning app/main.py
```
