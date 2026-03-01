import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hey there, my name is harsh saxena"

tokens = enc.encode(text)
print("tokens, ", tokens)

decoded_tokens = enc.decode(tokens)
print("decoded tokens, ", decoded_tokens)