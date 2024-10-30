import streamlit as st
from datetime import date, timedelta
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath("../backend/db_interface"))

from utils import class_to_dict
from db_crud_ops import (
    add_associato, delete_associato, modify_associato, read_associato,
    add_prestazione, delete_prestazione, modify_prestazione, read_prestazione,
    add_servizio, delete_servizio, modify_servizio, read_servizio,
    add_transazione, delete_transazione, modify_transazione, read_transazione,
)

# Funzione per la UI per ciascun operatore
def associato_ui(operation):
    if operation == "Visualizza":
        st.subheader("Visualizza un record")
        associato_id = st.number_input("ID Associato", min_value=1)
        if st.button("Visualizza Associato"):
            record = read_associato(associato_id)
            record_df = pd.DataFrame([class_to_dict(record)])
            st.table(record_df.transpose())

    elif operation == "Aggiungi":
        st.subheader("Aggiungi un nuovo associato")
        nome = st.text_input("Nome")
        cognome = st.text_input("Cognome")
        data_nascita = st.date_input("Seleziona la data di nascita", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        luogo_nascita = st.text_input("Luogo di nascita")
        email = st.text_input("Email")
        cellulare = st.text_input("Cellulare")
        data_associazione = st.date_input("Seleziona una data", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        collegamenti = st.text_area("Collegamenti (JSON)")
        if st.button("Aggiungi Associato"):
            associato = add_associato(nome, cognome, data_nascita, luogo_nascita, email, cellulare, data_associazione, collegamenti)
            st.success(f"Associato aggiunto: {associato}")

    elif operation == "Modifica":
        st.subheader("Modifica un associato")
        associato_id = st.number_input("ID Associato", min_value=1)
        nome = st.text_input("Nome")
        cognome = st.text_input("Cognome")
        data_nascita = st.date_input("Seleziona la data di nascita", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        luogo_nascita = st.text_input("Luogo di nascita")
        email = st.text_input("Email")
        cellulare = st.text_input("Cellulare")
        data_associazione = st.date_input("Seleziona una data", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        collegamenti = st.text_area("Collegamenti (JSON)")
        if st.button("Modifica Associato"):
            kwargs = {
                "nome": nome, "cognome": cognome, "data_nascita": data_nascita,
                "luogo_nascita": luogo_nascita, "email": email, "cellulare": cellulare,
                "data_associazione": data_associazione, "collegamenti": collegamenti
            }
            associato = modify_associato(associato_id, **{k: v for k, v in kwargs.items() if v})
            st.success(f"Associato modificato: {associato}")

    elif operation == "Elimina":
        st.subheader("Elimina un associato")
        associato_id = st.number_input("ID Associato", min_value=1)
        if st.button("Elimina Associato"):
            if delete_associato(associato_id):
                st.success(f"Associato con ID {associato_id} eliminato.")
            else:
                st.error("Errore nell'eliminazione.")

def prestazione_ui(operation):
    if operation == "Visualizza":
        st.subheader("Visualizza un record")
        prestazione_id = st.number_input("ID prestazione", min_value=1)
        if st.button("Visualizza"):
            record = read_prestazione(prestazione_id)
            record_df = pd.DataFrame([class_to_dict(record)])
            st.table(record_df.transpose())

    elif operation == "Aggiungi":
        st.subheader("Aggiungi una prestazione")
        id_servizio = st.number_input("ID Servizio", min_value=1)
        usufruitore = st.number_input("ID Usufruitore", min_value=1)
        data_prestazione = st.date_input("Seleziona una data", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        if st.button("Aggiungi Prestazione"):
            prestazione = add_prestazione(id_servizio, usufruitore, data_prestazione)
            st.success(f"Prestazione aggiunta: {prestazione}")

    elif operation == "Modifica":
        st.subheader("Modifica una prestazione")
        prestazione_id = st.number_input("ID Prestazione", min_value=1)
        id_servizio = st.number_input("ID Servizio", min_value=1)
        usufruitore = st.number_input("ID Usufruitore", min_value=1)
        data_prestazione = st.date_input("Seleziona una data", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        if st.button("Modifica Prestazione"):
            kwargs = {"id_servizio": id_servizio, "usufruitore": usufruitore, "data_prestazione": data_prestazione}
            prestazione = modify_prestazione(prestazione_id, **{k: v for k, v in kwargs.items() if v})
            st.success(f"Prestazione modificata: {prestazione}")

    elif operation == "Elimina":
        st.subheader("Elimina una prestazione")
        prestazione_id = st.number_input("ID Prestazione", min_value=1)
        if st.button("Elimina Prestazione"):
            if delete_prestazione(prestazione_id):
                st.success(f"Prestazione con ID {prestazione_id} eliminata.")
            else:
                st.error("Errore nell'eliminazione.")

def servizio_ui(operation):
    if operation == "Visualizza":
        st.subheader("Visualizza un record")
        servizio_id = st.number_input("ID servizio", min_value=1)
        if st.button("Visualizza"):
            record = read_servizio(servizio_id)
            record_df = pd.DataFrame([class_to_dict(record)])
            st.table(record_df.transpose())

    elif operation == "Aggiungi":
        st.subheader("Aggiungi un servizio")
        descrizione = st.text_input("Descrizione Servizio")
        costo = st.number_input("Costo", min_value=0.0, format="%.2f")
        personale = st.checkbox("Servizio personale")
        if st.button("Aggiungi Servizio"):
            servizio = add_servizio(descrizione, costo, personale)
            st.success(f"Servizio aggiunto: {servizio}")

    elif operation == "Modifica":
        st.subheader("Modifica un servizio")
        servizio_id = st.number_input("ID Servizio", min_value=1)
        descrizione = st.text_input("Descrizione Servizio")
        costo = st.number_input("Costo", min_value=0.0, format="%.2f")
        personale = st.checkbox("Servizio personale")
        if st.button("Modifica Servizio"):
            kwargs = {"descrizione": descrizione, "costo": costo, "personale": personale}
            servizio = modify_servizio(servizio_id, **{k: v for k, v in kwargs.items() if v})
            st.success(f"Servizio modificato: {servizio}")

    elif operation == "Elimina":
        st.subheader("Elimina un servizio")
        servizio_id = st.number_input("ID Servizio", min_value=1)
        if st.button("Elimina Servizio"):
            if delete_servizio(servizio_id):
                st.success(f"Servizio con ID {servizio_id} eliminato.")
            else:
                st.error("Errore nell'eliminazione.")

def transazione_ui(operation):  
    if operation == "Visualizza":
        st.subheader("Visualizza un record")
        transazione_id = st.number_input("ID transazione", min_value=1)
        if st.button("Visualizza"):
            record = read_transazione(transazione_id)
            record_df = pd.DataFrame([class_to_dict(record)])
            st.table(record_df.transpose())

    elif operation == "Aggiungi":
        st.subheader("Aggiungi una transazione")
        ammontare = st.number_input("Ammontare", min_value=0.0, format="%.2f")
        data_transazione = st.date_input("Seleziona una data", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        modalita = st.selectbox("Modalità", ["pos", "bonifico", "contante", "assegno"])
        id_associato = st.number_input("ID Associato", min_value=1)
        id_prestazione = st.number_input("ID Prestazione", min_value=1)
        if st.button("Aggiungi Transazione"):
            transazione = add_transazione(ammontare, data_transazione, modalita, id_associato, id_prestazione)
            st.success(f"Transazione aggiunta: {transazione}")

    elif operation == "Modifica":
        st.subheader("Modifica una transazione")
        transazione_id = st.number_input("ID Transazione", min_value=1)
        ammontare = st.number_input("Ammontare", min_value=0.0, format="%.2f")
        data_transazione = st.date_input("Seleziona una data", min_value=date.today() - timedelta(days=365*100), max_value=date.today())
        modalita = st.selectbox("Modalità", ["pos", "bonifico", "contante", "assegno"])
        id_associato = st.number_input("ID Associato", min_value=1)
        id_prestazione = st.number_input("ID Prestazione", min_value=1)
        if st.button("Modifica Transazione"):
            kwargs = {"ammontare": ammontare, "data_transazione": data_transazione, "modalita": modalita, "id_associato": id_associato, "id_prestazione": id_prestazione}
            transazione = modify_transazione(transazione_id, **{k: v for k, v in kwargs.items() if v})
            st.success(f"Transazione modificata: {transazione}")

    elif operation == "Elimina":
        st.subheader("Elimina una transazione")
        transazione_id = st.number_input("ID Transazione", min_value=1)
        if st.button("Elimina Transazione"):
            if delete_transazione(transazione_id):
                st.success(f"Transazione con ID {transazione_id} eliminata.")
            else:
                st.error("Errore nell'eliminazione.")

def crud_gui_main(table, operation):
    if table == "Associato":
        associato_ui(operation)
    elif table == "Prestazione":
        prestazione_ui(operation)
    elif table == "Servizio":
        servizio_ui(operation)
    elif table == "Transazione":
        transazione_ui(operation)