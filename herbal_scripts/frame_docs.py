### graphic
graphic_style_B = Style(name="red_style", family="graphic")
graphic_properties_B = GraphicProperties(border="1cm double #000000",
									padding="1cm",
									backgroundcolor="#ff0000")
graphic_style_B.addElement(graphic_properties_B)
beehive_B = beehive(myodt, graphic_style_B, "10cm", "15cm", "4cm", "4cm", "1")
frame_B = beehive_B["frame"]
textbox_B = beehive_B["textbox"]

### paragraphic
letter_style_B = Style(name="diluvienne_style",
					family="paragraph")
text_properties_B = TextProperties(fontsize="40pt",
									fontfamily="diluvienne")
letter_style_B.addElement(text_properties_B)
paragraph_properties_B = ParagraphProperties(textalign="left")
letter_style_B.addElement(paragraph_properties_B)
myodt.styles.addElement(letter_style_B)

text_unit(myodt, letter_style_B, "morning", textbox_B)
myodt.text.addElement(frame_B)
