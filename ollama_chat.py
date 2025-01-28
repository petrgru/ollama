import json
import requests

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "deepseek-r1:14b"  # TODO: update this for whatever model you wish to use


def chat(messages):
    """
    Sends a chat request to the specified API endpoint and returns the response message.

    Args:
        messages (list): A list of messages to send in the chat.

    Returns:
        dict: The response message received from the API.

    Raises:
        Exception: If an error occurs during the chat request.

    """
    r = requests.post(
        "http://192.168.22.131:7869/api/chat",
        json={
            "model": model,
            "messages": messages,
            "options": {
                "temperature": 0.7,
                "max_tokens": 500,
                "stream": True }  # Vracet streaming odpovědi?
            }
    )
    r.raise_for_status()
    output = ""

    # iterate over the response stream
    for line in r.iter_lines():
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])

        # if the response is not done, add the content to the output
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            # the response streams one token at a time, print that as we receive it
            print(content, end="", flush=True)

        # if the response is done, return the message
        if body.get("done", False):
            message["content"] = output
            return message


def main():
    """
    This function takes user input, adds it to a list of messages, and prints the chat history.
    """

    messages = []  # List to store the chat messages

    while True:
        user_input = input("Enter a prompt: ")  # Prompt the user for input

        if not user_input:  # If the user input is empty, exit the program
            exit()

        print()

        # Add user input to the messages list
        messages.append({"role": "user", "content": user_input})

        # Call the chat function to generate a response
        message = chat(messages)
        messages.append(message)  # Add the response to the messages list

        print("\n\n")  # Print new lines to separate chat history


if __name__ == "__main__":
    main()
