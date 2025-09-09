# 📝 Multiple Disease Prediction (Machine Learning)

A **comprehensive application** that leverages **machine learning** to **predict multiple diseases** from user-provided medical inputs. Designed with flexibility and usability in mind, the app delivers accurate predictions via a streamlined user interface.


## ✨Features
-  **Predict Multiple Conditions** — Supports prediction for diseases like **diabetes**, **heart disease**, and **Parkinson’s disease**.
-  **Machine Learning Models** — Includes classifiers such as **Logistic Regression**, **Support Vector Machine (SVM)**, and **Random Forest** tailored per disease.
-  **Interactive Interface** — Built with **Streamlit** (or your chosen UI tool) for responsive, web-based interactivity.
-  **Parameter Input Forms** — Collects disease-specific clinical parameters like age, blood pressure, glucose levels, etc.
-  **Real-Time Prediction** — Instantly displays prediction results along with model accuracy or confidence.
-  **Model Persistence** — Utilizes **pickle** or **joblib** to load pre-trained models for quick inference.
-  **Visual Feedback** — Optionally includes performance metrics or charts (e.g., accuracy, confusion matrix).


##  🛠Tech Stack Used
- **Python** – Core programming language.
- **scikit-learn** – For building and evaluating classification models.
- **Streamlit** – For crafting the user interface.
- **pickle / joblib** – For saving and loading trained models.
- **Pandas / NumPy** – Efficient data handling and preprocessing.
- **Matplotlib / Seaborn** – (Optional) Visualization of model performance.


##  🛠Installation Process
To set up the project locally:
```bash
# 1️⃣ Clone the repository
git clone https://github.com/singharpana-24/Multiple-Disease-Prediction-ML.git
# 2️⃣ Move to project directory
cd Multiple-Disease-Prediction-ML
# 3️⃣ Create a virtual environment (recommended)
python -m venv venv
# 4️⃣ Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
# 5️⃣ Install dependencies
pip install -r requirements.txt

# 6️⃣ Launch the app
streamlit run app.py
```


## 🚀 How to Run
```bash
streamlit run app.py
```


## 📌Project Preview
<img width="1903" height="1015" alt="Screenshot 2025-09-09 175613" src="https://github.com/user-attachments/assets/785837cf-a41a-470c-a4f4-acc46d66bb91" />


