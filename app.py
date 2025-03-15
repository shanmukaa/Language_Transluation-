from flask import Flask, send_file
from psd_tools import PSDImage

app = Flask(__name__)

@app.route('/render-psb')
def render_psb():
    psd = PSDImage.open('static/psb/weddihng.psb')
    psd.composite().save('static/psb/rendered.png')
    return send_file('static/psb/rendered.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)