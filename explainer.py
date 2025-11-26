# Step 1: Import necessary libraries
import requests  # Used to send data to the local Ollama API
import os  # Used to check if the file we want to explain actually exists

# Step 2: Define file path and read the content
filename = "sample_function.py"  # The name of the file we want to analyze

try:
    with open(filename, "r") as f:
        code_snippet = f.read()  # Read the entire content of the file into a variable
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit()  # Stop the script if we can't find the file
# Step 3 (Revised): Define model and specific instructor prompts
MODEL_NAME = "llama3"

SYSTEM_PROMPT = (
    "You are a Senior Software Instructor. Your job is to explain complex code "
    "in simple, non-technical terms suitable for a beginner. "
    "Provide a step-by-step breakdown of the code's goal and execution flow."
)

USER_PROMPT = (
    "Please analyze the following Python code and explain, line-by-line, "
    "exactly what it does, and what the overall function is. \n\n"
    f"```python\n{code_snippet}\n```"
)


# Step 4: Define function and prepare the data payload
def get_explanation():
    url = "http://localhost:11434/api/generate"
    # Combine model, system instruction, and user prompt into one package
    payload = {
        "model": MODEL_NAME,
        "system": SYSTEM_PROMPT,
        "prompt": USER_PROMPT,
        "stream": False,
    }

    # Step 5: Send request and return the response text
    try:
        response = requests.post(url, json=payload)  # Send data to local API
        return response.json()["response"]  # Extract only the text answer
    except Exception as e:
        return f"Connection Error: {e}"  # Handle cases where Ollama isn't running


# Step 6: Main execution block to run the script
if __name__ == "__main__":
    print(f"Analyzing {filename} with {MODEL_NAME}... (This may take a moment)")
    result = get_explanation()  # Call the function we just wrote
    print("\n--- AI Explanation ---\n")
    print(result)  # Print the AI's response to the terminal
