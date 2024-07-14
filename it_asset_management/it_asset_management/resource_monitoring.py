import sqlite3
import random
from datetime import datetime

def add_usage_data(asset_id):
    conn = sqlite3.connect('it_assets.db')
    c = conn.cursor()

    cpu_usage = random.uniform(0, 100)
    memory_usage = random.uniform(0, 100)
    network_usage = random.uniform(0, 100)

    c.execute("INSERT INTO usage (asset_id, cpu_usage, memory_usage, network_usage, timestamp) VALUES (?, ?, ?, ?, ?)",
              (asset_id, cpu_usage, memory_usage, network_usage, str(datetime.now())))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    add_usage_data(1)
