# Censure Userbot 

A Pyrogram userbot for censoring messages. Replaces profanity and offensive words in user's messages with "#" symbols.

## Installation

This guide will walk you through installing and running the Pyrogram-based censorship userbot.

**Prerequisites:**

•   Python 3.7 or higher is required.
•   A Telegram account.
•   Basic familiarity with the command line.

**Steps:**

1.  **Install Pyrogram:**

    Pyrogram is the Telegram client library that this userbot relies on. Use pip to install it:

    bash```
    pip install pyrogram
    ```

    If you encounter issues with this command, make sure you have pip installed correctly. You might need to use pip3 instead of pip depending on your system configuration.

2. **Clone the Repository**:

    Clone this repository to your local machine using Git:
    bash```
    git clone git@github.com:CheStorrr/censure_userbot.git && cd censure_userbot
    ```
 
3. **Configure Environment Variables** (Important):

  This userbot requires you to set environment variables for your Telegram API credentials and possibly other configuration options. The most common method is to create a .env file in the root directory of the project:

  •  **Create .env File**:

    Create a file named .env in the same directory as your userbot.py (or whatever your main file is named).

    ```env
    api_id=YOUR_TELEGRAM_API_ID
    api_hash=YOUR_TELEGRAM_API_HASH
    password=YOUR_PASSWORD (optional)
    phone_number=YOUR_PHONE_NUMBER 

    ```

 •  Install python-dotenv: (If using a .env file)

    If you are loading the environment variables from a .env file you must install the python-dotenv package:

    ```bash 
    pip install python-dotenv
    ```




4. Run the Userbot:

  Run the userbot using the following command from the root directory of the project:

  
```bash 
python -m userbot
```
