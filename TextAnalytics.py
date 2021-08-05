#Spelling Correction
from textblob import TextBlob
words = ["Artifisial intelligence","Computor Visione", "Data Sciense", "Machyne Learnin"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Spelling Correction:")
print("Entered words :", words)
print("\nCorrected Words are :")
for i in corrected_words:
    print(i.correct(), end="\n")
    
# Sentiment Analysis
from textblob.sentiments import NaiveBayesAnalyzer
import nltk

text          = "Have a great day!" 
sent          = TextBlob(text) 
polarity      = sent.sentiment.polarity #The polarity score is a float within the range [-1.0, 1.0] # where negative value = negative text and positive value = positive text.
subjectivity  = sent.sentiment.subjectivity #The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
sent          = TextBlob(text, analyzer = NaiveBayesAnalyzer())
classification= sent.sentiment.classification
positive      = sent.sentiment.p_pos
negative      = sent.sentiment.p_neg
print("\nSentence:", text)
if positive > negative:
    print("Overall Sentiment of the sentence is Positve")
elif positive<negative:
    print("Overall Sentiment of the sentence is Negative")
else:
    print("Overall Sentiment of the sentence is Neutral")
#print(polarity,subjectivity,classification,positive,negative)

#Tokenization
text = TextBlob("I played yesterday. "
               "I am playing today. "
                "I will play tomorrow.")
print("\nTokenzation words:", text.words)
print("Tokenization sentences:", text.sentences)
print("Sample word:",text.words[0])
print("Singular:",text.words[0].singularize())
print("Plural:",text.words[0].pluralize())

#Lemmatization
from textblob import TextBlob,Word
text =Word("Trusting")
print("Lemmatization of",text, "is", text.lemmatize("v")) #v- Verb; a- Adjective; n- Noun; r-Adverb 

sentence="you are playing better than me"
text=sentence.split(" ")
print(text)
print([Word(word).lemmatize() for word in text])
print([Word(word).lemmatize("v") for word in text])

#Language detection
text = TextBlob("Buongiorno!") #Italian to English
print(text.detect_language())
print(text.translate(to='en'))
print(text.translate(to='fr')) #Italian to French

#Word Count

#Categorization

#Synonyms