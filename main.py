import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

image_base64 = encode_image("./images/Screenshot 2024-11-27 at 1.57.05 PM.png")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("KEY")}'

}
payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            'role': 'system',
            'content': [
                {
                    'type': 'text',
                    'text': 'You are a hashtag generation model. When you get an image as input, your response should always contain exactly 50 hashtags separated by commas.'
                }
            ]
        },
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': 'Provide the hashtags for this image:'
                },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': f'data:image/png;base64,{image_base64}'
                    }
                }
            ]
        }

    ],
    "max_tokens": 500
}

response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
print(response.json()['choices'][0]['message']['content'].split(','))