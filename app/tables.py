import sqlalchemy

metadata = sqlalchemy.MetaData()

todos = sqlalchemy.Table(
    "todos",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer(),
        primary_key=True,
        index=True,
        autoincrement=True,
    ),
    sqlalchemy.Column("title", sqlalchemy.String()),
    sqlalchemy.Column("description", sqlalchemy.String()),
    sqlalchemy.Column("priority", sqlalchemy.Integer()),
    sqlalchemy.Column("complete", sqlalchemy.Boolean(), default=False),
)

all = [
    todos,
]
