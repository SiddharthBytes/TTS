#hey everyone here you will find lots of comments and explanations about the code.
#so you can understand it better and learn from it
#but i am writing it because i write ml notebooks and there we usually write markdown 



#downloading the required libraries
import streamlit as st
import edge_tts
import asyncio

#source of the gif
st.image('https://cdn.pixabay.com/animation/2024/10/17/21/08/21-08-48-468_512.gif')

#background color with customize html 

st.markdown("""
<style>
.stApp {
    background-color: #0d0d0d;
    color: #ff7518; 
}
</style>
""", unsafe_allow_html=True)

#title of the app
st.title('Text-To-Speech App')

#extracting the first 10 voices from the list of voices in edgetts

voices= asyncio.run(edge_tts.list_voices())[:10]
voice_names= [voice['ShortName'] +' (' + voice['Locale'] +')' for voice in voices]
#showing the extracted voices
selected_voice=st.sidebar.selectbox('Choose a voice:', voice_names)
#gicing user a choice
mode=st.radio('Choose a mode from below',options=['type/paste text','upload file(.txt)'])

all_text=None
#for typing or pasting text
if mode=='type/paste text':
    text=st.text_area('Paste or Type here')
    all_text=text
#uploading the .txt file and making it readable for thebackend
elif mode=='upload file(.txt)':
    file=st.file_uploader('Upload your file below',type=['txt'])
    if file is not None:
        file_text=file.read().decode('utf-8')
        st.write(f'File contents: {file_text}')
        all_text=file_text
#ui for volume and words per minute sliders
volume=st.slider('Volume (%):',0,100,70)
rate=st.slider('Words Per Minute(WPM)/rate(%):',min_value=-50,max_value=50,value=0)

communicate=None

#converting the value the user choose for making the edge tts read able 
#edge tts accept string with % percentage symbol and we get a int value from st.slider

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



#making it read here the main function is called Communicate
#C in capital alphabets

if all_text and st.button('Read'):
    ShortName=selected_voice.split(' ')[0]

    communicate=edge_tts.Communicate(
        text=all_text,
        voice=ShortName,
        rate=rate_tts,
        volume=volume_tts

    )

#last step to save the generated audio of what you uploaded 

if communicate:
    asyncio.run(communicate.save("output.mp3"))
    st.audio('output.mp3')
