import os
import argparse
from dotenv import load_dotenv
from google import genai 
from google.genai import types
from config import system_prompt
from config_functions import available_functions
from call_function import call_function

#Parsing arguments
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
v = args.verbose

#Setting up Gemini AI Client
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key: 
    raise RuntimeError("***ERROR: API_KEY=NONE***")
client = genai.Client(api_key=api_key)
model_name = "gemini-2.5-flash"

def generate_content():
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    func_results_list = []

    for reps in range(20):
        if func_results_list:
            messages.append(types.Content(role="user", parts=func_results_list))

        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
                ),
            )

        if response.candidates:
            for c in response.candidates:
                messages.append(c.content)

        if v:
            prompt_tokens = response.usage_metadata.prompt_token_count
            response_tokens = response.usage_metadata.candidates_token_count
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {prompt_tokens}")
            print(f"Response tokens: {response_tokens}")
        
        if response.function_calls:
            if response.function_calls:
                func_results_list = []
                for function_call in response.function_calls:
                    function_call_result = call_function(function_call, verbose=v)
                    if not function_call_result.parts:
                        raise Exception("Error: function_call_result.parts should be non-empty")
                    if not function_call_result.parts[0]:
                        raise Exception("Error: function_call_result.parts[0] should not be None")
                    if not function_call_result.parts[0].function_response.response:
                        raise Exception("Error: function_call_result.parts[0].function_response.response should not be None")
                    func_results_list.append(function_call_result.parts[0])
                    if v:
                        print(f"-> {function_call_result.parts[0].function_response.response}")

        else:
            print(response.text)
            return reps + 1


def main():
    cycles = generate_content()
    if cycles == 20:
        sys.exit("Error: Maximum iterations reached.")

if __name__ == "__main__":
    main()