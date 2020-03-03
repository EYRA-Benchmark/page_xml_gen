#!/usr/bin/env python

#
# Generated Tue Mar  3 13:39:46 2020 by generateDS.py version 2.35.15.
# Python 3.7.3 (default, Mar 27 2019, 22:11:17)  [GCC 7.3.0]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'page_api.py')
#   ('-s', 'page_sub.py')
#   ('--super', 'page_api')
#
# Command line arguments:
#   pagecontent.xsd
#
# Command line:
#   /home/tom/miniconda3/bin/generateDS -f -o "page_api.py" -s "page_sub.py" --super="page_api" pagecontent.xsd
#
# Current working directory (os.getcwd()):
#   experiments
#

import os
import sys
from lxml import etree as etree_

from page_xml_gen import page_api as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class PcGtsTypeSub(supermod.PcGtsType):
    def __init__(self, pcGtsId=None, Metadata=None, Page=None, **kwargs_):
        super(PcGtsTypeSub, self).__init__(pcGtsId, Metadata, Page,  **kwargs_)
supermod.PcGtsType.subclass = PcGtsTypeSub
# end class PcGtsTypeSub


class MetadataTypeSub(supermod.MetadataType):
    def __init__(self, Creator=None, Created=None, LastChange=None, Comments=None, **kwargs_):
        super(MetadataTypeSub, self).__init__(Creator, Created, LastChange, Comments,  **kwargs_)
supermod.MetadataType.subclass = MetadataTypeSub
# end class MetadataTypeSub


class PageTypeSub(supermod.PageType):
    def __init__(self, imageFilename=None, imageWidth=None, imageHeight=None, Border=None, PrintSpace=None, ReadingOrder=None, Layers=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, NoiseRegion=None, FrameRegion=None, UnknownRegion=None, **kwargs_):
        super(PageTypeSub, self).__init__(imageFilename, imageWidth, imageHeight, Border, PrintSpace, ReadingOrder, Layers, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, NoiseRegion, FrameRegion, UnknownRegion,  **kwargs_)
supermod.PageType.subclass = PageTypeSub
# end class PageTypeSub


class TextRegionTypeSub(supermod.TextRegionType):
    def __init__(self, id=None, orientation=None, type_=None, textColour=None, bgColour=None, reverseVideo=None, fontSize=None, leading=None, kerning=None, readingDirection=None, readingOrientation=None, indented=None, primaryLanguage=None, secondaryLanguage=None, primaryScript=None, secondaryScript=None, Coords=None, TextLine=None, TextEquiv=None, **kwargs_):
        super(TextRegionTypeSub, self).__init__(id, orientation, type_, textColour, bgColour, reverseVideo, fontSize, leading, kerning, readingDirection, readingOrientation, indented, primaryLanguage, secondaryLanguage, primaryScript, secondaryScript, Coords, TextLine, TextEquiv,  **kwargs_)
supermod.TextRegionType.subclass = TextRegionTypeSub
# end class TextRegionTypeSub


class CoordsTypeSub(supermod.CoordsType):
    def __init__(self, Point=None, **kwargs_):
        super(CoordsTypeSub, self).__init__(Point,  **kwargs_)
supermod.CoordsType.subclass = CoordsTypeSub
# end class CoordsTypeSub


class PointTypeSub(supermod.PointType):
    def __init__(self, x=None, y=None, **kwargs_):
        super(PointTypeSub, self).__init__(x, y,  **kwargs_)
supermod.PointType.subclass = PointTypeSub
# end class PointTypeSub


class TextLineTypeSub(supermod.TextLineType):
    def __init__(self, id=None, Coords=None, Word=None, TextEquiv=None, **kwargs_):
        super(TextLineTypeSub, self).__init__(id, Coords, Word, TextEquiv,  **kwargs_)
supermod.TextLineType.subclass = TextLineTypeSub
# end class TextLineTypeSub


class WordTypeSub(supermod.WordType):
    def __init__(self, id=None, Coords=None, Glyph=None, TextEquiv=None, **kwargs_):
        super(WordTypeSub, self).__init__(id, Coords, Glyph, TextEquiv,  **kwargs_)
supermod.WordType.subclass = WordTypeSub
# end class WordTypeSub


class GlyphTypeSub(supermod.GlyphType):
    def __init__(self, id=None, ligature=None, symbol=None, Coords=None, TextEquiv=None, **kwargs_):
        super(GlyphTypeSub, self).__init__(id, ligature, symbol, Coords, TextEquiv,  **kwargs_)
supermod.GlyphType.subclass = GlyphTypeSub
# end class GlyphTypeSub


