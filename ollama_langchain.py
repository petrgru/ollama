from langchain_community.llms import Ollama

def process_question():
    """
    Process a user's question using the Ollama language model.

    This function prompts the user for a question, invokes the Ollama language model
    to generate a response, and prints the response.

    Args:
        None

    Returns:
        None
    """

    # Prompt the user for a question
    user_question = input("What is your question? ")

    # Create an instance of the Ollama language model
    llm = Ollama(model="llama2")

    # Invoke the Ollama language model to generate a response
    response = llm.invoke(user_question)

    # Print the response
    print(response)


if __name__ == "__main__":
    process_question()
