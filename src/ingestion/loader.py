from pathlib import Path
def load_text(file_path:str)-> str:
    path=Path(file_path)
    if not path.exists() :
        raise FileNotFoundError(f"document not found : {file_path}")
    if not path.is_file() :
        raise IsADirectoryError(f"Expected a file,recieved a directory: {file_path}")
    if path.suffix.lower() != ".txt":
        raise ValueError("Only TXT files are supported")
    with path.open("r",encoding="utf-8") as file:
        content = file.read()
    if not content.strip() :
        raise ValueError(f"document is empty: {file_path}")
    return content