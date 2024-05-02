from flask import Flask, request, jsonify
import requests
import joblib


model = joblib.load('model.joblib')

# List of feature names that your model was trained on
feature_names =['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
       'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
       'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
       'touch_screen', 'wifi',]

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data, '\n')
    
     # Select only the features that your model was trained on
    features = [data[feature] for feature in feature_names]
    prediction = model.predict([features])
    print('prediction ',  prediction.tolist()[0], '\n')
    return jsonify({'prediction': prediction.tolist()[0]})

if __name__ == '__main__':
    app.run(port=5000, debug=True)