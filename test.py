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
