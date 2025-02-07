import markdown


def markdown_to_html(md_file_path, html_file_path):
    # Read the Markdown file
    with open(md_file_path, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Write the HTML to a file
    with open(html_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    # Specify your input and output file paths
    md_file_path = "test.md"  # Markdown file to be converted
    html_file_path = "output.html"  # Desired output HTML file

    markdown_to_html(md_file_path, html_file_path)
    print(f"Converted {md_file_path} to {html_file_path}")
