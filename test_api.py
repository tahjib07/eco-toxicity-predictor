from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rdkit import Chem
from rdkit.Chem import Descriptors

# Initialize the API
app = FastAPI(title="COMP3D Pharma API")

# Define what the incoming data should look like
class MoleculeInput(BaseModel):
    smiles: str

# Create an endpoint that listens for POST requests
@app.post("/predict")
def predict_chemical_properties(data: MoleculeInput):
    # 1. Convert the SMILES string into an RDKit molecule object
    mol = Chem.MolFromSmiles(data.smiles)
    
    # 2. Check if the SMILES string is valid
    if mol is None:
        raise HTTPException(status_code=400, detail="Invalid SMILES string provided.")
    
    # 3. Calculate the molecular weight using RDKit
    mol_weight = Descriptors.ExactMolWt(mol)
    
    # 4. Create a dummy toxicity score (just for this toy example)
    # In the future, your PyTorch GNN model will go here!
    dummy_toxicity = round(mol_weight / 500, 2) 
    
    # 5. Return the data as a JSON response
    return {
        "smiles": data.smiles,
        "molecular_weight": round(mol_weight, 2),
        "predicted_toxicity_risk": dummy_toxicity
    }