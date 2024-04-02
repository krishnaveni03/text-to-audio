import streamlit as st
from gtts import gTTS
from googletrans import Translator
import requests
import os

# Custom CSS
custom_css = """
<style>
/* Add your custom CSS styles here */
body {
    font-family: 'Arial', sans-serif;
    background-color: #7b68ee; /* Purple background color */
    margin: 20px; /* Add margin */
}

h1 {
    color: #fff; /* White text color */
    font-family: 'Times New Roman', serif; /* Custom font family */
}

textarea {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    font-size: 16px;
    margin-bottom: 20px;
}

select {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 8px;
    font-size: 16px;
    margin-bottom: 20px;
}

.button-primary {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 10px; /* Add margin */
}

.button-primary:hover {
    background-color: #0056b3;
}
</style>
"""

# Main function for Streamlit app
def main():
    # Set page title and background color
    st.set_page_config(page_title="Text to Audio Converter", page_icon="🔊", layout="centered", initial_sidebar_state="collapsed")

    # Inject custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Set title and subtitle
    st.title("Text to Audio Converter")
    st.write("Convert your text into audio in different languages!")

    # Input text area
    text = st.text_area("Enter your text here:", height=150)

    # Language selection
    languages = {
        "English": "en",
        "Hindi": "hi",
        "Telugu": "te",
        "Tamil": "ta",
        "Spanish": "es",
        "French": "fr",
    }
    lang = st.selectbox("Select Language", list(languages.keys()))

    # Convert button
    convert_button_clicked = st.button("Convert to Audio", key="convert_button")

    # Convert text to audio when button is clicked
    if convert_button_clicked:
        if text:
            lang_code = languages[lang]

            # Convert original text to audio
            tts_original = gTTS(text, lang=lang_code)
            with st.spinner("Converting original text to audio..."):
                output_file_original = "output_original.mp3"
                tts_original.save(output_file_original)
            st.audio(output_file_original, format="audio/mp3", start_time=0)

    # Translate button
    translate_button_clicked = st.button("Translate Text", key="translate_button")

    # Translate text when button is clicked
    if translate_button_clicked:
        if text:
            try:
                translator = Translator()
                translated_text = translator.translate(text, dest=languages[lang]).text
                st.text_area("Translated Text", value=translated_text, height=150)

                # Convert translated text to audio
                tts_translated = gTTS(translated_text, lang='en')  # Use 'en' for English
                with st.spinner("Converting translated text to audio..."):
                    output_file_translated = "output_translated.mp3"
                    tts_translated.save(output_file_translated)
                st.audio(output_file_translated, format="audio/mp3", start_time=0)
            except Exception as e:
                st.error("Translation failed. Please try again later.")
                print(e)

if __name__ == "__main__":
    main()
