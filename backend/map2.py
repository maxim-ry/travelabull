import gemini

# def generate_summary(user_city, user_rate, user_type):
#   """Generates a concise and captivating summary of a location using the Gemini AI.

#   Args:
#     user_city: The name of the city to generate a summary for.
#     user_rate: The user's rating of the city (1-5).
#     user_type: The type of traveler the user is (e.g., "cultural enthusiast", "nature lover", etc.).

#   Returns:
#     A concise and captivating summary of the location.
#   """

#   # Define the prompt for the Gemini AI.
#   prompt = f"""Generate a concise and captivating summary of {user_city} for a {user_type} traveler.
#   Ensure the summary is 2-3 sentences long and aims to spark curiosity and make the visit memorable.
#   Include the city's rating: {user_rate} out of 5.
#   """

#   # Generate the summary using the Gemini AI.
#   response = gemini.generate(prompt=prompt)

#   # Extract the summary from the response.
#   summary = response.candidates[0].output

#   return summary


# # Example usage.
# location = "Tokyo"
# rating = 5
# type = "foodie"
# summary = generate_summary(location, rating, type)


def generate_summary(user_city, user_rate, user_type):
  """Generates a concise and captivating summary of a location using the Gemini AI.

  Args:
    user_city: The name of the city to generate a summary for.
    user_rate: The user's rating of the city (1-5).
    user_type: The type of traveler the user is (e.g., "cultural enthusiast", "nature lover", etc.).

  Returns:
    A concise and captivating summary of the location.
  """

  # Define the prompt for the Gemini AI.
  prompt = f"""Generate a concise and captivating summary of {user_city} for a {user_type} traveler.
  Ensure the summary is 2-3 sentences long and aims to spark curiosity and make the visit memorable.
  Include the city's rating: {user_rate} out of 5.
  """

  # Generate the summary using the Gemini AI.
  response = gemini.generate(prompt=prompt)

  # Extract the summary from the response.
  summary = response.candidates[0].output

  return summary



import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


##Set up KEYS. 

def get_api_key():
    # Assuming your API key is stored in a file named 'api_key.txt'
    api_key_file = '/Users/sultansamid/Documents/GitHub/allCodings/authMy.txt'  # Specify the path to your API key file
    with open(api_key_file, 'r') as file:
        return file.read().strip()


genai.configure(api_key=get_api_key())

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)



# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}


# Example prompt using f-strings for dynamic input:

def generate_summary(user_city, user_rate, user_type):
  """Generates a concise and captivating summary of a location.

  Args:
    user_city: The name of the city to generate a summary for.
    user_rate: The user's rating of the city (1-5).
    user_type: The type of traveler the user is (e.g., "cultural enthusiast", "nature lover", etc.).

  Returns:
    A concise and captivating summary of the location.
  """

  # Define the prompt for the AI assistant.
  prompt = f"""Generate a concise and captivating summary of {user_city} for a {user_type} traveler.
  Ensure the summary is 2-3 sentences long and aims to spark curiosity and make the visit memorable.
  Include the city's rating: {user_rate} out of 5.
  """


safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)



response = model.generate_content("What is the meaning of life?")
print(response)

