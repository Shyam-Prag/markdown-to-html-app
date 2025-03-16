from textnode import TextNode, TextType
import shutil 
import os 

from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    # STEP 1: DELETE PUBLIC DIRECTORY 
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # STEP 2: COPY STATIC FILES]
    print("copying files...")
    copy_files_recursive(dir_path_static, dir_path_public)
    print("successfully copied files...")
    
    # STEP3: GENERATE PAGES
    print("Generating pages...")
    for root, dirs, files in os.walk("content"):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)

                # Replace 'content' with 'public' in the path to make the destination
                dest_path = from_path.replace("content", "public").replace(".md", ".html")

                # Use a shared template
                template_path = "template.html"

                # Generate the page
                generate_page(from_path, template_path, dest_path)

main()
