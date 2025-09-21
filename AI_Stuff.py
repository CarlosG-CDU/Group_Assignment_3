
#****************
#Sentiment Model
#*************

#https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

#modified example AI sentiment. Alined with GUI

import torch
import time
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

local_model_path = "./models/distilbert-base-uncased-finetuned-sst-2-english"

#tokenizer = DistilBertTokenizer.from_pretrained(local_model_path)
#model = DistilBertForSequenceClassification.from_pretrained(local_model_path)
#***************************************
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")     #uncomment this line to use online
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")     #uncomment this line to use online
#***************************************
#inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
#with torch.no_grad():
#    logits = model(**inputs).logits

#predicted_class_id = logits.argmax().item()
#model.config.id2label[predicted_class_id]
#print(model.config.id2label[predicted_class_id])

# Decorator: log when a function is called
# Reference:(https://www.geeksforgeeks.org/python/timing-functions-with-decorators-python/)
def log_call(func):
    def wrapper(*args, **kwargs):
        print("LOG: running function ->", func.__name__)
        result = func(*args, **kwargs)
        print("LOG: finished function ->", func.__name__)
        return result
    return wrapper

# Decorator: time how long it takes to complete function

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter() # swapped out instead of time.time()
        try:
            return func(*args, **kwargs)
        finally:
            dur = time.perf_counter() - start
            msg = f"TIME: {func.__name__} took {dur:.2f} seconds"
            print(msg, flush=true) #force it to print
            with open("debug.log", "a", encoding="utf-8") as f:
                f.write(msg + "\n")
    return wrapper

@log_call
@timeit
def analyse_sentiment(input_text):
    print("Analysing this from AI_Stuff: ", input_text) #remove later

    inputs = tokenizer(input_text, return_tensors = "pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    sentiment = model.config.id2label[predicted_class_id]
    print(model.config.id2label[predicted_class_id])
    return sentiment


###**************************************
#  Text to Picture Model. Modified for our needs
#***********************

import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler

@log_call
@timeit
def text_to_image(input_text):
    print("This is the text from GUI.py: ", input_text)

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
    #prompt = "One red lady bug on a green leaf background"
    prompt = input_text

    image = pipe(prompt, num_inference_steps=25, height=256, width=256).images[0]
    # Save the image
    image.save("output.png")
    print("Image saved as output.png")
    print(f"Generated with prompt: '{prompt}' and {image.size} resolution.")
    savedTo = f"{prompt}_{image.size}"  #string to be passed
    return savedTo
