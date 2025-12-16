import requests
import json

def test_backend_api():
    """Test the deployed backend API to ensure it's working correctly."""
    url = "https://giaic-hackathon-book-rag-2025-production.up.railway.app/api/chat"

    # Test message
    test_message = {"message": "What is humanoid robotics?"}

    try:
        print("Testing the deployed backend API...")
        print(f"Sending request to: {url}")
        print(f"Message: {test_message['message']}")

        response = requests.post(
            url,
            json=test_message,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        print(f"Response status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"Response: {data.get('response', 'No response field')[:100]}...")
            print(f"Sources: {data.get('sources', [])}")
            print("\n[SUCCESS] Backend API test successful!")
        else:
            print(f"[ERROR] Backend API test failed with status {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Error testing backend API: {e}")

if __name__ == "__main__":
    test_backend_api()