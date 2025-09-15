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

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="apple/FastVLM-0.5B", trust_remote_code=True)
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)
