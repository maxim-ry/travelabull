

# def summarize_eatery(eatery_name):
#   """
#   Generates a concise, captivating summary of the given eatery using prompts.
#   """
#   prompt_1 = f"Write a concise and captivating 2-3 sentence summary of {eatery_name}, an acclaimed eatery."
#   prompt_2 = f"Write a short and engaging blurb about the hidden gem {eatery_name}, sparking curiosity for a visit."

#   summary_1 = model.generate_content(prompt_1)["generated_text"].strip()
#   summary_2 = model.generate_content(prompt_2)["generated_text"].strip()

#   print(f"Acclaimed Eatery Summary:\n{summary_1}")
#   print(f"\nHidden Gem Summary:\n{summary_2}")

# # Get user input for eatery name
# eatery_name = input("Enter the name of an eatery: ")

# summarize_eatery(eatery_name)