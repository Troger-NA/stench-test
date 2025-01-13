from flask import Flask, request, jsonify
from textblob import TextBlob
import random
import nltk
import os

# Descargar recursos de NLTK
nltk.download('brown')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Inicializar Flask
app = Flask(__name__)

# Lista de rimas categorizadas por sentimiento
rimas = {
    "positive": [
        "Quench your thirst with Aroma Coin's stench!",
        "Sweet as a peach, Aroma Coin's stench."
    ],
    "negative": [
        "Get drenched in gains despite the stench.",
        "Money wrenched from the market's stench."
    ],
    "neutral": [
        "Sitting on the bench, smelling Aroma Coin's stench.",
        "Digging deep in the crypto trench with Aroma Coin's stench."
    ]
}

def analizar_sentimiento(texto):
    """Analiza el sentimiento del texto proporcionado."""
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    if polaridad > 0.1:
        return 'positive'
    elif polaridad < -0.1:
        return 'negative'
    else:
        return 'neutral'

def extraer_contexto(texto):
    """Extrae frases clave del texto proporcionado."""
    blob = TextBlob(texto)
    frases_clave = blob.noun_phrases
    return ', '.join(frases_clave[:2]) if frases_clave else ''

def generar_respuesta_natural(contexto, sentimiento):
    """Genera una respuesta más natural basada en el contexto y el sentimiento."""
    preludios = {
        "positive": ["That's great to hear!", "What a positive vibe!"],
        "negative": ["Oh, that doesn't sound great.", "Seems tricky."],
        "neutral": ["Interesting point.", "That's quite neutral."]
    }
    preludio = random.choice(preludios.get(sentimiento, ["Let's explore that."]))
    rima = random.choice(rimas.get(sentimiento, ["Sorry, no rhyme found."]))
    if contexto:
        return f"{preludio} I noticed you're talking about {co
     
