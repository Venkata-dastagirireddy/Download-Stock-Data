
def save_text_to_file(text):
    with open("Insights.txt", "a") as file:
        file.write(text + "\n")