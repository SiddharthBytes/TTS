import pyttsx3
import streamlit as st

st.title('Text-To-Speech App')

engine=pyttsx3.init()

voices=engine.getProperty('voices')
voice_names= [voice.name for voice in voices]


volume=engine.getProperty('volume')

rate=engine.getProperty('rate')


mode=st.radio('choose a option',['type/paste Text','upload a file'])

all_text=None

if mode=='type/paste Text':
    text=st.text_area('please type here')
    if text:
        all_text=text
elif mode=='upload a file':
    file=st.file_uploader('please upload the file')
    if file is not None:
        file_text=file.read().decode('utf-8')
        st.write('file contents :')
        st.text(file_text)
        all_text=file_text
else:
    pass


    


selected_voice=st.sidebar.selectbox('Choose a voice:', voice_names)

voice_obj=voices[voice_names.index(selected_voice)]

engine.setProperty('voice', voice_obj.id)

volume_st=st.slider('Volume: ',0.0,1.0,0.7,0.05)
engine.setProperty('volume',volume_st)


rate_st=st.sidebar.slider('Words Per Minute :',10,1000,200,10)
engine.setProperty('rate',rate_st)

if all_text and st.button('read'):
    engine.save_to_file(all_text, "output.wav")
    engine.runAndWait()
    st.audio("output.wav")

