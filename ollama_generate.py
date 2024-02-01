import ollama

result = ollama.generate(model='llama2', prompt='Why is the sky blue?')
print(result.get('response', ''))