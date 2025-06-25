from slack.models import generate_image

def main():
    # Example usage
    title = "Sample Title"
    subtitle = "Sample Subtitle"
    author = "Sample Author"
    image_code = "1"  # Example image code
    theme = "0"  # Example theme
    guide_text_placement = 'bottom_right'
    guide_text = 'The Definitive Guide'

    image_path = generate_image(title, subtitle, author, image_code, theme, guide_text_placement, guide_text)
    print(f"Image generated at: {image_path}")

if __name__ == "__main__":
    main()