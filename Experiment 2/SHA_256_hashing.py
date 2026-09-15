import hashlib

filename = "Experiment 2/Sample.txt"
sha256_hash = hashlib.sha256()

with open(filename, "rb") as file:
    while chunk := file.read(4096):
        sha256_hash.update(chunk)

print("Filename    :", filename)
print("SHA-256 Hash:", sha256_hash.hexdigest())



text="hello"
digest=hashlib.sha256(text.encode()).hexdigest()
print(text)
print(f"sha 256 digest:{digest}")