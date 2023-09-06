from flask import Flask, request, render_template
from backend import breed_prediction as b, register_helper, chatbot, breed_recommender, vet_recommender as r
from backend.disease_prediction import predictDisease, getDiseaseDescription, getDietRecommendation

app = Flask(__name__)
app.static_folder = 'public'

# Home page route


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        register_helper.append_data(request.form)
    return render_template('index.html')

# Breed classifier page route


@app.route('/breed-classifier')
def breed_classifier():
    return render_template('breed-classification.html')

# Prediction route


@app.route('/predict', methods=['POST'])
def predict():
    if 'dog_image' not in request.files:
        return 'No file uploaded', 400
    image_file = request.files['dog_image']
    image_path = 'uploaded_image.jpg'  # Path to save the uploaded image
    image_file.save(image_path)
    predicted_breed = b.predict_breed(image_path)
    return predicted_breed

# Chatbot route


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot.chatbot_response(userText)

# Disease prediction route


@app.route("/disease-prediction", methods=["GET", "POST"])
def disease_prediction():
    dp = dis_pred = dsc = dis_desc = diet = diet_rec = ""
    dh = dnh = ddh = drh = ""

    if request.method == "POST":
        sym1 = request.form['symptom1']
        sym2 = request.form['symptom2']
        sym3 = request.form['symptom3']
        fsym = sym1 + "," + sym2 + "," + sym3

        dh = "Report Generated"
        dnh = "Disease Name"
        ddh = "Disease Information"
        drh = "Recommended Diet"

        dp = predictDisease(fsym)
        dsc = getDiseaseDescription(dp)
        diet = getDietRecommendation(dp)

    return render_template('disease-prediction.html', disease_heading=dh, disease_name=dnh,
                           disease_desc=ddh, diet_recm=drh, my_disease=dp,
                           my_description=dsc, my_diet=diet)

# Vet recommendation route


@app.route("/vet-recommendation", methods=["GET", "POST"])
def vet_recommender_route():
    nearest_vet = nv = vh = ""

    if request.method == "POST":
        cityname = request.form['city_name']
        sectornum = request.form['sector_num']

        nearest_vet = r.vet_rec(cityname, sectornum)
        vh = "Nearest Vet to given Location"
        nv = nearest_vet

    return render_template('vet-recommendation.html', vet_heading=vh, my_vet=nv)

# Breed recommendation route


@app.route('/breed-recommendation', methods=['GET', 'POST'])
def breed_route():
    if request.method == 'POST':
        prediction = breed_recommender.breed_recommendation(request.form)
        return render_template('breed-recommendation.html', prediction=prediction)
    else:
        return render_template('breed-recommendation.html')


# Run the Flask app
if __name__ == "__main__":
    app.run()
