from flask import Flask, render_template, jsonify, request

import altair as alt
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    dataset_name = 'cars'

    return render_template('index.html', dataset_name=dataset_name)

@app.route('/json/<dataset_name>')
def return_vega_json(dataset_name):

    cars = alt.load_dataset(dataset_name)

    j = alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).to_json()

    return jsonify(j)

if __name__ == '__main__':
    app.run(debug=True)
