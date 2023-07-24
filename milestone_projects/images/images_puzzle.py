from PIL import Image

mac = Image.open("milestone_projects/impages/example.jpg")

# mac.show()
print(type(mac))
print(f"image size: {mac.size}")
print(mac.filename)
print(mac.format_description)

mac_cropped = mac.crop((1993/2 -200, 800, 1993/2 + 200, 1257))
# mac_cropped.show()

# copy images
mac.paste(mac_cropped, (0, 0))
mac.paste(mac_cropped, (796, 0))
mac.paste(mac_cropped, (1592, 0))
mac.paste(mac_cropped, (0, 800))
mac.paste(mac_cropped, (1592, 800))

# resize
mac_resized = mac.resize((3000, 200))
mac_resized.show()

# rotate
mac_rotated = mac.rotate(90)
mac_rotated.show()

# # save 
# mac.save("mult_macs.jpg")
# mac.close()

# mult_macs = Image.open("mult_macs.jpg")
# # mult_macs.show()
# mult_macs.close()

# pencils = Image.open("milestone_projects/impages/pencils.jpg")
# print(pencils.size)
# pencils_cropped = pencils.crop((0, 1100, 1950/3, 1300))
# # pencils_cropped.show()

# red = Image.open("milestone_projects/impages/red_color.jpg")
# red.show()
# red.putalpha(0)
# red.show()
# red.putalpha(128)
# red.show()

# blue = Image.open("milestone_projects/impages/blue_color.png")
# blue.show()

# purple = blue.paste(im = red, box = (0, 0), mask = red)
# blue.show()

# word = Image.open("milestone_projects/impages/word_matrix.png")
# print(f"word size: {word.size}")

# mask = Image.open("milestone_projects/impages/mask.png")
# mask_resized = mask.resize((1015, 559))
# print(f"mask size: {mask_resized.size}")
# mask_resized.putalpha(128)

# word.paste(mask_resized, (0, 0), mask_resized)

# word.show()


