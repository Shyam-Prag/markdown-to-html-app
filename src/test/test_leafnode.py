import unittest
from htmlnode import LeafNode 

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        html_node = LeafNode(tag="p", value="This is a paragraph of text.")
        print(html_node)
        x = html_node.to_html()

        self.assertEqual(
            x,
            "<p>This is a paragraph of text.</p>"
            )

    def test_repr(self):
        html_node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(
            html_node.__repr__(),
            'LeafNode(p, This is a paragraph of text., {})'
                         )

if __name__ == "__main__":
    unittest.main()