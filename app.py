# from flask import Flask, render_template, request, redirect, url_for
# import json

# app = Flask(__name__)

# # Load sample datasets from JSON files
# def load_hair_dataset():
#     with open('hair_dataset.json') as f:
#         return json.load(f)

# def load_skin_dataset():
#     with open('skin_dataset.json') as f:
#         return json.load(f)

# # Generate recommendations based on the selected type
# def get_recommendations(analysis_type, type_id):
#     if analysis_type == 'hair':
#         if int(type_id) == 1:
#             return 'Curly Hair Routine', ['Curly Hair Shampoo', 'Leave-in Conditioner'], 'Avoid sulfate products.'
#         elif int(type_id) == 2:
#             return 'Straight Hair Routine', ['Moisturizing Shampoo', 'Light Conditioner'], 'Use heat protectants.'
#         elif int(type_id) == 3:
#             return 'Wavy Hair Routine', ['Gentle Cleanser', 'Frizz Control Serum'], 'Limit heat styling.'
#     elif analysis_type == 'skin':
#         if int(type_id) == 1:
#             return 'Oily Skin Routine', ['Oil-Free Cleanser', 'Light Moisturizer'], 'Use non-comedogenic products.'
#         elif int(type_id) == 2:
#             return 'Dry Skin Routine', ['Hydrating Cleanser', 'Rich Moisturizer'], 'Avoid hot showers.'
#         elif int(type_id) == 3:
#             return 'Combination Skin Routine', ['Balancing Cleanser', 'Light Moisturizer'], 'Use spot treatments.'

# # Routes
# @app.route('/')
# def home():
#     return render_template('home.html')

# # @app.route('/submit', methods=['POST'])
# # # def submit():
# # #     user_data = {
# # #         'name': request.form['name'],
# # #         'email': request.form['email']
# # #     }
# # #     analysis_type = request.form.get('analysis_type')
# # #     return redirect(url_for('analysis', analysis_type=analysis_type))
# @app.route('/submit', methods=['POST'])
# def submit():
#     # Capture all user input data
#     user_data = {
#         'name': request.form['name'],
#         'email': request.form['email'],
#         'age': request.form['age'],
#         'gender': request.form['gender'],
#         'phone': request.form['phone'],
#         'concerns': request.form.get('concerns', ''),  # concerns is optional
#     }
    
#     # Log the data or save it to a database (if needed)
#     print(user_data)  # This prints user data to the console for now

#     # Capture the analysis type (hair/skin)
#     analysis_type = request.form.get('analysis_type')
    
#     # Redirect to the analysis page based on user's choice
#     return redirect(url_for('analysis', analysis_type=analysis_type))


# @app.route('/analysis/<analysis_type>')
# def analysis(analysis_type):
#     if analysis_type == 'hair':
#         dataset = load_hair_dataset()
#     elif analysis_type == 'skin':
#         dataset = load_skin_dataset()
#     return render_template('analysis.html', analysis_type=analysis_type, dataset=dataset)

# @app.route('/recommendation/<analysis_type>/<type_id>')
# def recommendation(analysis_type, type_id):
#     routine, products, tips = get_recommendations(analysis_type, type_id)
#     return render_template('result.html', routine=routine, products=products, tips=tips)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import csv

# app = Flask(__name__)

# # Load the CSV data from recommendations.csv
# def load_recommendations():
#     recommendations = {}
    
#     with open('static/data/recommendations.csv', mode='r') as file:
#         reader = csv.DictReader(file)
        
#         for row in reader:
#             if row['Type'] not in recommendations:
#                 recommendations[row['Type']] = []
#             recommendations[row['Type']].append(row)
    
#     return recommendations

# # Load hair and skin datasets for selection
# def load_hair_dataset():
#     return [
#         {'id': 1, 'name': 'Curly Hair'},
#         {'id': 2, 'name': 'Straight Hair'},
#         {'id': 3, 'name': 'Wavy Hair'}
#     ]

