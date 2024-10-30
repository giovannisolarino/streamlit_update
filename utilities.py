import streamlit as st
import io
import base64
from PIL import Image

@st.cache_resource
def logo():
    file = open("./static/logo.png", "rb")
    contents = file.read()
    img_str = base64.b64encode(contents).decode("utf-8")
    buffer = io.BytesIO()
    file.close()
    img_data = base64.b64decode(img_str)
    img = Image.open(io.BytesIO(img_data))
    resized_img = img.resize((400, 120))  # x, y
    resized_img.save(buffer, format="PNG")
    img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")


    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url('data:image/png;base64,{img_b64}');
                background-repeat: no-repeat;
                padding-top: 100px;
                background-position: 5px 50px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def title():
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title></title>
        <style>
            body {
                margin: 0;
                padding: 0;
                text-align: justify;
            }
            .title-container {
                padding: 0px;
            }
            .title {
                text-align:center;
                font-size: 48px;
                color: #333333;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }
            .highlight {
                color: #d62121;
            }
        </style>
    </head>
    <body>
        <div class="title-container">
            <h1 class="title"><span class="highlight">M</span>ethods <span class="highlight">V</span>alidation <span class="highlight">A</span>pp</h1>
        </div>
    </body>
    </html>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def hide():
    hide_streamlit_style = """
           <style>
           #MainMenu {visibility: hidden;}
           footer {visibility: hidden;}
           </style>
           """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)




