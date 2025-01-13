from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError("to html method not yet implemented")

    def props_to_html(self):
        if self.props:
            return " ".join(f'{key}="{value}"' for key,value in self.props.items())
        else: 
            return ""
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):    
        if value is None:
            raise ValueError("A LeafNode must contain a value")

        if props is None:
            props = {}

        super().__init__(tag=tag,value=value, children=None, props=props)

    def to_html(self):   
        if self.value is None:
            raise ValueError("LeafNode to_html method needs a value!")
        if self.tag is None:
            return f"{self.value}"
        
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def text_node_to_html_node(text_node):
        available_text_types = {
            TextType.BOLD: 1,
            TextType.TEXT:2,
            TextType.ITALIC:3,
            TextType.CODE:4,
            TextType.LINK:5,
            TextType.IMAGE:6
        }
        if text_node.text_type not in available_text_types:
            raise ValueError("Text Type is not valid")
        


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode to_html needs tag")
        if self.children is None:
            raise ValueError("ParentNode to_html method needs children value")
        
        res = ""
        for child in self.children:
            res += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{res}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

