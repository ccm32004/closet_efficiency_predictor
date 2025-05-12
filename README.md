# closet_efficiency_predictor
model that predicts the chance that one will wear an article of clothing based on given parameters !
- uses random forest regression, model accuracy constrained by small data sizee
- run via streamlit run app.py (must cd into app folder first)
- dockerization: 
  - to build image: `docker build -t wear-predictor-app .`
  - to run container: `docker run -p 8501:8501 wear-predictor-app`
