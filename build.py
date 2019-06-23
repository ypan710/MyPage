head1 = open("templates/top.html").read()
body1 = open("content/bio.html").read()
bottom1 = open("templates/bottom.html").read()
full1 = head1 + body1 + bottom1
open("docs/bio1.html", "w+").write(full1)

head2 = open("templates/top.html").read()
body2 = open("content/project.html").read()
bottom2 = open("templates/bottom.html").read()
full2 = head2 + body2 + bottom2
open("docs/project1.html", "w+").write(full2)

head3 = open("templates/top.html").read()
body3 = open("content/contact.html").read()
bottom3 = open("templates/bottom.html").read()
full3 = head3 + body3 + bottom3
open("docs/contact1.html", "w+").write(full3)