class TextEquivTypeSub(supermod.TextEquivType):
    def __init__(self, PlainText=None, Unicode=None, **kwargs_):
        super(TextEquivTypeSub, self).__init__(PlainText, Unicode,  **kwargs_)
supermod.TextEquivType.subclass = TextEquivTypeSub
# end class TextEquivTypeSub


class ImageRegionTypeSub(supermod.ImageRegionType):
    def __init__(self, id=None, orientation=None, colourDepth=None, bgColour=None, embText=None, Coords=None, **kwargs_):
        super(ImageRegionTypeSub, self).__init__(id, orientation, colourDepth, bgColour, embText, Coords,  **kwargs_)
supermod.ImageRegionType.subclass = ImageRegionTypeSub
# end class ImageRegionTypeSub


class LineDrawingRegionTypeSub(supermod.LineDrawingRegionType):
    def __init__(self, id=None, orientation=None, penColour=None, bgColour=None, embText=None, Coords=None, **kwargs_):
        super(LineDrawingRegionTypeSub, self).__init__(id, orientation, penColour, bgColour, embText, Coords,  **kwargs_)
supermod.LineDrawingRegionType.subclass = LineDrawingRegionTypeSub
# end class LineDrawingRegionTypeSub


class GraphicRegionTypeSub(supermod.GraphicRegionType):
    def __init__(self, id=None, orientation=None, type_=None, numColours=None, embText=None, Coords=None, **kwargs_):
        super(GraphicRegionTypeSub, self).__init__(id, orientation, type_, numColours, embText, Coords,  **kwargs_)
supermod.GraphicRegionType.subclass = GraphicRegionTypeSub
# end class GraphicRegionTypeSub


class TableRegionTypeSub(supermod.TableRegionType):
    def __init__(self, id=None, orientation=None, rows=None, columns=None, lineColour=None, bgColour=None, lineSeparators=None, embText=None, Coords=None, **kwargs_):
        super(TableRegionTypeSub, self).__init__(id, orientation, rows, columns, lineColour, bgColour, lineSeparators, embText, Coords,  **kwargs_)
supermod.TableRegionType.subclass = TableRegionTypeSub
# end class TableRegionTypeSub


class ChartRegionTypeSub(supermod.ChartRegionType):
    def __init__(self, id=None, orientation=None, type_=None, numColours=None, bgColour=None, embText=None, Coords=None, **kwargs_):
        super(ChartRegionTypeSub, self).__init__(id, orientation, type_, numColours, bgColour, embText, Coords,  **kwargs_)
supermod.ChartRegionType.subclass = ChartRegionTypeSub
# end class ChartRegionTypeSub


class SeparatorRegionTypeSub(supermod.SeparatorRegionType):
    def __init__(self, id=None, orientation=None, colour=None, Coords=None, **kwargs_):
        super(SeparatorRegionTypeSub, self).__init__(id, orientation, colour, Coords,  **kwargs_)
supermod.SeparatorRegionType.subclass = SeparatorRegionTypeSub
# end class SeparatorRegionTypeSub


class MathsRegionTypeSub(supermod.MathsRegionType):
    def __init__(self, id=None, orientation=None, bgColour=None, Coords=None, **kwargs_):
        super(MathsRegionTypeSub, self).__init__(id, orientation, bgColour, Coords,  **kwargs_)
supermod.MathsRegionType.subclass = MathsRegionTypeSub
# end class MathsRegionTypeSub


class NoiseRegionTypeSub(supermod.NoiseRegionType):
    def __init__(self, id=None, Coords=None, **kwargs_):
        super(NoiseRegionTypeSub, self).__init__(id, Coords,  **kwargs_)
supermod.NoiseRegionType.subclass = NoiseRegionTypeSub
# end class NoiseRegionTypeSub


class UnknownRegionTypeSub(supermod.UnknownRegionType):
    def __init__(self, id=None, Coords=None, **kwargs_):
        super(UnknownRegionTypeSub, self).__init__(id, Coords,  **kwargs_)
supermod.UnknownRegionType.subclass = UnknownRegionTypeSub
# end class UnknownRegionTypeSub


class FrameRegionTypeSub(supermod.FrameRegionType):
    def __init__(self, id=None, bgColour=None, borderPresent=None, Coords=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, NoiseRegion=None, FrameRegion=None, UnknownRegion=None, **kwargs_):
        super(FrameRegionTypeSub, self).__init__(id, bgColour, borderPresent, Coords, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, NoiseRegion, FrameRegion, UnknownRegion,  **kwargs_)
supermod.FrameRegionType.subclass = FrameRegionTypeSub
# end class FrameRegionTypeSub


