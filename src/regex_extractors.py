import re 

def extract_markdown_images(text):
    image_regex_pattern = "!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex_pattern, text)
    return matches 

def extract_markdown_links(text):
    image_regex_pattern = "(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex_pattern, text)
    return matches 

