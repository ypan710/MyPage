pages = [
        {
            "filename": "content/bio.html",
            "output": "docs/bio.html",
            "title": "About Me",
        },
        {
            "filename": "content/project.html",
            "output": "docs/project.html",
            "title": "My Projects",
        },
        {
            "filename": "content/contact.html",
            "output": "docs/contact.html",
            "title": "Contact me",
        },
    ]

# replace content holder with contents
def apply_template(template, index_content):
    result = template.replace("{{Content}}", str(index_content))
    return result

# replace title holder with titles
def apply_title(template, title_content):
    result = template.replace("{{Title}}", str(title_content))
    return result

# open and read the base file
def read_template():
    template = open("templates/base.html").read()
    return template

def main():

    # loop through a   list
    for page in pages:

        # access data within dictionary
        page_name = page["filename"]
        page_output = page["output"]
        page_title = page["title"]

        # read in the entire template
        template = read_template()
        
        # read in the content of the index HTML page
        index_content = open(page_name).read
        
        # use the string replace
        finished_index_page = apply_template(template, index_content)
        finished_index_page = apply_title(finished_index_page, page_title)
        open(page_output, "w+").write(finished_index_page)

if __name__ == "__main__":
    main()
