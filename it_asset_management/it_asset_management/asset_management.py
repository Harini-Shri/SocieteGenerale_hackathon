import sqlite3
from datetime import datetime

def add_asset(name, asset_type, purchase_date, warranty_period, status):
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute("INSERT INTO assets (name, type, purchase_date, warranty_period, status) VALUES (?, ?, ?, ?, ?)",
              (name, asset_type, purchase_date, warranty_period, status))

    conn.commit()
    conn.close()

def get_assets():
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute("SELECT * FROM assets")
    assets = c.fetchall()

    conn.close()
    return assets

def delete_asset(asset_id):
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute("DELETE FROM assets WHERE id = ?", (asset_id,))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    add_asset('Laptop XYZ', 'Laptop', str(datetime.now()), 24, 'Active')
    print(get_assets())
