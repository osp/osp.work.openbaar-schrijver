# -*- coding: utf-8 -*-
# lovely!
# IMPORTANT: when finished, goto where it says
# for key in text_style["brief"].keys():
# at the moment, we're only looping through the letters !
# a.u.b.
from odf.opendocument import OpenDocumentText
from odf.text import P, Span
from odf.style import Style, TextProperties, ParagraphProperties, BackgroundImage, GraphicProperties
from odf.draw import Frame, TextBox

from texts import *
from stylesheet import *

words = [u"aai", u"aan", u"alleen", u"beloofde", u"bemind", u"benen", u"bewust", u"borst", u"eenzaam", u"elkaar", u"geloofde", u"gesmoord", u"gevoel", u"gezicht", u"giechelend", u"glimlachte", u"haar", u"hand", u"haren", u"hem", u"hen", u"herinner", u"herinneren", u"herinneringen", u"hier", u"hij", u"hoofd", u"hoop", u"huilen", u"ik", u"ja", u"je", u"Jij", u"jij", u"jou", u"jouw", u"kiezen", u"kleurde", u"leven", u"liefde", u"liefdes", u"liefs", u"liefste", u"lieve", u"lippen", u"man", u"me", u"mijn", u"moed", u"moeilijk", u"ogen", u"ons", u"ontmoeting", u"onze", u"opnieuw", u"rituelen", u"roos", u"routine", u"ruggen", u"samen", u"smoorverliefd", u"spijt", u"stotterde", u"streelde", u"tenen", u"troost", u"vergat", u"vergeet", u"vergeten", u"voorzichtig", u"vriend", u"vrienden", u"vrijheid", u"vrouw", u"we", u"wij", u"wil", u"wilde", u"wilden", u"willen", u"ze", u"zelf", u"zij", u"zijn", u"zinnen"]

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

def text_unit_spice(an_odt, a_textgraph_style, a_boldstyle, a_text, a_textbox):
	sectioned = a_text.split()
	a_p = P(text=u"", stylename=a_textgraph_style)
	try:
		sectioned[-1]
		for i in range(len(sectioned)-1):
			if sectioned[i] in words:
				boldpart = Span(stylename=a_boldstyle, text=sectioned[i] + u" ")
				a_p.addElement(boldpart)
			else:
				normalpart = Span(text=sectioned[i] + u" ")
				a_p.addElement(normalpart)
		a_p.addText(sectioned[-1])
	except IndexError:
		a_p.addText(u"")
	a_textbox.addElement(a_p)

def border_spices(an_odt, a_spice, a_font):
	## graphic
	border_stylename = a_spice + "border_style"
	border_graphic_style = Style(name=border_stylename, family="graphic")
	#href = an_odt.addPicture(a_spice + ".jpg")
	#if a_spice == "sexy":
	#	border_graphic_properties = GraphicProperties(border="0.5mm double #000000")
	#elif a_spice == "champagne":
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

def text_frame(an_odt, a_genre, a_font, a_spice):
	# character spice !
	if a_spice == "sexy":
		boldstyle = Style(name=a_spice + "Bold", family="text")
		boldprop = TextProperties(fontfamily="diluvienne", fontsize="28pt")
		boldstyle.addElement(boldprop)
		an_odt.automaticstyles.addElement(boldstyle)
	elif a_spice == "champagne":
		boldstyle = Style(name=a_spice + "Bold", family="text")
		boldprop = TextProperties(fontfamily="Cimatics_Trash")
		boldstyle.addElement(boldprop)
		an_odt.automaticstyles.addElement(boldstyle)
	else:
		boldstyle = Style(name=a_spice + "Bold", family="text")
		boldprop = TextProperties(fontweight="bold", fontfamily="NotCourierSans", letterspacing="2mm")
		boldstyle.addElement(boldprop)
		an_odt.automaticstyles.addElement(boldstyle)

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
		text_unit_spice(an_odt, a_genre + "_" + a_font, boldstyle, paragraph, mid_textbox)

	an_odt.text.addElement(mid_frame)

def character_spice(genre, font, spice):
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
		text_frame(myodt, genre, font, myspice)

		label(myodt, myspice, font)

		myname = genre + "_" + font + "_" + myspice
		myodt.save(myname, True)

for key in text_style["brief"].keys():
	# def image_spice(genre, style, spice, mytext):
	character_spice("brief", key, ["sexy", "champagne", "lungo"])
	
for key in text_style["verhaal"].keys():
	# def image_spice(genre, style, spice, mytext):
	character_spice("verhaal", key, ["sexy", "champagne", "lungo"])
	
for key in text_style["gedicht"].keys():
	# def image_spice(genre, style, spice, mytext):
	character_spice("gedicht", key, ["sexy", "champagne", "lungo"])

