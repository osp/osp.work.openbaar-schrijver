from odf.opendocument import OpenDocumentText
from odf.text import P
from odf.style import Style, MasterPage, PageLayout, PageLayoutProperties, TextProperties, GraphicProperties, ParagraphProperties, DrawingPageProperties, BackgroundImage
from odf.draw import Page, Frame, TextBox, Image

doc = OpenDocumentText()

graphicStyleA = Style(name="graphicstyleA", family="graphic")
gpA = GraphicProperties(border="1cm double #000000", padding="1cm", backgroundcolor="#cccccc")
graphicStyleA.addElement(gpA)

textStyleA = Style(name="textstyleA", family="paragraph")
tpA = TextProperties(fontsize="16pt", fontfamily="Limousine")
textStyleA.addElement(tpA)
ppA = ParagraphProperties(textalign="right")
textStyleA.addElement(ppA)

graphicStyleB = Style(name="graphicstyleB", family="graphic")
gpB = GraphicProperties(border="1cm double #000000", padding="1cm", backgroundcolor="#ff0000")
graphicStyleB.addElement(gpB)

textStyleB = Style(name="textstyleB", family="paragraph")
tpB = TextProperties(fontsize="16pt", fontfamily="diluvienne")
textStyleB.addElement(tpB)

frameA = Frame(stylename=graphicStyleA, height="15cm", width="10cm")
frameB = Frame(stylename=graphicStyleB, height="10cm", width="15cm")

doc.styles.addElement(graphicStyleA)
doc.styles.addElement(textStyleA)

doc.styles.addElement(graphicStyleB)
doc.styles.addElement(textStyleB)

textboxA = TextBox()
textboxB = TextBox()

frameA.addElement(textboxA)
frameB.addElement(textboxB)

pA = P(stylename="textstyleA", text="aaaaaah")
pB = P(stylename="textstyleB", text="bbbbbah")

textboxA.addElement(pA)
textboxB.addElement(pB)

doc.text.addElement(frameA)
doc.text.addElement(frameB)

doc.save("ab", True)
