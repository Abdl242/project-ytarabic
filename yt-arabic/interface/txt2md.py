from bs4 import BeautifulSoup
import markdownify

def parse_to_markdown(path,text):



    # Save the markdown content to a file
    output_file_path = f"{path}.md"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)

    print(f"Markdown content has been saved to {output_file_path}.")
