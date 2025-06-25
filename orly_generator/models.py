import json, os, re, requests, random
from PIL import Image, ImageDraw, ImageFont
import datetime
from orly_generator.cache import get, set, clear  # Import cache functions directly
from fontTools.ttLib import TTFont

def get_text_size(draw, text, font, multiline=False):
    """Helper function to get text size compatible with both old and new Pillow versions"""
    if multiline:
        # For multiline text, we need to handle it differently
        lines = text.split('\n')
        total_width = 0
        total_height = 0
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            line_width = bbox[2] - bbox[0]
            line_height = bbox[3] - bbox[1]
            total_width = max(total_width, line_width)
            total_height += line_height
        return total_width, total_height
    else:
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

def generate_image(title, topText, author, image_code, theme, guide_text_placement='bottom_right', guide_text='The Definitive Guide'):
    cache_string = title + "_" + topText + "_" + author + "_" + image_code + "_" + theme + "_" + guide_text_placement + "_" + guide_text

    cached = get(cache_string)
    if cached:
        print("Cache hit")
        try:
            final_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), ('%s.png'%datetime.datetime.now())))
            width = 500
            height = 700
            im = Image.frombytes('RGBA', (width, height), cached)
            im.save(final_path)
            im.close()
            return final_path
        except Exception as e:
            print(str(e))
    else:
        print("Cache miss")

    themeColors = {
        "0" : (85,19,93,255),
        "1" : (113,112,110,255),
        "2" : (128,27,42,255),
        "3" : (184,7,33,255),
        "4" : (101,22,28,255),
        "5" : (80,61,189,255),
        "6" : (225,17,5,255),
        "7" : (6,123,176,255),
        "8" : (247,181,0,255),
        "9" : (0,15,118,255),
        "10" : (168,0,155,255),
        "11" : (0,132,69,255),
        "12" : (0,153,157,255),
        "13" : (1,66,132,255),
        "14" : (177,0,52,255),
        "15" : (55,142,25,255),
        "16" : (133,152,0,255),
    }
    themeColor = themeColors[theme]

    width = 500
    height = 700
    im = Image.new('RGBA', (width, height), "white")

    font_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fonts', 'Garamond Light.ttf'))
    font_path_helv = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fonts', 'HelveticaNeue-Medium.otf'))
    font_path_helv_bold = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fonts', 'Helvetica Bold.ttf'))
    font_path_italic = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fonts', 'Garamond LightItalic.ttf'))

    topFont = ImageFont.truetype(font_path_italic, 20)
    subtitleFont = ImageFont.truetype(font_path_italic, 34)
    authorFont = ImageFont.truetype(font_path_italic, 24)
    titleFont = ImageFont.truetype(font_path, 62)
    oriellyFont = ImageFont.truetype(font_path_helv, 28)
    questionMarkFont = ImageFont.truetype(font_path_helv_bold, 16)

    dr = ImageDraw.Draw(im)
    dr.rectangle(((20,0),(width-20,10)), fill=themeColor)

    topText = sanitzie_unicode(topText, font_path_italic)
    textWidth, textHeight = get_text_size(dr, topText, topFont)
    textPositionX = (width/2) - (textWidth/2)

    dr.text((textPositionX,10), topText, fill='black', font=topFont)

    author = sanitzie_unicode(author, font_path_italic)
    textWidth, textHeight = get_text_size(dr, author, authorFont)
    textPositionX = width - textWidth - 20
    textPositionY = height - textHeight - 20

    dr.text((textPositionX,textPositionY), author, fill='black', font=authorFont)

    oreillyText = "O RLY"

    textWidth, textHeight = get_text_size(dr, oreillyText, oriellyFont)
    textPositionX = 20
    textPositionY = height - textHeight - 20

    dr.text((textPositionX,textPositionY), oreillyText, fill='black', font=oriellyFont)

    oreillyText = "?"

    textPositionX = textPositionX + textWidth

    dr.text((textPositionX,textPositionY-1), oreillyText, fill=themeColor, font=questionMarkFont)

    titleFont, newTitle = clamp_title_text(sanitzie_unicode(title, font_path), width-80)
    if newTitle == None:
        raise ValueError('Title too long')

    textWidth, textHeight = get_text_size(dr, newTitle, titleFont, multiline=True)
    dr.rectangle([(20,400),(width-20,400 + textHeight + 40)], fill=themeColor)

    subtitle = sanitzie_unicode(guide_text, font_path_italic)

    if guide_text_placement == 'top_left':
        textWidth, textHeight = get_text_size(dr, subtitle, subtitleFont)
        textPositionX = 20
        textPositionY = 400 - textHeight - 2
    elif guide_text_placement == 'top_right':
        textWidth, textHeight = get_text_size(dr, subtitle, subtitleFont)
        textPositionX = width - 20 - textWidth
        textPositionY = 400 - textHeight - 2
    elif guide_text_placement == 'bottom_left':
        textPositionY = 400 + textHeight + 40
        textWidth, textHeight = get_text_size(dr, subtitle, subtitleFont)
        textPositionX = 20
    else:#bottom_right is default
        textPositionY = 400 + textHeight + 40
        textWidth, textHeight = get_text_size(dr, subtitle, subtitleFont)
        textPositionX = width - 20 - textWidth

    dr.text((textPositionX,textPositionY), subtitle, fill='black', font=subtitleFont)

    dr.multiline_text((40,420), newTitle, fill='white', font=titleFont)

    cover_image_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images', ('%s.png'%image_code)))
    coverImage = Image.open(cover_image_path).convert('RGBA')

    offset = (80,40)
    im.paste(coverImage, offset, coverImage)

    final_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), ('%s.png'%datetime.datetime.now())))
    im.save(final_path)

    set(cache_string, im.tobytes())
    im.close()

    return final_path

def clamp_title_text(title, width):
    im = Image.new('RGBA', (500,500), "white")
    dr = ImageDraw.Draw(im)

    font_path_italic = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'fonts', 'Garamond Light.ttf'))
    #try and fit title on one line
    font = None

    startFontSize = 80
    endFontSize = 61

    for fontSize in range(startFontSize,endFontSize,-1):
        font = ImageFont.truetype(font_path_italic, fontSize)
        w, h = get_text_size(dr, title, font)

        if w < width:
            return font, title

    #try and fit title on two lines
    startFontSize = 80
    endFontSize = 34

    for fontSize in range(startFontSize,endFontSize,-1):
        font = ImageFont.truetype(font_path_italic, fontSize)

        for match in list(re.finditer(r'\s',title, re.UNICODE)):
            newTitle = ''.join((title[:match.start()], '\n', title[(match.start()+1):]))
            substringWidth, h = get_text_size(dr, newTitle, font, multiline=True)

            if substringWidth < width:
                return font, newTitle

    im.close()

    return None, None

def sanitzie_unicode(string, font_file_path):
    sanitized_string = ''

    font = TTFont(font_file_path)
    cmap = font['cmap'].getcmap(3,1).cmap
    for char in string:
        code_point = ord(char)

        if code_point in cmap.keys():
            sanitized_string = ''.join((sanitized_string,char))

    return sanitized_string