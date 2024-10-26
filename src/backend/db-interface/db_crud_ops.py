from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from db_classes import Associato, Prestazione, Servizio, Transazione
from db_connectors import get_session

# CRUD Ops
def add_entry(entry):
    """Aggiunge un nuovo record alla tabella specificata."""
    session = get_session()
    session.add(entry)
    session.commit()
    return entry

def delete_entry(entry_class, entry_id):
    """Elimina un record dalla tabella specificata dato il suo ID."""
    session = get_session()
    entry = session.get(entry_class, entry_id)
    if entry:
        session.delete(entry)
        session.commit()
        return True
    return False

def modify_entry(entry_class, entry_id, **kwargs):
    """Modifica un record della tabella specificata con i nuovi valori di kwargs."""
    session = get_session()
    entry = session.get(entry_class, entry_id)
    if entry:
        for key, value in kwargs.items():
            setattr(entry, key, value)
        session.commit()
        return entry
    return None


# Tables Ops
def add_associato(nome, cognome, data_nascita, luogo_nascita, email, cellulare, data_associazione, collegamenti):
    associato = Associato(
        nome=nome,
        cognome=cognome,
        data_nascita=data_nascita,
        luogo_nascita=luogo_nascita,
        email=email,
        cellulare=cellulare,
        data_associazione=data_associazione,
        collegamenti=collegamenti
    )
    return add_entry(associato)

def delete_associato(associato_id):
    return delete_entry(Associato, associato_id)

def modify_associato(associato_id, fields):
    return modify_entry(Associato, associato_id, fields)

def add_prestazione(id_servizio, usufruitore, data_prestazione):
    prestazione = Prestazione(
        id_servizio=id_servizio,
        usufruitore=usufruitore,
        data_prestazione=data_prestazione
    )
    return add_entry(prestazione)

def delete_prestazione(prestazione_id):
    return delete_entry(Prestazione, prestazione_id)

def modify_prestazione(prestazione_id, fields):
    return modify_entry(Prestazione, prestazione_id, fields)

def add_servizio(descrizione, costo, personale):
    servizio = Servizio(
        descrizione=descrizione,
        costo=costo,
        personale=personale
    )
    return add_entry(servizio)

def delete_servizio(servizio_id):
    return delete_entry(Servizio, servizio_id)

def modify_servizio(servizio_id, fields):
    return modify_entry(Servizio, servizio_id, fields)

def add_transazione(ammontare, data_transazione, modalita, id_associato, id_prestazione):
    transazione = Transazione(
        ammontare=ammontare,
        data_transazione=data_transazione,
        modalita=modalita,
        id_associato=id_associato,
        id_prestazione=id_prestazione
    )
    return add_entry(transazione)

def delete_transazione(transazione_id):
    return delete_entry(Transazione, transazione_id)

def modify_transazione(transazione_id, fields):
    return modify_entry(Transazione, transazione_id, fields)