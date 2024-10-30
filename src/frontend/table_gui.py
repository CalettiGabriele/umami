import streamlit as st
from datetime import date, timedelta
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath("../backend/db_interface"))

from utils import class_to_dict
from db_crud_ops import read_table
from db_classes import Associato, Prestazione, Servizio, Transazione


str_to_class = {
    "Associato":Associato,
    "Prestazione":Prestazione,
    "Transazione":Transazione,
    "Servizio":Servizio,
}

def table_gui_main(table):

    results, has_next = read_table(str_to_class[table])
    record_df = pd.DataFrame([class_to_dict(r) for r in results])
    st.dataframe(record_df)