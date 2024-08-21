import os
import requests
from pydub import AudioSegment

def download_and_convert_audio(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Extract the file name from the URL and set the output path
        original_file_name = os.path.basename(url)
        temp_file_path = f"temp_{original_file_name}"
        output_file_name = os.path.splitext(original_file_name)[0] + ".wav"
        
        # Download the audio file
        with open(temp_file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        # Convert to WAV format using pydub
        audio = AudioSegment.from_file(temp_file_path)
        audio.export(output_file_name, format="wav")
        
        # Remove the temporary file
        os.remove(temp_file_path)
        
        print(f"Audio downloaded and converted to WAV successfully and saved as {output_file_name}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Replace 'Paste Url Here' with the actual URL of the audio file
audio_url = "Paste Url Here"

download_and_convert_audio(audio_url)
