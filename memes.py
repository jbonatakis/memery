from PIL import Image, ImageDraw, ImageFont

import discord

# Embed default colors
error = 0xB22222
success = 0x207325

def distracted_boyfriend(message):
    image = Image.open('templates/boyfriend.jpg')

    color = 'rgb(0, 0, 0)' # black color
    stroke = 'rgb(255,255,255)'
    stroke_width = 3
    base_font_size = 70
    message_content = message.content.replace(" ", " \n").split("-")

    boyfriend = message_content[1]
    girlfriend = message_content[2]
    other_girl = message_content[3]

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('fonts/Roboto[wdth,wght].ttf', size=base_font_size)


    # draw the messages on the background
    (x, y) = (600, 400)
    draw.text((x, y), boyfriend, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    (x, y) = (875, 500)
    draw.text((x, y), girlfriend, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    (x, y) = (275, 450)
    draw.text((x, y), other_girl, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    # save the edited image
    image.save("output/boyfriend.jpg")


def whatcat(message):
    image = Image.open('templates/whatcat.jpg')

    color = 'rgb(0, 0, 0)'
    stroke = 'rgb(255,255,255)'
    stroke_width = 1
    base_font_size = 30
    max_length = 24
    message_content = message.content.split("-")

    if (len(message_content[1]) > max_length*2) or (len(message_content[2]) > max_length*2):
        pass
    else:
        line = 1
        woman = ""
        for word in message_content[1].split(" "):
            if len(woman) + len(word) < max_length:
                woman +=word
                woman += " "
            elif (len(woman) + len(word) > max_length) and line == 1:
                woman +='\n'
                woman += word
                woman += " "
                line += 1
            elif (len(woman) + len(word) > max_length) and line == 2:
                woman +=word
                woman += " "
    
    if len(message_content[2]) > max_length:
        cat = message_content[2][:max_length] + "\n" + message_content[2][max_length:]
    else:
        cat = message_content[2]


    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('fonts/Roboto[wdth,wght].ttf', size=base_font_size)


    # draw the messages on the background
    (x, y) = (10, 20)
    draw.text((x, y), woman, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    (x, y) = (350, 20)
    draw.text((x, y), cat, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    image.save("output/whatcat.jpg")


def two_buttons(message):
    image = Image.open('templates/two_buttons.jpg')

    color = 'rgb(0, 0, 0)' # black color
    stroke = 'rgb(255,255,255)'
    stroke_width = 3
    base_font_size = 70
    message_content = message.content.replace(" ", " \n").split("-")

    first_button = message_content[1]
    second_button = message_content[2]
    man = message_content[3]

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('fonts/Roboto[wdth,wght].ttf', size=base_font_size)


    # draw the messages on the background
    (x, y) = (130, 100)
    draw.text((x, y), first_button, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    (x, y) = (300, 70)
    draw.text((x, y), second_button, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    (x, y) = (275, 450)
    draw.text((x, y), man, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    # save the edited image
    image.save("output/two_buttons.jpg")


def handshake(message):
    image = Image.open('templates/handshake.jpg')

    color = 'rgb(0, 0, 0)' # black color
    stroke = 'rgb(255,255,255)'
    stroke_width = 3
    base_font_size = 35
    message_content = message.content.split("-")

    left_arm = message_content[1]
    right_arm = message_content[2]
    hands = message_content[3]

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('fonts/Roboto[wdth,wght].ttf', size=base_font_size)

    # draw the messages on the background
    (x, y) = (25, 300)
    draw.text((x, y), left_arm, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    (x, y) = (700, 250)
    draw.text((x, y), right_arm, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    (x, y) = (300, 100)
    draw.text((x, y), hands, fill=color, font=font, stroke_width=stroke_width, stroke_fill=stroke)

    # save the edited image
    image.save("output/handshake.jpg")



def give_help():
        embed = discord.Embed(description="Supported Memes", color=success)
        embed.add_field(name="Distracted Boyfriend", value="`!bf -<boyfriend> -<girlfriend> -<other girl>`", inline = True)
        embed.add_field(name="Two Buttons", value="`!buttons -<first button> -<second button> -<man>`", inline = True)
        embed.add_field(name="Woman Yelling at Cat", value="`!whatcat -<woman> -<cat>`", inline = True)
        embed.add_field(name="Interracial Handshake", value="`!handshake -<left arm> -<right arm> <hands>`", inline= True)

        return embed

