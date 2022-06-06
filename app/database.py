from sqlalchemy.ext.asyncio import create_async_engine

from conf.settings import settings

kwargs = {}

if "DEBUG" in settings:
    kwargs |= {"echo": settings["DEBUG"]}
if "SQLALCHEMY" in settings and "CONNECT_ARGS" in settings["SQLALCHEMY"]:
    kwargs |= {"connect_args": settings["SQLALCHEMY"]["CONNECT_ARGS"]}

# SQLAlchemy engine instance
# lazy initialization
engine = create_async_engine(
    # dialect+driver://username:password@host:port/database
    settings["SQLALCHEMY"]["DATABASE_URI"],
    **kwargs,
)
