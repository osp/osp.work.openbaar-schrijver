# -*- coding: utf-8 -*-
# lovely!
# IMPORTANT: when finished, goto where it says
# for key in text_style["brief"].keys():
# at the moment, we're only looping through the letters !
# a.u.b.
from odf.opendocument import OpenDocumentText
from odf.text import P
from odf.style import Style, TextProperties, ParagraphProperties, BackgroundImage, GraphicProperties
from odf.draw import Frame, TextBox

from texts import *
from stylesheet import *

dingbats = {"kristallen" : [u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴", u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴", u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴", u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴",u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴", u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴", u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴", u"✭", u"✮", u"✯", u"✰", u"✱", u"✲", u"✳", u"✴"],
	"roze" : [u"✿", u"❀", u"✿", u"❀", u"❁", u"✼", u" ", u"✿", u"❀",u"✿", u"❀", u"❁", u"✼", u" ", u"✿", u"❀", u"✿", u"❀", u"❁", u"✼", u" ", u"✿", u"❀",u"✿", u"❀", u"❁", u"✼", u" ", u"✿", u"❀", u"✿", u"❀", u"❁", u"✼", u" ", u"✿", u"❀",u"✿", u"❀", u"❁", u"✼"],
	"lavendel" : [u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍",u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍",u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍",u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍", u"҈", u"❍"]
}

# mytext_properties will come from the stylesheet.
# this function takes the base styling of a genre and appends a set of
# paragraphic properties
def genre2template(genre, mytext_properties, font, myparagraph_properties):
	myname = genre + "_" + font
	my_style = Style(attributes={"name" : myname, "family" : "paragraph"})
	my_style.addElement(TextProperties(attributes=mytext_properties))
	my_style.addElement(ParagraphProperties(attributes=myparagraph_properties))
	return my_style

def beehive(an_odt, a_graphic_style, an_h, a_w, an_x, a_y, a_z):
	# http://en.wikipedia.org/wiki/Frame_(beehive)
	an_odt.styles.addElement(a_graphic_style)
	a_frame = Frame(stylename=a_graphic_style, height=an_h, width=a_w,
					x=an_x, y=a_y, zindex=a_z)
	a_textbox = TextBox()
	a_frame.addElement(a_textbox)
	return {"frame" : a_frame, "textbox" : a_textbox}

def text_unit(an_odt, a_textgraph_style, a_text, a_textbox):
	a_p = P(stylename=a_textgraph_style, text=a_text)
	a_textbox.addElement(a_p)	

def dingbat_spices(an_odt, a_spice, a_font):
	## graphic
	dingbat_stylename = a_spice + "_style_frame"
	dingbat_graphic_style = Style(name=dingbat_stylename, family="graphic")
	dingbat_graphic_properties = GraphicProperties()
	dingbat_graphic_style.addElement(dingbat_graphic_properties)
	dingbat_beehive = beehive(an_odt, dingbat_graphic_style,
							"240mm", "10mm", "0mm", "0mm", "100")
	dingbat_frame = dingbat_beehive["frame"]
	dingbat_textbox = dingbat_beehive["textbox"]

	## textgraph
	dingbat_stylename = a_spice + "_style_paragraph"
	dingbat_textgraph_style = Style(name=dingbat_stylename, family="paragraph")
	dingbat_text_props = TextProperties(fontsize="14pt", fontfamily="FreeSerif")
	dingbat_textgraph_style.addElement(dingbat_text_props)
	dingbat_paragraph_props = ParagraphProperties()
	dingbat_textgraph_style.addElement(dingbat_paragraph_props)
	an_odt.styles.addElement(dingbat_textgraph_style)

	for i in dingbats[a_spice]:
		text_unit(an_odt, dingbat_textgraph_style, i, dingbat_textbox)

	an_odt.text.addElement(dingbat_frame)

def border_spices(an_odt, a_spice, a_font):
	## graphic
	border_stylename = a_spice + "border_style"
	border_graphic_style = Style(name=border_stylename, family="graphic")
	#href = an_odt.addPicture(a_spice + ".jpg")
	#if a_spice == "kristallen":
	#	border_graphic_properties = GraphicProperties(border="0.5mm double #000000")
	#elif a_spice == "roze":
	#	border_graphic_properties = GraphicProperties(border="0.5mm double #000000")
	#else:
	#	border_graphic_properties = GraphicProperties(border="0.5mm double #000000")
	border_graphic_properties = GraphicProperties(border="0.5mm double #000000")
	border_graphic_style.addElement(border_graphic_properties)
	border_beehive = beehive(an_odt, border_graphic_style,
							"273mm", "194mm", "-12mm", "-12mm", "1")
	border_frame = border_beehive["frame"]
	border_textbox = border_beehive["textbox"]

	## textgraph
	border_stylename = "emptygif"
	border_textgraph_style = Style(name=border_stylename, family="paragraph")
	border_text_props = TextProperties()
	border_textgraph_style.addElement(border_text_props)
	border_paragraph_props = ParagraphProperties()
	border_textgraph_style.addElement(border_paragraph_props)
	an_odt.styles.addElement(border_textgraph_style)

	text_unit(an_odt, border_textgraph_style, u"", border_textbox)

	an_odt.text.addElement(border_frame)

def label(an_odt, a_spice, a_font):
	label_stylename = a_spice + a_font
	label_graphic_style = Style(name=label_stylename, family="graphic")
	label_graphic_properties = GraphicProperties()
	label_graphic_style.addElement(label_graphic_properties)
	label_beehive = beehive(an_odt, label_graphic_style,
							"5mm", "50mm", "60mm", "263mm", "1")
	label_frame = label_beehive["frame"]
	label_textbox = label_beehive["textbox"]

	## textgraph
	label_stylename = a_spice + a_font
	label_textgraph_style = Style(name=label_stylename, family="paragraph")
	label_text_props = TextProperties(fontsize="11.1pt", fontfamily="Nimbus Sans L", color="#ffffff")
	label_textgraph_style.addElement(label_text_props)
	label_paragraph_props = ParagraphProperties(backgroundcolor="#000000", textalign="center")
	label_textgraph_style.addElement(label_paragraph_props)
	an_odt.styles.addElement(label_textgraph_style)

	text_unit(an_odt, label_textgraph_style, a_spice + " " + a_font, label_textbox)

	an_odt.text.addElement(label_frame)

def text_frame(an_odt, a_genre, a_font):
	### header frame (for letter)
	if a_genre == "brief":
		## graphic
		#FS ADDED ATLAS STYLE
		header_stylename = "header_frame_style"
		header_graphic_style = Style(name=header_stylename, family="graphic")
		header_graphic_properties = GraphicProperties(backgroundcolor="#ffffff", border="10mm double #ffffff")
		header_graphic_style.addElement(header_graphic_properties)
		header_beehive = beehive(an_odt, header_graphic_style,
								"20mm", "170mm", "0mm", "0mm", "2")
		header_frame = header_beehive["frame"]
		header_textbox = header_beehive["textbox"]
	
		## paragraphic
		header_stylename = "header_paragraph_style"
		header_textgraph_style = Style(name=header_stylename, family="paragraph")
		atlas_textgraph_style = Style(name="atlas", family="paragraph")
		
		header_text_props = TextProperties(fontsize="12pt", fontfamily="DIN_OSP")
		atlas_text_props = TextProperties(fontsize="16pt", fontfamily="OSP-Atlast")

		header_textgraph_style.addElement(header_text_props)
		atlas_textgraph_style.addElement(atlas_text_props)

		header_paragraph_props = ParagraphProperties(textalign="right")
		atlas_paragraph_props = ParagraphProperties(textalign="right")
		header_textgraph_style.addElement(header_paragraph_props)
		atlas_textgraph_style.addElement(atlas_paragraph_props)
		an_odt.styles.addElement(header_textgraph_style)
		an_odt.styles.addElement(atlas_textgraph_style)

		text_unit(an_odt, header_textgraph_style, u"Gaasbeek, 13 februari 2050", header_textbox)
		
		text_unit(an_odt, atlas_textgraph_style, u"Hello World", header_textbox)
	
		an_odt.text.addElement(header_frame)

	### textframe
	## graphic
	mid_stylename = "mid_frame_style"
	mid_graphic_style = Style(name=mid_stylename, family="graphic")
	mid_graphic_properties = GraphicProperties(backgroundcolor="#ffffff", border="10mm double #ffffff")
	mid_graphic_style.addElement(mid_graphic_properties)
	mid_beehive = beehive(an_odt, mid_graphic_style,
							"240mm", "170mm", "0mm", "0mm", "1")
	mid_frame = mid_beehive["frame"]
	mid_textbox = mid_beehive["textbox"]

	for paragraph in txt[a_genre]:
		text_unit(an_odt, a_genre + "_" + a_font, paragraph, mid_textbox)

	an_odt.text.addElement(mid_frame)

def dingbat_spice(genre, font, spice):
	for myspice in spice:
		myodt = OpenDocumentText()

		# template is updated by font
		text_template[genre].update(text_style[genre][font])
		paragraph_template[genre].update(paragraph_style[genre][font])
		template = genre2template(genre,
							text_template[genre],
							font,
							paragraph_template[genre])
		myodt.styles.addElement(template)
		border_spices(myodt, myspice, font)
		text_frame(myodt, genre, font)
		dingbat_spices(myodt, myspice, font)

		label(myodt, myspice, font)

		myname = genre + "_" + font + "_" + myspice
		myodt.save(myname, True)

for key in text_style["brief"].keys():
#	def dingbat_spice(genre, font, spice):
	dingbat_spice("brief", key, ["kristallen", "roze", "lavendel"])
	
for key in text_style["verhaal"].keys():
#	def dingbat_spice(genre, font, spice):
	dingbat_spice("verhaal", key, ["kristallen", "roze", "lavendel"])

for key in text_style["gedicht"].keys():
#	def dingbat_spice(genre, font, spice):
	dingbat_spice("gedicht", key, ["kristallen", "roze", "lavendel"])
