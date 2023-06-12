# cs180-project-webapp
 
Setup
```bash
py -m venv venv
.\venv\Scripts\activate
pip install scikit-learn numpy pandas seaborn matplotlib flask python-dotenv
```

Run with
```bash
py -m app.app
# or, when deploying on Linux
FLASK_RUN_PORT=$PORT FLASK_RUN_HOST=0.0.0.0 flask -app app/app --run
```