# def load_skin_dataset():
#     return [
#         {'id': 1, 'name': 'Oily Skin'},
#         {'id': 2, 'name': 'Dry Skin'},
#         {'id': 3, 'name': 'Combination Skin'}
#     ]

# # Route for the home page
# @app.route('/')
# def home():
#     return render_template('home.html')

# # Route to handle form submission and redirect to analysis page
# @app.route('/submit', methods=['POST'])
# def submit():
#     user_data = {
#         'name': request.form['name'],
#         'email': request.form['email']
#     }
#     analysis_type = request.form.get('analysis_type')
#     return redirect(url_for('analysis', analysis_type=analysis_type))

# # Route for hair/skin type selection
# @app.route('/analysis/<analysis_type>')
# def analysis(analysis_type):
#     if analysis_type == 'hair':
#         dataset = load_hair_dataset()
#     elif analysis_type == 'skin':
#         dataset = load_skin_dataset()
#     return render_template('analysis.html', analysis_type=analysis_type, dataset=dataset)

# # Route to show product recommendations based on selection
# @app.route('/recommendation/<analysis_type>/<type_id>')
# def recommendation(analysis_type, type_id):
#     recommendations = load_recommendations()
    
#     if analysis_type == 'hair':
#         if type_id == '1':
#             type_name = 'Curly Hair'
#         elif type_id == '2':
#             type_name = 'Straight Hair'
#         elif type_id == '3':
#             type_name = 'Wavy Hair'
#     elif analysis_type == 'skin':
#         if type_id == '1':
#             type_name = 'Oily Skin'
#         elif type_id == '2':
#             type_name = 'Dry Skin'
#         elif type_id == '3':
#             type_name = 'Combination Skin'
    
#     # Filter recommendations for the selected type
#     recommended_products = recommendations.get(type_name, [])
    
#     return render_template('result.html', type_name=type_name, recommendations=recommended_products)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Load sample datasets
def load_hair_dataset():
    return [
        {'id': 1, 'name': 'Curly Hair'},
        {'id': 2, 'name': 'Straight Hair'},
        {'id': 3, 'name': 'Wavy Hair'}
    ]

def load_skin_dataset():
    return [
        {'id': 1, 'name': 'Oily Skin'},
        {'id': 2, 'name': 'Dry Skin'},
        {'id': 3, 'name': 'Combination Skin'}
    ]

# Load recommendations from CSV
def load_recommendations():
    recommendations = {}
    with open('static/data/recommendations.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            type_name = row['Type']
            if type_name not in recommendations:
                recommendations[type_name] = []
            recommendations[type_name].append({
                'Product Name': row['Product Name'],
                'Product Type': row['Product Type'],
                'Description': row['Description']
            })
    return recommendations

# Pre-load recommendations
recommendations_data = load_recommendations()

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'age': request.form['age'],
        'gender': request.form['gender']
    }
    analysis_type = request.form.get('analysis_type')
    return redirect(url_for('analysis', analysis_type=analysis_type))

@app.route('/analysis/<analysis_type>')
def analysis(analysis_type):
    if analysis_type == 'hair':
        dataset = load_hair_dataset()
    elif analysis_type == 'skin':
        dataset = load_skin_dataset()
    return render_template('analysis.html', analysis_type=analysis_type, dataset=dataset)

@app.route('/recommendation/<analysis_type>/<type_id>')
def recommendation(analysis_type, type_id):
    # Map type_id to names in the dataset
    if analysis_type == 'hair':
        dataset = load_hair_dataset()
    else:
        dataset = load_skin_dataset()

    selected_type = next((item for item in dataset if item['id'] == int(type_id)), None)
    type_name = selected_type['name'] if selected_type else None

    if type_name and type_name in recommendations_data:
        recommendations = recommendations_data[type_name]
    else:
        recommendations = []

    return render_template('result.html', type_name=type_name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
