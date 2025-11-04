import requests

# AWS Elastic Beanstalk endpoint
BASE_URL = "http://ece444pra5-env.eba-ax2ejuz9.ca-central-1.elasticbeanstalk.com/predict"

# Define test cases (2 fake, 2 real)
test_cases = {
    "real_1": "It is 2025 this year",
    "real_2": "Canada is next to the United States",
    "fake_1": "The sky is falling",
    "fake_2": "The world is made of cheese",
}

print("=== FUNCTIONAL TEST RESULTS ===\n")

for name, text in test_cases.items():
    response = requests.post(BASE_URL, json={"message": text})
    print(f"--- {name} ---")
    print("Input:", text)
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except Exception:
        print("Invalid JSON Response:", response.text)
    print()
