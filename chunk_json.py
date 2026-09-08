import json

with open("chunks.json", "r") as f:
    data = json.load(f)

chunk_size_len = len(data)
chunk_count = 0

for i in range(0, len(data), chunk_size):
    chunk_count += 1
    with open(f"chunk_{chunk_count}.json", "w") as f:
        for record in data[i:i+chunk_size]:
            json.dump(record, f)
            f.write("\n")
#print(len())

print("Chunked files created.")
