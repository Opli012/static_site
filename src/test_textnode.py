import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.google.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.google.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()