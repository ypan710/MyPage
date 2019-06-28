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

def apply_template(template,index_content):
    result = template.replace("{{Content}}", index_content)
    return result

def read_template():
    template = open("templates/base.html").read()
    return template

def main():

    # loop through a list
    for page in pages:

        # access data within dictionary
        page_name = page["filename"]
        page_output = page["output"]
        page_title = page["title"]

#        # open and read the files
#        top = open("templates/top.html").read()
#        content = open(page_name).read()
#        bottom = open("templates/bottom.html").read()
#        full = top + content + bottom
#        open(page_output, "w+").write(full)

        # read in the entire template
        template = read_template()
        
        # read in the content of the index HTML page
        index_content = open(page_name).read()
        
        # use the string replace
        finished_index_page = apply_template(template, index_content)
        open(page_output, "w+").write(finished_index_page)

        

    #top = open("templates/top.html").read()
    #project = open("content/project.html").read()
    #bottom = open("templates/bottom.html").read()
    #full_project = top + project + bottom
    #open("docs/project1.html", "w+").write(full_project)

    #top = open("templates/top.html").read()
    #contact = open("content/contact.html").read()
    #bottom = open("templates/bottom.html").read()
    #full_contact = top + contact + bottom
    #open("docs/contact1.html", "w+").write(full_contact)

if __name__ == "__main__":
    main()
