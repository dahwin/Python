from PIL import Image, ImageDraw

# Create a white full HD image (1920x1080)
image = Image.new("RGB", (1920, 1080), "white")
draw = ImageDraw.Draw(image)

# Define the coordinates of the box (1500, 200, 160, 241)
box_coordinates = (1500, 200, 1660, 441)  # Adjusted to match (160, 241) size

# Draw a red rectangle (box) on the image
draw.rectangle(box_coordinates, outline="red", width=2)

# Save the image
image.save("full_hd_image_with_box.png")

# Show the image
image.show()
