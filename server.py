#http://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart
from flask import Flask, request, jsonify
import os
import pickle
from processing_text import get_clean_text 

app = Flask(__name__)

classifier_filepath = os.path.join("logistic_regression.pkl")
classifier_file = open(classifier_filepath, "rb")
classifier = pickle.load(open(classifier_filepath, "rb"))
classifier_file.close()



@app.route('/predict', methods=['POST'])
def predict():
 
    data = request.get_json(force=True)  
    data_transformed = [get_clean_text(comment) for comment in data]  
    result=classifier.predict(data_transformed)
    return jsonify({
        "comments": data,
        "results": result.tolist()})
 
if __name__ == '__main__':
    app.run(port=8080, debug=True)