class PrintSpaceTypeSub(supermod.PrintSpaceType):
    def __init__(self, Coords=None, **kwargs_):
        super(PrintSpaceTypeSub, self).__init__(Coords,  **kwargs_)
supermod.PrintSpaceType.subclass = PrintSpaceTypeSub
# end class PrintSpaceTypeSub


class ReadingOrderTypeSub(supermod.ReadingOrderType):
    def __init__(self, OrderedGroup=None, UnorderedGroup=None, **kwargs_):
        super(ReadingOrderTypeSub, self).__init__(OrderedGroup, UnorderedGroup,  **kwargs_)
supermod.ReadingOrderType.subclass = ReadingOrderTypeSub
# end class ReadingOrderTypeSub


class RegionRefIndexedTypeSub(supermod.RegionRefIndexedType):
    def __init__(self, index=None, regionRef=None, **kwargs_):
        super(RegionRefIndexedTypeSub, self).__init__(index, regionRef,  **kwargs_)
supermod.RegionRefIndexedType.subclass = RegionRefIndexedTypeSub
# end class RegionRefIndexedTypeSub


class OrderedGroupIndexedTypeSub(supermod.OrderedGroupIndexedType):
    def __init__(self, id=None, index=None, RegionRefIndexed=None, OrderedGroupIndexed=None, UnorderedGroupIndexed=None, **kwargs_):
        super(OrderedGroupIndexedTypeSub, self).__init__(id, index, RegionRefIndexed, OrderedGroupIndexed, UnorderedGroupIndexed,  **kwargs_)
supermod.OrderedGroupIndexedType.subclass = OrderedGroupIndexedTypeSub
# end class OrderedGroupIndexedTypeSub


class UnorderedGroupIndexedTypeSub(supermod.UnorderedGroupIndexedType):
    def __init__(self, id=None, index=None, RegionRef=None, OrderedGroup=None, UnorderedGroup=None, **kwargs_):
        super(UnorderedGroupIndexedTypeSub, self).__init__(id, index, RegionRef, OrderedGroup, UnorderedGroup,  **kwargs_)
supermod.UnorderedGroupIndexedType.subclass = UnorderedGroupIndexedTypeSub
# end class UnorderedGroupIndexedTypeSub


class RegionRefTypeSub(supermod.RegionRefType):
    def __init__(self, regionRef=None, **kwargs_):
        super(RegionRefTypeSub, self).__init__(regionRef,  **kwargs_)
supermod.RegionRefType.subclass = RegionRefTypeSub
# end class RegionRefTypeSub


class OrderedGroupTypeSub(supermod.OrderedGroupType):
    def __init__(self, id=None, RegionRefIndexed=None, OrderedGroupIndexed=None, UnorderedGroupIndexed=None, **kwargs_):
        super(OrderedGroupTypeSub, self).__init__(id, RegionRefIndexed, OrderedGroupIndexed, UnorderedGroupIndexed,  **kwargs_)
supermod.OrderedGroupType.subclass = OrderedGroupTypeSub
# end class OrderedGroupTypeSub


class UnorderedGroupTypeSub(supermod.UnorderedGroupType):
    def __init__(self, id=None, RegionRef=None, OrderedGroup=None, UnorderedGroup=None, **kwargs_):
        super(UnorderedGroupTypeSub, self).__init__(id, RegionRef, OrderedGroup, UnorderedGroup,  **kwargs_)
supermod.UnorderedGroupType.subclass = UnorderedGroupTypeSub
# end class UnorderedGroupTypeSub


class BorderTypeSub(supermod.BorderType):
    def __init__(self, Coords=None, **kwargs_):
        super(BorderTypeSub, self).__init__(Coords,  **kwargs_)
supermod.BorderType.subclass = BorderTypeSub
# end class BorderTypeSub


class LayersTypeSub(supermod.LayersType):
    def __init__(self, Layer=None, **kwargs_):
        super(LayersTypeSub, self).__init__(Layer,  **kwargs_)
supermod.LayersType.subclass = LayersTypeSub
# end class LayersTypeSub


class LayerTypeSub(supermod.LayerType):
    def __init__(self, id=None, zIndex=None, RegionRef=None, **kwargs_):
        super(LayerTypeSub, self).__init__(id, zIndex, RegionRef,  **kwargs_)
supermod.LayerType.subclass = LayerTypeSub
# end class LayerTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGtsType'
        rootClass = supermod.PcGtsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGtsType'
        rootClass = supermod.PcGtsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGtsType'
        rootClass = supermod.PcGtsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2010-03-19"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGtsType'
        rootClass = supermod.PcGtsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from page_api import *\n\n')
        sys.stdout.write('import page_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
