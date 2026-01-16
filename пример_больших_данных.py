import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import csv

# Генерация 1 миллиона записей
np.random.seed(42)
n_records = 1_000_000

# Временные метки (каждую секунду в течение 11.5 дней)
start_time = datetime(2024, 1, 1, 0, 0, 0)
timestamps = [start_time + timedelta(seconds=i) for i in range(n_records)]

# Генерация данных
device_ids = [f"sensor_{i:03d}" for i in np.random.randint(1, 1001, n_records)]
temperatures = np.random.normal(23, 3, n_records).round(1)
humidities = np.random.normal(65, 5, n_records).round(1)
pressures = np.random.normal(1013.25, 0.2, n_records).round(2)
locations = np.random.choice(['zone_a', 'zone_b', 'zone_c', 'zone_d', 'zone_e'], n_records)
statuses = np.random.choice(['active', 'warning', 'error'], n_records, p=[0.95, 0.04, 0.01])

# Создание DataFrame
df = pd.DataFrame({
    'timestamp': timestamps,
    'device_id': device_ids,
    'temperature': temperatures,
    'humidity': humidities,
    'pressure': pressures,
    'location': locations,
    'status': statuses
})

# Сохранение в CSV (разделим на части для удобства)
df.to_csv('big_data_example.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

print(f"Файл создан: {len(df)} записей, ~{df.memory_usage().sum() / 1024 / 1024:.1f} МБ")
print("Пример первых 5 строк:")
print(df.head())
