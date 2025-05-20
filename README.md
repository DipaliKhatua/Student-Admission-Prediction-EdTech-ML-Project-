# Student Admission Prediction (EdTech ML Project)

## 🚀 Project Overview
A machine learning model that predicts **student admission chances** based on academic records, university rating, and research experience.

## 📂 Directory Structure
- artifacts/  (Stores the trained model)
- app.py  (Flask API)
- requirements.txt  (Dependencies)
- README.md  (Project Documentation)

## 🔧 Tech Stack Used
- **Machine Learning:** Scikit-learn (Random Forest Regressor)
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Model Deployment:** Flask
- **API Testing:** Thunder Client

## 🏗️ Steps to Set Up & Run
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

- Train & Save Model
import pickle
with open("artifacts/random_forest_model.pkl", "wb") as file:
    pickle.dump(trained_model, file)
- 
- Run the Flask API
python app.py
- Test API with Thunder Client Send a POST request to:
http://127.0.0.1:5000/predict

- With JSON body:
{
  "GRE Score": 320,
  "TOEFL Score": 110,
  "University Rating": 4,
  "SOP": 4.5,
  "LOR": 4.0,
  "CGPA": 9.2,
  "Research": 1
}
- Example Response
{
  "Chance of Admit": 0.86
}
 ### Model Performance:
 - Evaluation Metric : MAE
 - MAE = 0.0438 (Low error, good predictions)

# Author
Dipali Khatua
Aspiring Data Scientist
Connect me : https://www.linkedin.com/in/dipalikhatua/