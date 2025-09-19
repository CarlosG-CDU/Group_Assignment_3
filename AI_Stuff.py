
#****************
#Sentiment Model
#*************

#https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

#modified example AI sentiment. Alined with GUI


from base_classes import AiModelBase
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler

#local_model_path = "./models/distilbert-base-uncased-finetuned-sst-2-english"      #use thisline for local model
#tokenizer = DistilBertTokenizer.from_pretrained(local_model_path)                  #use thisline for local model
#model = DistilBertForSequenceClassification.from_pretrained(local_model_path)      #use thisline for local model

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")                  #uncomment this line to use online
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")       #uncomment this line to use online

class SentimentModel(AiModelBase):
    def __init__(self):
        super().__init__("Sentiment Model")

    def run(self, input_text):
        inputs = tokenizer(input_text, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
        predicted_class_id = logits.argmax().item()
        sentiment = model.config.id2label[predicted_class_id]
        print(model.config.id2label[predicted_class_id])
        return f"Sentiment: {sentiment}"



###**************************************
#  Text to Picture Model. Modified for our needs
#***********************

#import torch
#from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler


class TextToImageModel(AiModelBase):
    def __init__(self):
        super().__init__("Text to Image")

    def run(self, input_text):
        pipe = DiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32,
            safety_checker=None
        )
        pipe = pipe.to("cpu")
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

        image = pipe(input_text, num_inference_steps=25, height=256, width=256).images[0]
        image.save("output.png")
        return "image saved as output.png"
