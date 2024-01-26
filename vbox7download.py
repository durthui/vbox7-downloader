import re
import requests
import subprocess

def download(src, title):
    # Construct the ffmpeg command
    command = [
        './ffmpeg.exe', '-i', src, '-c', 'copy', '-bsf:a', 'aac_adtstoasc', f'{title}.mp4'
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Downloaded and saved as '{title}.mp4'")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def extract_video_id(url):
    # Regular expression pattern to match the required URL format and extract video ID
    pattern = r'https://www\.vbox7\.com/play:([a-zA-Z0-9]+)'
    match = re.match(pattern, url)
    if match:
        return match.group(1)
    else:
        return None


import subprocess
import re

def sanitize_filename(title):
    # Regex pattern to match most common emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese characters
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U0001F1F2-\U0001F1F4"  # Macau flag
                               u"\U0001F1E6-\U0001F1FF"  # flags
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1F2-\U0001F1F4"
                               u"\U0001F1E6-\U0001F1FF"
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F1F2-\U0001F1F4"
                               u"\U0001F1E6-\U0001F1FF"
                               "]+", flags=re.UNICODE)

    # Remove emojis
    title = emoji_pattern.sub(r'', title)

    # Remove specific special characters
    title = re.sub(r'[\\\/?!@#$%^&*|]', '', title)


    # Truncate the title if it's too long for a filename
    max_length = 240
    return title[:max_length]

def download(src, title):
    sanitized_title = sanitize_filename(title)

    command = [
        './ffmpeg.exe', '-i', src, '-c', 'copy', '-bsf:a', 'aac_adtstoasc', f'{sanitized_title}.mp4'
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Downloaded and saved as '{sanitized_title}.mp4'")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# rest of your script...


def download(src, title):
    sanitized_title = sanitize_filename(title)

    command = [
        './ffmpeg.exe', '-i', src, '-c', 'copy', '-bsf:a', 'aac_adtstoasc', f'{sanitized_title}.mp4'
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Downloaded and saved as '{sanitized_title}.mp4'")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def fetch_video_info(video_id):
    api_url = f'https://www.vbox7.com/aj/player/video/options?vid={video_id}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        options = data.get('options', {})

        src = options.get('src')
        title = options.get('title')

        if title:
            try:
                # Attempt to decode directly from UTF-8
                title = title.encode('utf-8').decode('utf-8')
            except UnicodeDecodeError:
                # In case of decode error, use the original string
                pass

        if src:
          
        else:
            print("Source not found.")

        print(f"Title: {title}")
    else:
        print("Failed to fetch video information.")
    download(src, title)

def main():
    url = input("Enter the vbox7 video URL: ")
    video_id = extract_video_id(url)

    if video_id:
        fetch_video_info(video_id)
    else:
        print("Invalid URL format. Please enter a valid vbox7 video URL.")


if __name__ == "__main__":
    main()
