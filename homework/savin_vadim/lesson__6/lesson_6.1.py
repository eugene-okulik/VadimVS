text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
list_text = text.split()
result_text = []
for word in list_text:
    if word[-1] not in ".,":
        result_text.append(word + "ing")
    else:
        punct = word[-1]
        result_text.append(word[:-1] + "ing" + punct)
result_text = " ".join(result_text)
print(result_text)
