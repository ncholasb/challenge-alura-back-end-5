from sqlalchemy.sql import text
from .database import engine

with engine.connect() as con:

    statement = text("""
                     INSERT INTO categorias(id, titulo, cor) VALUES(1, 'Livre', 'Gray') ON CONFLICT(id) DO NOTHING;
                     """)

    con.execute(statement)
