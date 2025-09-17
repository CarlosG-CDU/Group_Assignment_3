#****************
#Sentiment Model
#*************

#https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

#modified example AI sentiment. Alined with GUI
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

#inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
#with torch.no_grad():
#    logits = model(**inputs).logits

#predicted_class_id = logits.argmax().item()
#model.config.id2label[predicted_class_id]
#print(model.config.id2label[predicted_class_id])

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
