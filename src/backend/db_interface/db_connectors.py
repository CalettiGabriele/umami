from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

def get_session():
    """
    Crea una sessione di database utilizzando SQLAlchemy.

    Args:
        database_url (str): URL di connessione al database PostgreSQL.

    Returns:
        Session: Un oggetto sessione per interagire con il database.
    """
    engine = create_engine(os.getenv("DATABASE_URL"))
    Session = sessionmaker(bind=engine)
    return Session()

# Esempio di utilizzo
if __name__ == "__main__":
    session = get_session()
    session.close()
