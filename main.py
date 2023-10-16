import json

# Your JSON data
json_data = '''
{
    "id": "10c77f40-6104-42b9-83f9-9c476651f599",
    "output": {
        "box": [],
        "score": [],
        "output": [],
        "data_type": "image_base64",
        "additional": []
    },
    "status": "COMPLETED",
    "delayTime": 9692,
    "executionTime": 2165
}
'''

# Parse the JSON data
data = json.loads(json_data)

# Access specific values
output = data["output"]
status = data["status"]

print("Output:", output)
print("Status:", status)
