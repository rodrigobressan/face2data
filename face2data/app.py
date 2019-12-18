from flask import Flask, request, jsonify, render_template, make_response
from face2data.predictor import load_model, predict_on_image
from face2data.preprocessing import pre_process_image

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.debug = True

model = load_model()


@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['image'].read()

    try:
        image = pre_process_image(image)
    except IOError as io:
        return make_response(jsonify({'error': io}), 400)

    prediction = predict_on_image(model, image)
    #
    # response = {
    #     'age': prediction,
    #     'race': prediction.race,
    #     'gender': prediction.gender,
    #     'race_confidence': prediction.race_confidence,
    #     'gender_confidence': prediction.gender_confidence
    # }

    return make_response(jsonify(prediction), 200)


@app.route('/how_it_works')
def how_it_works():
    return render_template('how.html')


@app.route('/dataset')
def dataset():
    return render_template('dataset.html')


@app.route('/')
def index():
    return render_template('index.html')


# When running through IDE/development
if __name__ == '__main__':
    app.run(debug=True)
