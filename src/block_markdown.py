from textnode import BlockType

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

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH