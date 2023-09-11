import os
import json
from pinatapy import PinataPy

with open("config.json", "r") as f:
    config = json.load(f)

logs = []

client = PinataPy(
    config["api_key"],
    config["secret"]
)

for file in os.listdir(config["input"]):
    print(f"Uploading {file}...")
    response = client.pin_file_to_ipfs(f"{config['input']}/{file}")
    print(f"added {file}")
    logs.append(f"ipfs://{response['Ipfshash']}/{file}")

with open("output.json", "w") as f:
    json.dump(logs, f, indent=3)
print("Done!")