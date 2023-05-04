import requests

query = "what is a frog?"

r = requests.get("https://api.duckduckgo.com",
    params = {
        "q": query,
        "format": "json"
    })

data = r.json()

print(data)

print("Abstract")
print(data["Abstract"])