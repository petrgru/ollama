from langchain_community.llms import Ollama


def process_question(user_question: str) -> str:
    """
    Process a user question using the Ollama language model.

    Args:
        user_question (str): The question asked by the user.

    Returns:
        str: The generated response from the Ollama language model.
    """
    # Create an instance of the Ollama language model
    llm = Ollama(model="llama2")

    # Invoke the Ollama language model to generate a response
    response = llm.invoke(user_question)

    return response


if __name__ == "__main__":
    # Prompt the user for a question
    user_question = input("What is your question? ")
    reponse = process_question(user_question=user_question)
    print(reponse)
