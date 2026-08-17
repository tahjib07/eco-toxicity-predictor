import streamlit as st
import requests

# Apply your UI/UX skills to structure the app
st.set_page_config(page_title="Pharma AI Predictor", layout="centered")

st.title("🧪 Eco-Toxicity Predictor")
st.write("Enter a chemical SMILES string to predict its properties.")

# Text input for the user
user_smiles = st.text_input("SMILES String", placeholder="e.g., CCO (Ethanol)")

# Action button
if st.button("Analyze Chemical"):
    if user_smiles:
        # Call your FastAPI backend
        api_url = "http://127.0.0.1:8000/predict"
        payload = {"smiles": user_smiles}
        
        with st.spinner("Analyzing molecular structure..."):
            response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                st.success("Analysis Complete!")
                
                # Display the results in columns
                col1, col2 = st.columns(2)
                col1.metric("Molecular Weight", f"{data['molecular_weight']} g/mol")
                
                # Add a visual warning if toxicity is high
                tox_score = data['predicted_toxicity_risk']
                if tox_score > 0.5:
                    col2.error(f"Toxicity Risk: {tox_score} (HIGH)")
                else:
                    col2.success(f"Toxicity Risk: {tox_score} (LOW)")
            else:
                st.error("Invalid SMILES string. Please check the structure and try again.")
    else:
        st.warning("Please enter a SMILES string first.")