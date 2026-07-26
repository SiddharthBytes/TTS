import pyttsx3
import streamlit as st

st.title('Text-To-Speech App')

engine=pyttsx3.init()

voices=engine.getProperty('voices')
voice_names= [voice.name for voice in voices]

selected_voice=st.selectbox('Choose a voice:', voice_names)
engine.setProperty('voices',[voice_names.index(selected_voice)])

volume=engine.getProperty('volume')
volume_st=st.slider('Volume: ',0.0,1.0,0.7,0.05)
engine.setProperty('Volume : ',volume_st)

rate=engine.getProperty('rate')
rate_st=st.slider('Words Per Minute :',10,1000,200,10)
engine.setProperty('rate',rate_st)

name=st.text_input('please enter your name below :')
if name :
     engine.say(f'welcome {name}')
else:
     engine.say('please enter your name')
engine.runAndWait()