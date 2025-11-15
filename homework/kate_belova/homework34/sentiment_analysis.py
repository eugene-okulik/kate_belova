from textblob import TextBlob

# Пример текста
text = (
    "I absolutely love the new design of the app, "
    "it's so user-friendly and beautiful!"
)

# Анализ настроения
blob = TextBlob(text)
print(
    f'Тональность текста: {blob.sentiment.polarity}'
)  # Значение от -1 до 1, где -1 — негативный, 1 — позитивный
