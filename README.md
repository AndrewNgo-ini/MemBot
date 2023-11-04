# MemBot

This Discord bot is designed to interact with users on Discord servers. It can learn from text inputs and provide answers based on previous interactions. The bot uses the `langchain` library for its language processing capabilities and FAISS for efficient similarity search in large databases.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1C5ke7wF_E-G92m2ccR3K75t-80rD9ESf?usp=sharing)

This repository contains a Colab notebook that demonstrates how to use the MemBot application. To open the notebook in your browser, click the "Open In Colab" button.


## Features

- **Learn**: The bot can learn from text inputs provided via the `/learn` command.
- **Ask**: Users can ask questions using the `/ask` command, and the bot will attempt to provide relevant answers based on what it has learned.

## Setup

Before running the bot, ensure you have the following prerequisites:

- Python 3.10 or higher
- A Discord Bot Token
- An OpenAI API Key

### Installation

1. Clone the repository:
2. Install the required dependencies:
```
pip install -r requirements.txt
```

### Configuration

1. Create a `.env` file in the root directory of your project.
2. Add your OpenAI API key and Discord Bot Token to the `.env` file:
 ```
 OPENAI_API_KEY=your_openai_api_key_here
 TOKEN=your_discord_bot_token_here
 ```

### Running the Bot

Execute the bot with the following command:
```
python main.py
```

The bot will create a new FAISS index on the first run if one doesn't exist.

### Commands

- `/learn [text]`: Teach the bot new information. Replace `[text]` with the content.
- `/ask [question]`: Ask the bot a question. Replace `[question]` with your query.

## Graceful Shutdown

The bot is configured to handle SIGINT (Ctrl+C) and SIGTERM signals to save the FAISS index state before exiting.

## Troubleshooting

If you encounter any issues, verify that all environment variables are correctly set and you have a working internet connection. Check the terminal's error messages for more information.

## Contributions

Feel free to fork the repository, make your improvements, and submit a pull request.

## License

This bot is released under the [MIT License](LICENSE).
