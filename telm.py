import json,os,random
from datetime import datetime


os.makedirs("telemetry_date",exist_ok=True)

for i in range(1000000):
    records={
        "device_id":f"device_id{random.randint(1,9)}",
        "timestamp":datetime.utcnow().isoformat(),
        "temperature":round(random.uniform(20, 80), 2),
        "status":random.choice(["OK","FAILURE","WARNING"])
    }
    with open(f"telemetry_date/data_{i}.json","w") as f:
        json.dump(records,f)