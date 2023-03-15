import streamlit as st
import pyshorteners
shorter = pyshorteners.Shortener()


st.title("Acortador de URL")
form=st.form("URL",clear_on_submit=True)
url=form.text_input("Colocar la URL para acortar:")
button=form.form_submit_button("Acortar")

with st.sidebar:
    st.write("Herramienta para cortar o expandir un link usando tinyurl")

if button: #funcionar solo cuando el botton es presionado
    try:
        url_shorter=shorter.tinyurl.short(url)
        st.success("El link acortado es: "+ url_shorter)
    except:
        st.error("Algo salió mal :(")

form_expand=st.form("URL2", clear_on_submit=True)
url_new=form.text_input("Colocar la URL acortada: ")
button_expand=form.form_submit_button("Expandir")
if button_expand:
    try:
        url_expand=shorter.tinyurl.expand(url_new)
        st.success(" El link acortado es: "+ url_expand)
    except:
        st.error("Algo salió mal :(")
    
    