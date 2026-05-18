from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# crio o engine, ligacao fisica á base de dados
engine = create_engine(
    settings.database_url,
    echo=True,
    future=True
)

# cria sessionlocal
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """
    dependencia da FastAPI - fornece uma sessao de base de dados

    cada endpoint que precisar de acesso á DB pode usar:
        db: Session = Depends(get_db)
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
