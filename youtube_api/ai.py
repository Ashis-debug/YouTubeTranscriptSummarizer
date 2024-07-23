# ai.py
import google.generativeai as genai


def generate_summary(prompt, message):
    model = genai.GenerativeModel('gemini-1.5-flash')
    """
    Generate summary or questions using Generative AI.
    """
    response = model.generate_content(prompt + "\n" + message)
    return response.text
