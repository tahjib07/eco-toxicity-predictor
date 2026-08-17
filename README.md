# 🧪 Eco-Toxicity Predictor (Microservice Architecture)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit)
![RDKit](https://img.shields.io/badge/RDKit-Cheminformatics-green)

A full-stack, decoupled computational science microservice designed to predict the ecological toxicity risk of chemical compounds using their SMILES strings. 

This project demonstrates a seamless integration of **Cheminformatics (RDKit)**, **High-Performance Backend Engineering (FastAPI)**, and **Clean UI/UX Design (Streamlit)**.

---

## 🏗 Architecture
This application is split into two isolated services:
1. **Backend API (`test_api.py`)**: A FastAPI server that ingests molecular data, validates it, and calculates properties using RDKit.
2. **Frontend UI (`app.py`)**: A Streamlit web dashboard providing a frictionless, interactive user experience to input data and visualize the analytical results.

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/eco-toxicity-predictor.git
cd eco-toxicity-predictor
```

**2. Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Running the Application

You will need two terminal windows to run the decoupled services.

**Terminal 1: Start the Backend API**
```bash
uvicorn test_api:app --reload
```
*The API will be available at `http://localhost:8000`*

**Terminal 2: Start the Frontend UI**
```bash
streamlit run app.py
```
*The dashboard will automatically open in your browser at `http://localhost:8501`*

---
*Designed and developed by Tahjib Ahmed Siddique.*
