import requests

# Replace 'YOUR_GOOGLE_API_KEY' with your actual API key
api_key = 'YOUR_GOOGLE_API_KEY'
url = 'https://texttospeech.googleapis.com/v1/text:synthesize'

# Your Google Cloud Project ID
project_id = 'your-project-id'

# Text you want to convert to speech
text_to_speech = 'If the downloaded MP3 file is not working as expected, there could be a few reasons for this. Here are some troubleshooting steps you can take.'

headers = {
    'Content-Type': 'application/json',
}

# Payload with the text you want to convert
payload = {
    'input': {
        'text': text_to_speech
    },
    'voice': {
        'languageCode': 'en-US',
        'name': 'en-US-Wavenet-D',
        'ssmlGender': 'NEUTRAL',
    },
    'audioConfig': {
        'audioEncoding': 'MP3',
    },
}

# Making a POST request to the Google TTS API with API key in URL parameters
response = requests.post(
    url,
    json=payload,
    headers=headers,
    params={'key': api_key},
)

# Checking the response
if response.status_code == 200:
    # If successful, you can save the audio or play it as needed
    with open('output.mp3', 'wb') as audio_file:
        audio_file.write(response.content)
    print('Speech conversion successful. Audio saved as output.mp3')
else:
    print(f'Error {response.status_code}: {response.text}')


