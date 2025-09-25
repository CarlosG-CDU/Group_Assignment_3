
#****************
#Sentiment Model
#*************

#https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

#modified example AI sentiment. Alined with GUI


from base_classes import AiModelBase
import torch
import time
import functools
import sys, itertools, threading
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler

#local_model_path = "./models/distilbert-base-uncased-finetuned-sst-2-english"      #use thisline for local model
#tokenizer = DistilBertTokenizer.from_pretrained(local_model_path)                  #use thisline for local model
#model = DistilBertForSequenceClassification.from_pretrained(local_model_path)      #use thisline for local model

tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")                  #uncomment this line to use online
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")       #uncomment this line to use online

# Decorator: log with spinner while function is running
# Reference: https://realpython.com/primer-on-python-decorators/    https://docs.python.org/3/library/itertools.html#itertools.cycle
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        stop_flag = {"stop": False}
        spinner_cycle = itertools.cycle("/-\\|") #spinner characters

        def _spin():
            while not stop_flag["stop"]:
                print("LOG: working... " + next(spinner_cycle))
                time.sleep(0.3) 
        t = threading.Thread(target=_spin, daemon=True)
        t.start()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            stop_flag["stop"] = True
            t.join(timeout=0.5)
            print(f"LOG: finished function -> {func.__name__}")
    return wrapper


            
# Decorator: time how long it takes to complete function
# Reference:(https://www.geeksforgeeks.org/python/timing-functions-with-decorators-python/)
def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter() # swapped out instead of time.time()
        try:
            return func(*args, **kwargs)
        finally:
            dur = time.perf_counter() - start
            msg = f"TIME: {func.__name__} took {dur:.2f} seconds"
            print(msg, flush=True) #force it to print
            with open("debug.log", "a", encoding="utf-8") as f:
                f.write(msg + "\n")
    return wrapper

class SentimentModel(AiModelBase):
    def __init__(self):
        super().__init__("Sentiment Model")

    @log_call
    @timeit
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

    @log_call
    @timeit
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