import streamlit as st
from utilities import logo, title, hide
from streamlit_space import space
from PIL import Image

st.set_page_config(page_title = "MVA", layout='wide',page_icon=':scientist:')
logo()
hide()

image = Image.open('./static/name.png')
left, center, right = st.columns([1,2,0.9])
with center:
    st.image(image, use_column_width='always')
    title()

    space(lines=5)
    st.markdown('### <div style="text-align: center"> MVA is under major revisions. </br>A new updated version will be launched soon! </div>', unsafe_allow_html=True)
    st.markdown('### <div style="text-align: center"> If you need to use our app, please contact us. </div>', unsafe_allow_html=True)
    st.markdown('#### <div style="text-align: center"> Giovanni Solarino <a href="mailto:giovanni.solarino@edu.unito.it">giovanni.solarino@edu.unito.it</a> </div>', unsafe_allow_html=True)
    st.markdown('#### <div style="text-align: center"> Eugenio Alladio <a href="mailto:eugenio.alladio@unito.it">eugenio.alladio@unito.it</a> </div>', unsafe_allow_html=True)
    st.markdown('#### <div style="text-align: center"> Marco Vincenti <a href="mailtomarco.vincenti@unito.it:">marco.vincenti@unito.it</a> </div>', unsafe_allow_html=True)
    
