from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
    """
    Crea una sessione di database utilizzando SQLAlchemy.

    Args:
        database_url (str): URL di connessione al database PostgreSQL.

    Returns:
        Session: Un oggetto sessione per interagire con il database.
    """
    DATABASE_URL = "postgresql+psycopg2://postgres:kety126@localhost:5432/gestionale"
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

# Esempio di utilizzo
if __name__ == "__main__":
    session = get_session()
    session.close()
