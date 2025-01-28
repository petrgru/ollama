# Ollama Chat
this use for  connect to chat with chatbot our ollam system
how to use our system for communicate with vscode for better programing with our AI system without copilot

use codestral into vscode
next change connector to our ollama server 
'''
"models": [
    {
      "model": "AUTODETECT",
      "title": "Autodetect",
      "completionOptions": {},
      "apiBase": "https://openai-api.sspu-opava.cz",
      "provider": "ollama"
    }
  ],
'''

This Python script allows you to interact with the Ollama AI chat models.

## Requirements

- Python 3
- `requests` library
- `langchain-community` library
- `ollama` library
- Ollama app. You can download it from [here](https://ollama.ai/download)
- Ollama model. You can download it from [here](https://ollama.ai/library)

## Usage

Ensure that the Ollama app is running. You can start it with the `ollama serve` command.
brew
Then, run the script with:

```bash
python ollama_chat.py
python ollama_langchain.py
python ollama_generate.py
```

## Additional Resources

For more information, you can check out the Ollama project on [GitHub](https://github.com/jmorganca/ollama).
