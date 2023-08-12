import streamlit as st
import cohere
import os


co = cohere.Client(st.secrets("COHERE_API_KEY"))



st.title("WasteX Chat")
with st.expander("ℹ️ Disclaimer"):
    # TODO: Add disclaimer
    st.caption(
        ""
    )

