# IMDB Sentiment Analysis
Classify a movie review into Positive or Negative review using DistilBERT Transformer.<br/>
A pre-trained DistilBERT transformer model was used which was fine-tuned on the IMDB reviews dataset. 
<br/><br/>
##  Webapp
### Home page
![home page](https://raw.githubusercontent.com/Modojojo/imdb-sentiment-analysis/main/screenshots/home.PNG)
### Positive review 
![positive review input](https://raw.githubusercontent.com/Modojojo/imdb-sentiment-analysis/main/screenshots/positive_with_review.PNG)
### Prediction for Positive review
![prediction for positive review](https://raw.githubusercontent.com/Modojojo/imdb-sentiment-analysis/main/screenshots/positive_prediction.PNG)
### Negative Review
![negative review input](https://github.com/Modojojo/imdb-sentiment-analysis/blob/main/screenshots/Negative_with_review.PNG)
### Prediction for negative review
![prediction for negative review](https://raw.githubusercontent.com/Modojojo/imdb-sentiment-analysis/main/screenshots/negative_review.PNG)
<br/><br/>
##  Repository Structure 
```
main
|── models
|    |── model                   # Holds model files
|    └── tokenizer               # Holds tokenizer files 
|
|── screenshots                  # Contains webapp screenshots
|
|── src
|    |── __init__.py     
|    └── models_utils.py         # Model loading and prediction utility
|
|── templates
|    |── index.html 
|    └── error.html
| 
|── training
|    └── imdb_sentiment_analysis_training.ipynb    # Training notebook
|
|── .gitignore
|── README.md
|── app.py
|── params.yaml
|── requirements.txt
└── setup.py
```
<br/><br/>
## Setup
  1. Create a new conda environment 
```
conda create -n imdb-sentiment-analysis python==3.7
```
  2. run the setup file <br/>
  **Note** - If any error occurs for any package, comment the corresponding package in requirements.txt file and install the dependency separately.
```
pip install .
```
  3. Use the notebook provided in Training folder to train a DistilBERT Transformer model on the imdb reviews dataset.
  4. Download/Save the trained Model and Tokenizer files and paste them in the corresponding folder in the models directory.
  5. Run the app 
```
python app.py
```
