# Simple Kiswahili <-> English Translator

translator = {
    "hello": "habari",
    "hi": "habari",
    "good morning": "habari ya asubuhi",
    "good night": "usiku mwema",
    "thank you": "asante",
    "please": "tafadhali",
    "sorry": "samahani",
    "friend": "rafiki",
    "girl": "nyako",
    "boy": "mvulana",
    "man": "mwanaume",
    "woman": "mwanamke",
    "water": "maji",
    "food": "chakula",
    "house": "nyumba",
    "school": "shule",
    "teacher": "mwalimu",
    "student": "mwanafunzi",
    "love": "upendo",
    "I": "mimi",
    "you": "wewe",
    "my": "yangu",
    "name": "jina",
    "what": "nini",
    "where": "wapi",
    "how": "vipi"
}

# Create reverse dictionary (Swahili -> English)
reverse_translator = {value: key for key, value in translator.items()}


def translate(sentence):
    words = sentence.lower().split()
    result = []

    for word in words:
        if word in translator:
            result.append(translator[word])
        elif word in reverse_translator:
            result.append(reverse_translator[word])
        else:
            result.append(word)

    return " ".join(result)


print("Welcome to Swahili-English Translator")
print("Type 'exit' to close")

while True:
    text = input("\nEnter word/sentence: ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    print("Translation:", translate(text))