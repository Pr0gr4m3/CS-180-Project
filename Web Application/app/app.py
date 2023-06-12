import os

from dotenv import load_dotenv
from flask import Flask, render_template, request

from app.prediction_model import Model, feature_cols, response_col

# Set the cwd to the location of app.py
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config.from_prefixed_env()

with open("./Sleep_Efficiency.csv") as f:
    model = Model(f.read())


@app.post("/predict")
def predict():
    sleep_eff = model.predict(request.json)

    print(f"{sleep_eff = }")
    return {"sleep_efficiency": sleep_eff}, 200


@app.get("/")
def index():
    """Displays a form where user can input their model"""
    form_entries = "".join(
        f'<p><label for="{f}">{f}</label>'
        f'<input type="{f}" name="{f}" id="{f}"/></p>'
        for f in feature_cols
    )
    return render_template(
        "index.html", form_entries=form_entries, response_col=response_col
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
