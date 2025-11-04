import requests
import time
import csv
import statistics
import matplotlib.pyplot as plt

# AWS Elastic Beanstalk endpoint
BASE_URL = "http://ece444pra5-env.eba-ax2ejuz9.ca-central-1.elasticbeanstalk.com/predict"

# Test inputs
test_cases = {
    "real_1": "It is 2025 this year",
    "real_2": "Canada is next to the United States",
    "fake_1": "The sky is falling",
    "fake_2": "The world is made of cheese",
}

N = 100  # number of API calls per test

print("=== PERFORMANCE TEST START ===\n")

for name, text in test_cases.items():
    latencies = []
    print(f"Testing case: {name}")

    for i in range(N):
        start = time.time()
        response = requests.post(BASE_URL, json={"message": text})
        end = time.time()
        latency = end - start
        latencies.append(latency)
        print(f"  Call {i+1}/{N}: {latency:.4f}s (status {response.status_code})")

    # Save results to CSV
    csv_filename = f"{name}_latency.csv"
    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["call_number", "latency_seconds"])
        for i, t in enumerate(latencies, start=1):
            writer.writerow([i, t])
    print(f"Saved {csv_filename} ({len(latencies)} rows)")

    # Print summary stats
    avg_latency = statistics.mean(latencies)
    print(f"Average latency for {name}: {avg_latency:.4f}s\n")

    # Generate boxplot
    plt.figure()
    plt.boxplot(latencies, vert=True)
    plt.title(f"Latency Distribution: {name}")
    plt.ylabel("Seconds")
    plt.savefig(f"{name}_boxplot.png")
    plt.close()

print("\n=== PERFORMANCE TEST COMPLETE ===")
