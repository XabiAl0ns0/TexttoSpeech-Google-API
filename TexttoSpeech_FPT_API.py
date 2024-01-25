import requests

url = 'https://api.fpt.ai/hmi/tts/v5'

# Your API key from FPT
api_key = 'Please fill API key from FPT'

# Text you want to convert to speech
text_to_speech = 'xin chào, công ty phương trang buslines'

headers = {
    'api-key': api_key,
    'voice': 'banmai',
}

# Payload with the text you want to convert
payload = {'text': text_to_speech}

# Making a POST request to the FPT TTS API
response = requests.post(url, data=payload, headers=headers)

# Checking the response
if response.status_code == 200:
    # If successful, you can save the audio or play it as needed
    with open('output.mp3', 'wb') as audio_file:
        audio_file.write(response.content)
    print('Speech conversion successful. Audio saved as output.mp3')
else:
    print(f'Error {response.status_code}: {response.text}')

print(response.status_code)
print(response.text)
