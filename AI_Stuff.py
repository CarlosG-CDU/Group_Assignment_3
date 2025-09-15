
#****************
#Sentiment Model
#*************

#https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

#modified example AI sentiment. Lined with GUI
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


