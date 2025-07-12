import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    print(user_prompt)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(20):
        # print(f"messages: {messages}")
        try:
            response = generate_content(client, messages, verbose)
            if not isinstance(response, str):
                messages = response
            else:
                print("Final Response:")
                print(response)
                break
        except OSError as e:
            raise Exception(f"Error: {e}")


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    for candidate in response.candidates:
        # print(f"Candidate: {candidate.content}")
        messages.append(candidate.content)
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        # print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        function_call_result = call_function(function_call_part, verbose)
        # print(f"func_call_result: {function_call_result}")
        if function_call_result.parts[0].function_response.response == "":
            raise Exception(f"Error: no response returned from function called")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        messages.append(function_call_result)
    return messages


if __name__ == "__main__":
    main()
