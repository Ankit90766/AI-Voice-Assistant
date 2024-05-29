# AI Voice Assistant

This is a simple AI Voice Assistant built with Python. It can perform various tasks like searching on Wikipedia, opening websites, playing music, and sending emails.

## Features

- Greet the user based on the time of day
- Listen to voice commands
- Search Wikipedia for a query
- Open popular websites (YouTube, Google, StackOverflow)
- Play music from a specified directory
- Tell the current time
- Open a code editor
- Send an email to a specified address

## Requirements

- Python 3.x
- pyttsx3
- SpeechRecognition
- wikipedia
- webbrowser
- smtplib

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/<your-username>/AI-Voice-Assistant.git
    ```

2. Install the required packages:
    ```sh
    pip install pyttsx3 SpeechRecognition wikipedia
    ```

3. Update the `sendEmail` function with your email credentials.

## Usage

Run the script:
```sh
python your_script_name.py
