from fastapi import FastAPI
import httpx
import uvicorn
import openai
import subprocess

app = FastAPI()

openai.api_key = ""

def launch_lean_server():
    # Command to launch Lean server
    command = ['lean', '--server']

    try:
        # Launch the Lean server as a subprocess
        server_process = subprocess.Popen(command)

        # Wait for the server process to finish
        server_process.wait()

    except FileNotFoundError:
        print("Lean executable not found. Make sure Lean is installed and added to the system path.")

launch_lean_server()

@app.post("/solve")
async def solve_problem(problem: str, answer: str) -> dict:
    # Envoie des données à ChatGPT via l'API OpenAI pour convertir en code Lean
    chatgpt_response = await convert_to_code(problem, answer)

    # Exécution du code Lean
    lean_response = execute_lean_code(chatgpt_response)

    # Demande à ChatGPT de générer une correction basée sur la réponse de Lean
    correction = await generate_correction(lean_response)

    # Impression de la réponse de ChatGPT
    print(correction)

    return {"message": "Traitement terminé"}

def convert_to_code(problem : str, answer : str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="is 2+2 =3",
        max_tokens=50  # Maximum length of the generated response
    )
    print(response)
    if "choices" in response:
        choices = response["choices"]
        if choices:
            generated_text = choices[0]["text"].strip()
            print(generated_text)
            return generated_text
        else:
            print("No response generated.")
    else:
        print("Unexpected response from OpenAI API.")
    return None


def execute_lean_code(chatgpt_response : str)-> str:
    


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
