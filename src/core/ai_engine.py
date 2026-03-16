from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

class AICore:
    def __init__(self, model_name="gpt2"):
        self.model_name = model_name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Initialize the model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)
        
        # Initialize text generation pipeline
        self.text_generator = pipeline("text-generation", model=model_name, device=0 if torch.cuda.is_available() else -1)

    def generate_response(self, prompt, max_length=100, temperature=0.7):
        """Generate AI response based on user prompt"""
        try:
            response = self.text_generator(prompt, max_length=max_length, temperature=temperature, num_return_sequences=1)
            return response[0]['generated_text']
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def answer_question(self, question, context=""):
        """Answer a question based on context"""
        full_prompt = f"{context}\nQuestion: {question}\nAnswer:"
        return self.generate_response(full_prompt, max_length=150)

    def summarize_text(self, text, max_length=100):
        """Summarize text using the model"""
        prompt = f"Summarize this: {text}\n\nSummary:"
        return self.generate_response(prompt, max_length=max_length)