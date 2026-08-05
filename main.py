import streamlit as st
import edge_tts
import asyncio

st.title('Text-To-Speech App')
voices= asyncio.run(edge_tts.list_voices())[:10]
voice_names= [voice['ShortName'] +' (' + voice['Locale'] +')' for voice in voices]

selected_voice=st.sidebar.selectbox('Choose a voice:', voice_names)

mode=st.radio('Choose a mode from below',options=['type/paste text','upload file(.txt)'])

all_text=None
if mode=='type/paste text':
    text=st.text_area('Paste or Type here')
    all_text=text
elif mode=='upload file(.txt)':
    file=st.file_uploader('Upload your file below',type=['txt'])
    if file is not None:
        file_text=file.read().decode('utf-8')
        st.write(f'File contents: {file_text}')
        all_text=file_text
volume=st.slider('Volume (%):',0,100,70)
rate=st.slider('Words Per Minute(WPM)/rate(%):',min_value=-50,max_value=50,value=0)

communicate=None

rate_tts=None
if rate == 0:
    rate_tts='+0%'
elif rate > 0:
    rate_tts=f'+{rate}%'
elif rate < 0:
    rate_tts=f'-{rate}%'

volume_tts=None

if volume > 0:
    volume_tts=f'+{volume}%'
elif volume == 0:
    volume_tts='+0%'
else:
    volume_tts=f'{volume}%'




if all_text and st.button('Read'):
    ShortName=selected_voice.split(' ')[0]

    communicate=edge_tts.Communicate(
        text=all_text,
        voice=ShortName,
        rate=rate_tts,
        volume=volume_tts

    )
if communicate:
    asyncio.run(communicate.save("output.mp3"))
    st.audio('output.mp3')

