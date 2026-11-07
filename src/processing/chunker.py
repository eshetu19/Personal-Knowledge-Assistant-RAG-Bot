from typing import List

def _split_text(text:str,separators:tuple,chunk_size:int) ->List[str]:
    if len(text) <= chunk_size:
        return [text] if text else []
    #finding the first separator that exists in the text
    separator = None
    separator_index = -1
    
    for index , candidate in enumerate(separators):
        if candidate == " " or candidate in text:
            separator = candidate
            separator_index = index
            break
        
    #split into individual character
    if separator == "":
        return [
            text[i:i+chunk_size] for i in range (0, len(text),chunk_size)
        ]
    parts = text.split(separator)
    pieces = []
    
    for index , part in enumerate(parts) :
        if not part :
            continue
        if index < len(parts)-1 :
            part += separator
        if len(part) <= chunk_size:
            pieces.append(part)
            
        else :
            smaller_separaters = separators[separator_index+1:]
            smaller_pieces = _split_text(
                part,
                smaller_separaters,
                chunk_size
            )
            pieces.extend(smaller_pieces)
    return pieces
    
def _merge_pieces(pices:List[str],chunk_size:int,chunk_overlap:int) -> List[str]:
    chunks = []
    current_pieces = []
    current_length = 0
    for piece in pices:
        piece_length = len(piece)
        if current_length + piece_length <= chunk_size:
            current_pieces.append(piece)
            current_length += piece_length
        else :
            if current_pieces :
                current_chunk = "".join(current_pieces).strip()
                if current_chunk :
                    chunks.append(current_chunk)
            while (current_pieces and current_length > chunk_overlap) :
                removed = current_pieces.pop(0)
                current_length -=len(removed)
            current_pieces.append(piece)
            current_length -= piece_length
        if current_pieces :
            final_chunk = "".join(current_pieces).strip()
            
            if final_chunk:
                chunks.append(final_chunk)
    return chunks

def chunk_text(text:str,chunk_size:int=1000,chunk_overlap:int=150)->List[str] :
    if not isinstance(text,str) :
        raise TypeError("Text must be A string")
    if not text.strip() :
        raise ValueError("Cannot chunk empty text")
    if not isinstance(chunk_size,int) or isinstance(chunk_size,bool):
        raise TypeError("chunk size must be integer")
    if not isinstance(chunk_overlap,int) or isinstance(chunk_overlap,bool):
        raise TypeError("Chunk overlap must be an intrger")
    if chunk_size <= 0 :
        raise ValueError("chunk size must be greater than zero.")
    if chunk_overlap < 0 :
        raise ValueError("chunk overlap cannot be negative")
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk overlap must be smaller than chunk size.")
    
    separators = (
        "\n\n",
        "\n",
        ".",
        "?",
        "!",
        ";",
        ":",
        ",",
        " ",
        ""
        
    )
    pieces =_split_text(text,separators,chunk_size)
    chunks = _merge_pieces(pieces,chunk_size,chunk_overlap)
    return chunks