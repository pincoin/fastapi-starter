from sqlalchemy.ext.asyncio import create_async_engine

from conf.settings import settings

# SQLAlchemy engine instance
# lazy initialization
engine = create_async_engine(
    # dialect+driver://username:password@host:port/database
    settings["SQLALCHEMY"]["DATABASE_URI"],
    echo=settings["DEBUG"],  # for debugging log
    connect_args=settings["SQLALCHEMY"]["CONNECT_ARGS"],
)
