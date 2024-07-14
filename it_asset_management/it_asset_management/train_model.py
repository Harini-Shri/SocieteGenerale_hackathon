import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
from datetime import datetime
from datetime import timedelta
import random

def generate_dummy_data():
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()
    
    for asset_id in range(1, 6):  # Assuming 5 assets
        for _ in range(10):  # 10 maintenance records per asset
            maintenance_date = datetime.now() - timedelta(days=random.randint(30, 365))
            cost = random.uniform(20, 200)
            c.execute("INSERT INTO maintenance (asset_id, maintenance_date, details, cost) VALUES (?, ?, ?, ?)",
                      (asset_id, maintenance_date, 'Dummy maintenance', cost))

    conn.commit()
    conn.close()

def train_model():
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()
    c.execute("SELECT asset_id, maintenance_date, cost FROM maintenance")
    data = c.fetchall()
    
    if len(data) < 50:  # Check if there's enough data
        generate_dummy_data()
        c.execute("SELECT asset_id, maintenance_date, cost FROM maintenance")
        data = c.fetchall()

    conn.close()

    df = pd.DataFrame(data, columns=['asset_id', 'maintenance_date', 'cost'])
    df['maintenance_date'] = pd.to_datetime(df['maintenance_date'])
    df['days_since_last_maintenance'] = (pd.to_datetime('now') - df['maintenance_date']).dt.days

    X = df[['asset_id', 'days_since_last_maintenance']]
    y = df['cost']

    model = RandomForestRegressor()
    model.fit(X, y)

    with open('maintenance_model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    train_model()
