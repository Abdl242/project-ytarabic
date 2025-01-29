from notion_client import Client
import os
# Initialize the Notion client
from params import *
notion = Client(auth=TOKEN)
# Function to read a markdown file
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Function to split content into chunks of 2000 characters
def split_content(content, max_length=2000):
    return [content[i:i + max_length] for i in range(0, len(content), max_length)]

# Function to save Markdown content as a Notion page
def save_markdown_as_page(parent_page_id, markdown_content, page_title):
    try:
        # Split the content into chunks
        content_chunks = split_content(markdown_content)

        # Create paragraph blocks for each chunk
        children = [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {"type": "text", "text": {"content": chunk}}
                    ]
                },
            }
            for chunk in content_chunks
        ]

        # Create the new page
        response = notion.pages.create(
            parent={"type": "page_id", "page_id": parent_page_id},
            properties={
                "title": [
                    {"type": "text", "text": {"content": page_title}}
                ]
            },
            children=children,
        )
        print("Page created successfully:", response["url"])
    except Exception as e:
        print("An error occurred while creating the page:", e)


def to_notion(file_path,parent_page_id,page_title):
    content=read_markdown_file(file_path)

    save_markdown_as_page(parent_page_id,content,page_title)
