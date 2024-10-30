import streamlit as st
import plotly.express as px

import sys
import os
sys.path.append(os.path.abspath("../backend/db_interface"))

from db_ops import get_numero_associati, get_numero_associati_debito, associati_per_eta


def associati_paganti_tile():
    associati_totali = get_numero_associati()
    associati_paganti = associati_totali-get_numero_associati_debito()
    percentuale_paganti = (associati_paganti / associati_totali) * 100
    st.metric(label="Associati Paganti", value=f"{associati_paganti} / {associati_totali}", delta=f"{percentuale_paganti:.1f}%")

def associati_per_età_tile():
    dati = associati_per_eta()
    etichette = list(dati.keys())
    valori = [len(valore) for valore in dati.values()]
    fig = px.bar(x=etichette, y=valori, labels={'x': '', 'y': ''}, title="Associati per fascia di età")
    st.plotly_chart(fig)

