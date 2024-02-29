from openai import OpenAI
import os

# Assuming OpenAI is initialized elsewhere or as shown:
client = OpenAI(api_key='API_KEY_HERE')

def get_summaries(cities):
    summaries = []
    for city in cities:
        prompt = f"Generate a concise and captivating summary of {city}. Do not exceed 2-3 sentences."
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Adjust the model as needed
            prompt=prompt,
            temperature=0.7,
            max_tokens=100,
            n=1
        )
        summary = response.choices[0].text.strip()
        summaries.append(summary)
    return summaries

def get_location_descriptions(locations):
    descriptions = []
    for location in locations:
        prompt = f"Write a short, engaging description for the following location based on its name and address: {location['name']}, {location['address']}. Keep it concise and informative. Do not use quotations. Also add variation to the beginning, do not start with welcome each time."
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Adjust the model as needed
            prompt=prompt,
            temperature=0.7,
            max_tokens=200,
            n=1
        )
        description = response.choices[0].text.strip()
        descriptions.append(description)
    return descriptions
