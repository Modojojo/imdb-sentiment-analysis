from flask import Flask, render_template, request
from src.models_utils import Model
import yaml

template_dir = 'templates'

app = Flask(__name__, template_folder=template_dir)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', display="none")


@app.route('/predict', methods=['POST'])
def prediction():
    sentences = request.form['sentence']
    if sentences == '' or sentences == ' ':
        return render_template('error.html', err_msg='Please enter a valid review')
    try:
        output = model.predict(sentences)
    except Exception as e:
        return render_template('error.html', err_msg=str(e))
    if output[0] == 'Positive':
        prediction = 'Positive Review'
        display = 'show'
        jumbotron_bg = "#88eba2"
        text_color = '#185e18'
    elif output[0] == 'Negative':
        prediction = 'Negative Review'
        display = 'show'
        jumbotron_bg = "#ed7e7e"
        text_color = '#a30000'

    return render_template('index.html',
                           prediction=prediction,
                           display=display,
                           jumbotron_bg=jumbotron_bg,
                           text_color=text_color)


def read_params(params_path):
    with open(params_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


if __name__ == '__main__':
    config = read_params('params.yaml')
    model = Model(config)
    app.run()