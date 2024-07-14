import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import pickle

def load_model():
    with open('maintenance_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict_maintenance(asset_id):
    model = load_model()
    
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()
    c.execute("SELECT maintenance_date FROM maintenance WHERE asset_id = ?", (asset_id,))
    records = c.fetchall()
    conn.close()
    
    if records:
        last_maintenance_date = pd.to_datetime(records[-1][0])
        days_since_last_maintenance = (datetime.now() - last_maintenance_date).days
        
        prediction = model.predict([[asset_id, days_since_last_maintenance]])
        next_maintenance_date = datetime.now() + timedelta(days=int(prediction[0]))
        return next_maintenance_date.strftime('%Y-%m-%d')  # Return predicted date as string
    else:
        return "No maintenance record found."

def predict_from_input(asset_id, days_since_last_maintenance):
    model = load_model()
    
    try:
        days_since_last_maintenance = int(days_since_last_maintenance)
    except ValueError:
        return "Invalid input for days since last maintenance."
    
    prediction = model.predict([[asset_id, days_since_last_maintenance]])
    next_maintenance_date = datetime.now() + timedelta(days=int(prediction[0]))
    
    return next_maintenance_date.strftime('%Y-%m-%d')  # Return predicted date as string

if __name__ == '__main__':
    print(predict_maintenance(1))
