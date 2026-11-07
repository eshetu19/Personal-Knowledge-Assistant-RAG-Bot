from src.processing.cleaner import clean_text

sample_text = """
 SOCIAL EXTRACT
 
 
 My startup idea is to build an app.
 
 
 Features :
 - No recomendation feed
 - Smart time limits
 
 
 
 I don't want to abandon this idea!!!
 
 My target is 100 users by December 2026.
"""

try:
    cleaned = clean_text(sample_text)
    print("CLEANED DOCUMENT")
    print("---------------")
    print(cleaned)

except (TypeError, ValueError) as error:
    print("Processing error:", error)
