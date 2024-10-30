import streamlit as st
from crud_gui import crud_gui_main
from table_gui import table_gui_main
from dashboard_gui import associati_paganti_tile, associati_per_età_tile


st.title("UMAMI")
tab_dashboard, tab_tabelle, tab_operazioni, tab_chat = st.tabs(["Dashboard", "Tabelle", "Operazioni", "Chat"])

with st.sidebar:
    operation = st.selectbox(
        "Seleziona un Operatore",
        ("Visualizza", "Aggiungi", "Modifica", "Elimina"),
        key="crud_ops"
    )
    table = st.selectbox(
        "Seleziona una Tabella",
        ("Associato", "Prestazione", "Transazione", "Servizio"),
        key="table_ops"
    )

with tab_dashboard:
    st.header("Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        associati_paganti_tile()
    with col2:
        associati_paganti_tile()
    with col3:
        associati_paganti_tile()
    associati_per_età_tile()

with tab_tabelle:
    st.header("Tabelle")
    table_gui_main(table)

with tab_operazioni:
    st.header("Operazioni")
    crud_gui_main(table, operation)

with tab_chat:
    st.header("Chat")