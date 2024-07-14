import sqlite3
from datetime import datetime

def add_maintenance_cost(asset_id, details, cost):
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute("INSERT INTO maintenance (asset_id, maintenance_date, details, cost) VALUES (?, ?, ?, ?)",
              (asset_id, str(datetime.now()), details, cost))

    conn.commit()
    conn.close()

def get_total_cost(asset_id):
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute("SELECT SUM(cost) FROM maintenance WHERE asset_id = ?", (asset_id,))
    total_cost = c.fetchone()[0]

    conn.close()
    return total_cost

if __name__ == '__main__':
    add_maintenance_cost(1, 'Replaced battery', 50.0)
    print(get_total_cost(1))
