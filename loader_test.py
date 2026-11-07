from src.ingestion.loader import load_text

try:
    content = load_text("C:/Users/s2s/Desktop/design system.txt")
    print("content successfully loaded")
    print(content)
except FileNotFoundError as error:
    print(error)
except IsADirectoryError as error :
    print(error)
except ValueError as error:
    print(error)
# except UnicodeDecodeError as error:
#     print("the document is not valid UTF-8",error)