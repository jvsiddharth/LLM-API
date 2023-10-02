from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def generate_reply(input_text):
    # Load pre-trained model and tokenizer
    model_name = "gpt2"  # You can use other models as well (e.g., "gpt2-medium", "distilgpt2", etc.)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Encode input text and generate response
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    
    # Decode and return response
    reply = tokenizer.decode(output[0], skip_special_tokens=True)
    return reply

if __name__ == "__main__":
    input_text = input("Enter a message: ")
    reply = generate_reply(input_text)
    print("Bot:", reply)
