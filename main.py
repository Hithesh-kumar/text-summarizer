from transformers import pipeline
summarizer = pipeline("summarization")
article = input("Enter the paragraphy: ")
summarizer(article, max_length = 130, min_length = 30, do_sample = False)