from openai import OpenAI
import os
import asyncio





client = OpenAI(
    # This is the default and can be omitted
    api_key= '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',
)

# user_city = ["Tokyo", "japan", "usa"]
# user_rate = [5, 3, 4]
# user_type = ["foodie", "cultural enthusiast", "foodie"]

def get_summeryies(user_city,user_rate,user_type):
    summaries = []
    for i in range(0, 3):

        text_to_summarize = f"""
        Generate a concise and captivating summary of {user_city[i]} for a {user_type[i]} traveler.
        #   Combines all summaries is 2-3 sentences long and aims to spark curiosity and make the visit memorable.
        #   Include the city's rating: {user_rate[i]} out of 5.
        """

        # Define the prompt with instruction to summarize the given text
        prompt = f"Summarize the following text:\n{text_to_summarize}\n\nSummary:"

        stream = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                summaries.append(''.join(chunk.choices[0].delta.content))

    return ''.join(summaries)
def get_summeryies_of_summary(user_city, user_rate, user_type):
    summaries_of_summery = []
    text_to_summarize_summery = f"""
            Generate a concise and captivating summary of the {get_summeryies(user_city,user_rate,user_type)} of for a traveler and vacationer.
            # Combines all summaries is 2-3 sentences long and aims to spark curiosity and make the visit memorable.
            #  Do not Exceed 2-3 sentences.
            """

    stream = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": text_to_summarize_summery}],
            stream=True,
        )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            summaries_of_summery.append(''.join(chunk.choices[0].delta.content))
    return ''.join(summaries_of_summery)

# print(get_summeryies_of_summary(user_city,user_rate,user_type))