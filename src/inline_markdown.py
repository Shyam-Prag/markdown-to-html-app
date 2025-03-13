from textnode import TextNode, TextType

import re 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    image_regex_pattern = "!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex_pattern, text)
    return matches 

def extract_markdown_links(text):
    image_regex_pattern = "(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex_pattern, text)
    return matches 


def split_nodes_image(old_nodes):
    result = []
    
    for old_node in old_nodes:
        # Skip non-text nodes
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        
        # Get the text and check for images
        text = old_node.text
        images = extract_markdown_images(text)
        
        if not images:
            # No images found, keep node as is
            result.append(old_node)
            continue
        
        # Start with the full text
        remaining_text = text
        
        # Process each image found
        for image_alt, image_url in images:
            #split on the first occurange of this image 
            image_markdown = f"![{image_alt}]({image_url})"
            parts = remaining_text.split(image_markdown, 1)

            #add text before the image if not empty 
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))

            # Add the image node
            result.append(TextNode(image_alt, TextType.IMAGE, image_url))

            #update the remaining text 
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        #add any other remaining text
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    
    return result 