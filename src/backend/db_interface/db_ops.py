from sqlalchemy import create_engine, func, distinct, and_
from sqlalchemy.orm import sessionmaker
from db_classes import Associato, Prestazione, Servizio, Transazione
from db_connectors import get_session
from datetime import date


def get_all_associati():
    """Restituisce tutti gli associati dal database."""
    session = get_session()
    associati = session.query(Associato).all()
    return associati

def get_associati_con_debito():
    """Restituisce tutti gli associati con debito e l'ammontare."""
    session = get_session()
    debitori = session.query(
        Associato.nome,
        Associato.cognome,
        func.coalesce(func.sum(Servizio.costo), 0).label("totale_servizi"),
        func.coalesce(func.sum(Transazione.ammontare), 0).label("totale_pagamenti"),
        (func.coalesce(func.sum(Servizio.costo), 0) - func.coalesce(func.sum(Transazione.ammontare), 0)).label("debito")
    ).outerjoin(Prestazione, Associato.id == Prestazione.usufruitore) \
     .outerjoin(Servizio, Prestazione.id_servizio == Servizio.id) \
     .outerjoin(Transazione, Prestazione.id == Transazione.id_prestazione) \
     .group_by(Associato.id) \
     .having((func.coalesce(func.sum(Servizio.costo), 0) - func.coalesce(func.sum(Transazione.ammontare), 0)) > 0) \
     .all()
    
    return debitori

def get_debito_associato(nome, cognome):
    """Calcola il debito di un associato specifico."""
    session = get_session()
    debito = session.query(
        Associato.nome,
        Associato.cognome,
        func.coalesce(func.sum(Servizio.costo), 0).label("totale_servizi"),
        func.coalesce(func.sum(Transazione.ammontare), 0).label("totale_pagamenti"),
        (func.coalesce(func.sum(Servizio.costo), 0) - func.coalesce(func.sum(Transazione.ammontare), 0)).label("debito")
    ).outerjoin(Prestazione, Associato.id == Prestazione.usufruitore) \
     .outerjoin(Servizio, Prestazione.id_servizio == Servizio.id) \
     .outerjoin(Transazione, Prestazione.id == Transazione.id_prestazione) \
     .filter(Associato.nome == nome, Associato.cognome == cognome) \
     .group_by(Associato.id) \
     .first()
     
    return debito

def get_numero_associati():
    """Calcola e restituisce il numero di associati presenti nel database."""
    session = get_session()
    numero_associati = session.query(func.count(Associato.id)).scalar()
    return numero_associati

def get_numero_associati_debito():
    """Calcola e restituisce il numero di associati con debiti non saldati."""
    session = get_session()
    associati_con_debiti = (
        session.query(Associato.id)
        .join(Prestazione, Prestazione.usufruitore == Associato.id)
        .outerjoin(Transazione, and_(
            Transazione.id_associato == Associato.id,
            Transazione.id_prestazione == Prestazione.id
        ))
        .filter(Transazione.id == None)
        .distinct()
        .count()
    )
    return associati_con_debiti

def associati_per_eta():
    """Restituisce gli associati suddivisi per fasce di età."""
    session = get_session()
    oggi = date.today()
    
    fasce_eta = {
        'minori di 14': [],
        '14-18': [],
        '18-30': [],
        '30-60': [],
        'maggiori di 60': []
    }
    
    associati = session.query(Associato).all()
    for associato in associati:
        eta = oggi.year - associato.data_nascita.year - ((oggi.month, oggi.day) < (associato.data_nascita.month, associato.data_nascita.day))
        if eta < 14:
            fasce_eta['minori di 14'].append(associato)
        elif 14 <= eta < 18:
            fasce_eta['14-18'].append(associato)
        elif 18 <= eta < 30:
            fasce_eta['18-30'].append(associato)
        elif 30 <= eta < 60:
            fasce_eta['30-60'].append(associato)
        else:
            fasce_eta['maggiori di 60'].append(associato)
    
    return fasce_eta


if __name__ == "__main__":
    for associato in get_all_associati():
        print(f"ID: {associato.id}, Nome: {associato.nome}, Cognome: {associato.cognome}, "
                  f"Data di Nascita: {associato.data_nascita}, Luogo di Nascita: {associato.luogo_nascita}, "
                  f"Email: {associato.email}, Cellulare: {associato.cellulare}, "
                  f"Data di Associazione: {associato.data_associazione}, Collegamenti: {associato.collegamenti}")