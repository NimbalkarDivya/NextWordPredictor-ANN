# 🤖 Next Word Prediction using ANN

An end-to-end NLP project that predicts the **next word in a sentence** using a trained **Artificial Neural Network (ANN)** model.
The project includes a **Flask backend API** and a **simple interactive frontend UI**.

---

## 🚀 Features

* 🧠 ANN-based deep learning model
* 🔤 Tokenization & sequence prediction
* ⚡ Real-time prediction via Flask API
* 🌐 Simple and clean frontend interface
* 🔗 Full-stack integration (ML + Backend + Frontend)

---

## 📁 Project Structure

```
NextWordPrediction/
│
├── backend/
│   ├── app.py
│   ├── next_word_model.h5
│   ├── tokenizer.pkl
│
├── frontend/
│   └── index.html
│
├── dataset/
│   └── text_data.txt
│
├── training/
│   └── model_training.py
│
├── venv/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download Project

```bash
git clone <your-repo-link>
cd NextWordPrediction
```

---

### 2️⃣ Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If TensorFlow is not installed:

```bash
pip install tensorflow
```

---

### 4️⃣ Install Additional Package (for frontend-backend connection)

```bash
pip install flask-cors
```

---

## 🧠 Train the Model (Optional)

If model files are not present:

```bash
cd training
python model_training.py
```

This will generate:

* `next_word_model.h5`
* `tokenizer.pkl`

Move them into the `backend/` folder.

---

## 🚀 Run the Application

### 🔹 Step 1: Start Backend (Flask API)

```bash
cd backend
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

---

### 🔹 Step 2: Start Frontend

Open a new terminal:

```bash
cd frontend
python -m http.server 5500
```

---

### 🔹 Step 3: Open in Browser

```
http://127.0.0.1:5500/index.html
```

---

## 🧪 How to Use

1. Enter a sentence (e.g., **"I love"**)
2. Click **Predict**
3. The model predicts the **next word**

---

## 🔗 API Endpoint

### POST `/predict`

#### Request:

```json
{
  "text": "I love"
}
```

#### Response:

```json
{
  "input": "I love",
  "next_word": "coding"
}
```

---

## ⚠️ Common Issues & Fixes

### ❌ 405 Method Not Allowed

✔ Cause: Using GET instead of POST
✔ Fix: Use POST request or frontend UI

---

### ❌ CORS Error

✔ Fix:

```python
from flask_cors import CORS
CORS(app)
```

---

### ❌ ModuleNotFoundError: tensorflow

✔ Fix:

```bash
pip install tensorflow
```

---

### ❌ Frontend not connecting

✔ Ensure:

* Backend is running on port 5000
* Frontend is running on port 5500

---

## 🛠️ Tech Stack

* Python 🐍
* TensorFlow / Keras 🤖
* Flask 🌐
* HTML, CSS, JavaScript 🎨

---

## ⚠️ Note

While LSTM/GRU models are commonly used for sequence prediction tasks, this project uses an **Artificial Neural Network (ANN)** to understand the fundamentals of text preprocessing, sequence generation, and prediction. Future improvements include upgrading the model to LSTM for better context understanding.

---

## 💡 Future Improvements

* 🔥 Top 3 word predictions
* ⚡ Auto-suggestions while typing
* 📱 Responsive UI (React + Tailwind)
* 🌍 Deployment (Render / AWS)

---

## 🎯 Conclusion

This project demonstrates:

* NLP sequence modeling using Artificial Neural Networks (ANN)
* API development with Flask
* Frontend-backend integration

---

## 👩‍💻 Author

**Divya Nimbalkar**
BTech CSE (Data Science)
Aspiring AI & Full Stack Engineer 🚀

---
