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
                LeafNode(tag="b", value="Bold text"),
                ParentNode("div", [
                    LeafNode(tag="i", value="italic text"),
                    LeafNode(tag="i", value="Normal text inside div"),
                ])
            ])
        
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b><div><i>italic text</i><i>Normal text inside div</i></div></p>"
        )
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><child>span</child></div>")

if __name__ == "__main__":
    unittest.main()