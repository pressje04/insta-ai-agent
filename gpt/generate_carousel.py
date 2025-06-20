import requests
import json

"""
Function to generate carousel slide content using Ollama (Mistral model).
Assumes Ollama is running locally at http://localhost:11434

:param problem_name: str - Name of the LeetCode problem
:return: list of dicts with 'title' and 'content' keys
"""
def generate_slides(problem_name: str):
    prompt = f"""
        You are a helpful assistant generating Instagram carousel slides.
        Break down the LeetCode problem "{problem_name}" into a JSON array of slides.

        Each slide should be an object with 'title' and 'content'.
        Include:
        - Brief problem description
        - Brute force approach
        - Optimal solution
        - Time and space complexity
        - Summary or call-to-action

        Make it engaging and beginner-friendly. Use clear language and emojis where helpful.

        Respond with ONLY the JSON array. Example:
        [
        {{ "title": "Slide 1", "content": "Explanation here" }},
        ...
        ]
    """

    print(f"🔁 Querying Ollama for '{problem_name}'...")
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama request failed: {response.text}")

    # Parse response
    raw_output = response.json()["response"]

    try:
        slides = json.loads(raw_output)
        assert isinstance(slides, list)
        return slides
    except Exception as e:
        print("❌ Failed to parse Ollama response.")
        print("Raw response:")
        print(raw_output)
        raise e
