import sqlite3
from datetime import datetime
import asset_management

def update_asset_status(asset_id, status):
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute("UPDATE assets SET status = ? WHERE id = ?", (status, asset_id))

    conn.commit()
    conn.close()

def get_lifecycle_data():
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute("SELECT * FROM assets")
    assets = c.fetchall()

    conn.close()
    return assets

if __name__ == '__main__':
    update_asset_status(1, 'Decommissioned')
    print(asset_management.get_assets())
