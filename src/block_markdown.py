def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue

        block = block.strip()  # Remove leading/trailing spaces from entire block
        
        # Split into lines and strip spaces for each line
        lines = block.split("\n")
        cleaned_lines = [line.strip() for line in lines]
        
        # Join the cleaned lines back into a single block
        cleaned_block = "\n".join(cleaned_lines)
        
        filtered_blocks.append(cleaned_block)

    return filtered_blocks