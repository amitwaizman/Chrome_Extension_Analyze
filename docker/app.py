import streamlit as st

import joblib
import time
from PIL import Image, ImageSequence
import base64
import extracrt_crx as extracrt
import feature_extraction as featu
import nltk
from gensim.models import Word2Vec
import os


def save_crx_file(file, file_name):
    with open(file_name, "wb") as crx_file:
        crx_file.write(file.getbuffer())

def word_2_vec(w):
    try_model = open("model/Word2Vec.pkl","rb")
    try_clf = joblib.load(try_model)
    tokenized_text = [nltk.word_tokenize(sentence.lower()) for sentence in [w]]
    for x in tokenized_text:
        return try_clf.wv[x].sum()

gender_nv_model = open("model/AdaBoostClassifier.pkl","rb")
gender_clf = joblib.load(gender_nv_model)

def predict_gender(vec):
  vec[8] = word_2_vec(vec[8])
  vec.pop(0)
  result = gender_clf.predict([vec])
  return result
      
def load_images(file_name):
  img = Image.open(file_name)
  return st.image(img,width=300)
  
def main():
  nltk.download('punkt')
  original_title = '<b><p style="font-family:Courier; color:white; font-size: 40px;">Crome Extantion Analayze</p><b>'
  st.markdown(original_title, unsafe_allow_html=True)
  file = st.file_uploader("Upload a crx file", type=["crx", "zip"])
  with open("unnamed.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
  st.markdown(
  f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
  unsafe_allow_html=True
  )
  tabs_font_css = """
	<style>
	div[class*="stTextArea"] label {
	  font-size: 30px;
	  color: red;
	  font-weight: bold;
	}
	div[class*="stTextInput"] label {
	  font-size: 30px;
	  color: blue;
	  font-weight: bold;
	}
	div[class*="stNumberInput"] label {
	  font-size: 35px;
	  color: white;
	  font-weight: bold;
	}
	</style>
	"""

  st.write(tabs_font_css, unsafe_allow_html=True)
  if file:
    save_crx_file(file, "my_extension.crx")
    width = 10
    height = 20

    # Use the beta_container function to create a container
    container = st.container()

    # Set the CSS styles for the container
    container.markdown(
        f"""
        <style>
        .reportview-container .main .block-container{{
            max-width: {width}px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Add your content to the container
    with container:
        new_size = (400, 400) # Change the numbers to your desired size
        placeholder = st.image("Bean Eater-1s-207px.gif")
        with open("my_extension.crx", "rb") as crx_file:
          crx_bytes = crx_file.read()
          b64 = base64.b64encode(crx_bytes).decode()
          extracrt.extarct()
          feature = featu.feature("temp")
          predict = predict_gender(feature)
          os.system("rm my_extension.crx")
          os.system("rm -r temp")
          placeholder.empty()
          if predict[0] == 0:
            placeholder = st.image("good.png", width=300)
            txt = "benign"
            color = "green"
          else:
            txt = "malware"
            color = "red"
            placeholder = st.image("mal.png", width=300)
          htmlstr1=f"""<p style='background-color:{color};
                                           color:white;
                                           font-size:18px;
                                           border-radius:3px;
                                           line-height:60px;
                                           padding-left:17px;
                                           opacity:0.6'>
                                           {txt}</style>
                                           <br></p>""" 
    
          st.markdown(htmlstr1,unsafe_allow_html=True) 
main()
