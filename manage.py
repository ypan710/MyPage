import utils
import sys


## loop through the files in content directory
#all_html_files = glob.glob("content/*.html")
#print(all_html_files)
#
## build up content from empty list

#for html_file in all_html_files:
#    # modify and extract useful parts from file paths
#    # file_path = "content/bio.html"
#    file_name = os.path.basename(html_file)
#    print(file_name)
#    name_only, extension = os.path.splitext(file_name)
#    print(name_only)
#    input = "content/" + file_name
#    output = "docs/" + file_name
#    pages.append({
#             "filename": input,
#             "output": output,
#             "title": name_only.capitalize(),
#             },)
#print(pages)

#pages.append({
#             "filename": "content/project.html",
#             "output": "docs/project.html",
#             "title": "My Projects",
#             },)
#pages.append({
#             "filename": "content/contact.html",
#             "output": "docs/contact.html",
#             "title": "Contact Me",
#             },)

# replace content holder with contents
#def apply_template(template, index_content):
#   result = template.replace("{{Content}}", str(index_content))
#   return result

# replace title holder with titles
#def apply_title(template, title_content):
#    result = template.replace("{{Title}}", str(title_content))
#    return result

# open and read the base file
#def read_template():
#    template = open("templates/base.html").read()
#    return template

def main():
    print("This is argv:", sys.argv)
    command = sys.argv[1]
    print(command)
    if command == "build":
        print("Build was specified")
        utils.build()
    elif command == "new":
        print("New page was specified")
        utils.new()
    else:
        print("Please specify 'build' or 'new'")

#    project_html = open("docs/project.html").read()
#    template_html = open("templates/base.html").read()
#    template = Template(template_html)
#    template.render(title="My Projects", content=project_html,)
#
#    contact_html = open("docs/contact.html").read()
#    template_html = open("templates/base.html").read()
#    template = Template(template_html)
#    template.render(title="Contact Me", content=contact_html,)


## loop through a list
#for page in pages:
#
#    # access data within dictionary
#    page_name = page["filename"]
#    page_output = page["output"]
#    page_title = page["title"]
#
#    # read in the entire template
#    template = read_template()
#
#        # read in the content of the index HTML page
#        index_content = open(page_name).read
#
#        # use the string replace
#        finished_index_page = apply_template(template, index_content)
#        finished_index_page = apply_title(finished_index_page, page_title)
#        open(page_output, "w+").write(finished_index_page)


if __name__ == "__main__":
    main()
