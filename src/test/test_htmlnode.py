import unittest

from ..htmlnode import HTMLNode 
class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        prop = {
        "href": "https://www.google.com", 
        "target": "_blank",
        }

        x = HTMLNode(tag="a", value="hello, world",children=None, props=prop)
        self.assertEqual(
            x.props_to_html(),
            'href="https://www.google.com" target="_blank"'
        )
        print("successfull ran test_props_to_html")
    
    def test_to_html(self):
        x = HTMLNode(tag="a", value="hello, world",children=None, props=None)
        with self.assertRaises(NotImplementedError) as context:
            x.to_html()
        print("successfully ran test_to_html")
    
    def test_repr_string(self):
        prop = {
        "href": "https://www.google.com", 
        "target": "_blank",
        }

        x = HTMLNode(tag="a", value="hello, world",children=None, props=prop)
        
        self.assertEquals(
                x.__repr__(), 
                f"HTMLNode(tag={x.tag}, value={x.value}, children={x.children}, props={x.props})"
            )
        print("successfully tested test_repr_string")
        


if __name__ == "__main__":
    unittest.main()