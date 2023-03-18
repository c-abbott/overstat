import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

class OWLAPI:
    def __init__(self) -> None:
        self.access_token: str = os.getenv("ACCESS_TOKEN")
        self.headers: Dict[str, str] = {
            "Authorization": f"Bearer {self.access_token}",
        }
        self.owl_api_url: str = "https://us.api.blizzard.com/owl/v1/owl2"

    def fetch_owl_data(self) -> Dict[str, Any]:
        response = requests.get(self.owl_api_url, headers=self.headers)

        if response.status_code == 200:
            try:
                owl_data = response.json()
                return owl_data
            except Exception as e:
                print(f"Error parsing JSON: {e}")
                print(f"Response content: {response.text}")
        else:
            print(f"API request failed with status code {response.status_code}")
            print(f"Response content: {response.text}")

# Usage:
owl_api = OWLAPI()
owl_data = owl_api.fetch_owl_data()
print(owl_data)
