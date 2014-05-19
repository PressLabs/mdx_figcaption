# -*- coding: utf-8 -*-
import markdown
from markdown.util import etree

class MarkdownCaption(markdown.treeprocessors.Treeprocessor):

    def run(self,root):
        self.search_and_change(root)
        return root

    def search_and_change(self, element):
        for child in list(element.getiterator()):
            if child.tag == "img":
                d=child.attrib.copy()
                child.clear()
                child.tag="figure"
                img=etree.Element("img")
                img.attrib=d
                child.append(img)
                caption=etree.Element("figcaption")
                caption.text=d.get("title","")
                child.append(caption)

class CaptionsExtension(markdown.extensions.Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors["figures"] = MarkdownCaption(md)
        md.registerExtension(self)

def makeExtension(configs=None):
    return CaptionsExtension(configs)
