import sqlite3

def create_tables():
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS assets (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 type TEXT,
                 purchase_date TEXT,
                 warranty_period INTEGER,
                 status TEXT
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS usage (
                 id INTEGER PRIMARY KEY,
                 asset_id INTEGER,
                 cpu_usage REAL,
                 memory_usage REAL,
                 network_usage REAL,
                 timestamp TEXT,
                 FOREIGN KEY (asset_id) REFERENCES assets (id)
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS maintenance (
                 id INTEGER PRIMARY KEY,
                 asset_id INTEGER,
                 maintenance_date TEXT,
                 details TEXT,
                 cost REAL,
                 FOREIGN KEY (asset_id) REFERENCES assets (id)
                 )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
