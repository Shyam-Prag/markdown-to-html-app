import unittest
from htmlnode import HTMLNode, ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_list_of_leaf_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode(tag="b",value= "Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    
    def test_mixed_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("div", [
                    LeafNode(tag="i", value="italic text"),
                    LeafNode(tag="i", value="Normal text inside div"),
                ])
            ])
        
        self.assertEqual(
            node.to_html(),
            "<p><Bold text>b</Bold text><div><i>italic text</i><i>Normal text inside div</i></div></p>"
        )

if __name__ == "__main__":
    unittest.main()