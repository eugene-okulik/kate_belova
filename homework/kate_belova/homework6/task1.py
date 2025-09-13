text = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

ending = 'ing'
new_text = []

for word in text.split():
    if word[-1] in ',.':
        new_word = word[:-1] + ending + word[-1]
    else:
        new_word = word + ending

    new_text.append(new_word)

print(' '.join(new_text))
