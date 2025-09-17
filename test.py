'''
from transformers import pipeline
classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
#text = "I love using transformers. The best part is wide range of support and its easy to use""
text = "I love to hate the rain. its wet"
prediction = classifier(text,top_k = None )
#print(prediction)
print(f"Text: {text}")
print("Emotion Prodiction: ")
for emotion in prediction:
    print(f"  - {emotion['label'].capitalize()}: {emotion['score']:.4f}")

'''
'''
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
res = nlp(question='Why is model conversion important?', 
          context='The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.')

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Print the result
print(res)
'''
'''
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="apple/FastVLM-0.5B", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)
'''
'''
from transformers import pipeline

toxic_model = pipeline("text-classification", model="unitary/toxic-bert")

def detect_toxicity(input_text):
    result = toxic_model(input_text)
    return f"{result[0]['label']} ({result[0]['score']:.2f})"
'''
'''
# toxic_test.py

from transformers import pipeline

# Load the model
toxic_model = pipeline("text-classification", model="unitary/toxic-bert")

def detect_toxicity(input_text):
    result = toxic_model(input_text)
    return f"{result[0]['label']} ({result[0]['score']:.2f})"

if __name__ == "__main__":
    # Example test inputs
    test_sentences = [
        "I love this product, it’s amazing!",
        "You are so stupid and annoying.",
        "I love that you are a flower that slowly wiltering"
    ]
    
    for sentence in test_sentences:
        print(f"Input: {sentence}")
        print("Result:", detect_toxicity(sentence))
        print("-" * 40)

'''

'''
# emotion_test.py

from transformers import pipeline

# Load the model
emotion_model = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)

def analyse_emotion(input_text):
    result = emotion_model(input_text)
    return f"{result[0]['label']} ({result[0]['score']:.2f})"

if __name__ == "__main__":
    # Example test inputs
    test_sentences = [
        "I am feeling great today!",
        "This is the worst day ever.",
        "I’m really anxious about tomorrow."
    ]
    
    for sentence in test_sentences:
        print(f"Input: {sentence}")
        print("Result:", analyse_emotion(sentence))
        print("-" * 40)
'''
'''
import torch
from diffusers import DiffusionPipeline

# Load the model without the NSFW safety checker
model_id = "runwayml/stable-diffusion-v1-5"  # Or "distil-diffusion/2" for the lighter version
pipe = DiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float32,
    safety_checker=None  # This disables the NSFW filter
)
pipe = pipe.to("cpu")  # Ensure CPU usage

# Generate an image
prompt = "A cute cartoon cat wearing a red hat, simple illustration"  # Your prompt
image = pipe(
    prompt, 
    num_inference_steps=30,  # Low steps for speed (adjust if needed)
    height=256, 
    width=256,  # Low-res for CPU
    generator=torch.Generator("cpu").manual_seed(42)  # Fixed seed for reproducibility (optional)
).images[0]

# Save the image
image.save("output.png")
print("Image saved as output.png")
'''

import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler

# Load the model without the NSFW safety checker
model_id = "runwayml/stable-diffusion-v1-5"  # Stick with this for now; switch to "distil-diffusion/2" if too slow
pipe = DiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float32,
    safety_checker=None  # Disables NSFW filter
)
pipe = pipe.to("cpu")  # Ensure CPU usage

# Switch to a better scheduler for coherent images with fewer steps
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Generate an image with improved settings
#prompt = "A simple wooden house on a green hill, landscape, clear blue sky, daytime"  # More detailed for better results
#prompt = "A cow standing on a green field, clear blue sky, daytime"
#prompt = "A bee on a yellow flower, clear blue sky, daytime"
#prompt = "A rainbow umbrella infront of a rain background"
prompt = "One red lady bug on a green leaf background"

image = pipe(prompt, num_inference_steps=25, height=256, width=256).images[0]
'''
negative_prompt = "blurry, noisy, abstract, deformed"  # Helps avoid messiness (optional but recommended)
image = pipe(
    prompt, 
    negative_prompt=negative_prompt,
    num_inference_steps=25,  # Increased for coherence (try 20 if too slow, 50 for max quality)
    height=256, 
    width=256,  # Low-res for CPU
    guidance_scale=7.5,  # Standard value for prompt adherence
    generator=torch.Generator("cpu").manual_seed(123)  # Different seed for variety; change to 42 or remove for random
).images[0]
'''
# Save the image
image.save("output.png")
print("Image saved as output.png")
print(f"Generated with prompt: '{prompt}' and {image.size} resolution.")


