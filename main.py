from openrouter import OpenRouter
import os

api_key = os.getenv("OPEN_ROUTER_KEY")
print(f"API Key set: {api_key is not None}")  # Debug

with OpenRouter(api_key=api_key) as client:
    response = client.chat.send(
        model="tencent/hy3:free",
        messages=[
            {
                "role": "user",
                "content": "Explain what a Python virtual environment is, in one paragraph, to a Node.js developer.",
            }
        ],
    )

    print(response.choices[0].message.content)
    if response and hasattr(response, "choices"):
        print(response.choices[0].message.content)
    else:
        print("ERROR: Unexpected response structure")
