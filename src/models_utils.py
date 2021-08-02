from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import yaml
import numpy as np


class Model:
    def __init__(self, config):
        self.model = DistilBertForSequenceClassification.from_pretrained(config['model']['model_path'])
        self.tokenizer = DistilBertTokenizerFast.from_pretrained(config['model']['tokenizer_path'])

    def predict(self, inputs):
        inputs = self.tokenizer(inputs, return_tensors='pt', truncation=True, padding=True)
        outputs = self.model(**inputs)
        return ['Negative' if np.argmax(i) == 0 else 'Positive' for i in outputs.logits.detach().numpy()]

    def test_model(self):
        inputs = self.tokenizer(['A Good movie indeed',
                                 'A really bad movie, did not like the actors',
                                 'Worst thing i ever saw'],
                                return_tensors='pt',
                                truncation=True,
                                padding=True)
        output = self.model(**inputs)
        return ['Negative' if np.argmax(i) == 0 else 'Positive' for i in output.logits.detach().numpy()]


if __name__ == "__main__":
    params_path = './params.yaml'
    config = None
    with open(params_path, 'r') as f:
        config = yaml.safe_load(f)

    model = Model(config)
    print(model.test_model())

