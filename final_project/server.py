'''server module : renders an iindex file on port 8080
   allow traduction of text from input text to either english or french
'''
from flask import Flask, render_template, request
from machinetranslation import translator


app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    '''
        english to french function route
    '''
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(text_to_translate)
    return translated_text

@app.route("/frenchToEnglish")
def french_to_english():
    '''
        french to english function route
    '''
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text

@app.route("/")
def render_index_page():
    '''
        index rendering function route
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
