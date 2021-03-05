from PIL import Image

# load images into Image() objects
words = Image.open('word_matrix.png')
word_masks = Image.open('mask.png')

# resize as per words size
print(words.size)
word_masks = word_masks.resize((1015, 559))

# adjust transparency of mask and paste mask on words
word_masks.putalpha(128)
words.paste(im=word_masks, box=(0, 0), mask=word_masks)
words.show()
