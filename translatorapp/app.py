# app.py
from flask import Flask, request, jsonify
from translations import translate_color

app = Flask(__name__)

@app.route('/translate', methods=['GET'])
def translate():
    color = request.args.get('color')
    from_lang = request.args.get('from')
    to_lang = request.args.get('to')

    if not color or not from_lang or not to_lang:
        return jsonify({'error': 'Missing required parameters'}), 400

    translation = translate_color(color, from_lang, to_lang)
    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
