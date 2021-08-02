from flask import Flask, render_template, request
from src.models_utils import Model
import yaml

template_dir = 'templates'

app = Flask(__name__, template_folder=template_dir)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def prediction():
    # sentences = request.form['sentence']
    # model.predict(sentences)
    return render_template('index.html')


def read_params(params_path):
    with open(params_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


if __name__ == '__main__':
    config = read_params('params.yaml')
    model = Model(config)
    app.run()