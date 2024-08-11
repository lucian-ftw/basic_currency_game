from typing import Dict, Any
import json


def load_data() -> Dict[str, Any]:
	"""Loads data from data.json file."""
	with open("data.json", "r") as file:
		return json.load(file)


def save_data(data: Dict[str, Any]) -> None:
	"""Writes the provided data to data.json file."""
	with open("data.json", "w") as file:
		json.dump(data, file, indent=4)