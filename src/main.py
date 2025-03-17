from textnode import TextNode, TextType
import shutil 
import os 

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    # STEP 1: DELETE PUBLIC DIRECTORY 
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # STEP 2: COPY STATIC FILES
    print("copying files...")
    copy_files_recursive(dir_path_static, dir_path_public)
    print("successfully copied files...")
    
    # STEP3: GENERATE PAGES
    print("Generating pages...")
    # Simply call generate_pages_recursive with the content directory
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

main()
