import streamlit as st
import joblib
model_nb=joblib.load('spam_ham')
st.title('spam-message-detector')
ip=st.text_input('Enter your Message:')
np=model_nb.predict([ip])
if st.button('PREDICT'):
   st.title[op[0])
