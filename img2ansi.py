from PIL import Image

def load_image(image_path, width):
    image = Image.open(image_path)
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width * 0.5)
    image = image.resize((width, new_height))
    return image.convert('RGB')
def rgb_to_ansi(r, g, b):
    return 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)

def pixel_to_ansi(pixel):
    r, g, b = pixel
    ansi_code = rgb_to_ansi(r, g, b)
    return f"\033[38;5;{ansi_code}m█\033[0m"
def convert_to_ansi(image):
    ansi_art = ""
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            ansi_art += pixel_to_ansi(pixel)
        ansi_art += "\n"
    return ansi_art
def display_ansi_art(ansi_art):
    print(ansi_art)
def save_ansi_art(ansi_art, outfile):
    if not outfile == "":
        save = open(outfile, 'w')
        save.write(ansi_art)

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    width = input("Enter ANSI art width: ")
    outfile = input("Enter the path to the saved art: ")
    image = load_image(image_path, int(width))
    ansi_art = convert_to_ansi(image)
    display_ansi_art(ansi_art)
    save_ansi_art(ansi_art, outfile)
