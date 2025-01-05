from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

id_attr = soup.find_all(id="boldest")
print("ID Attribute is: ", id_attr)

tag_object = soup.title
print("tag object:", tag_object)

print("tag object type:", type(tag_object))

tag_object = soup.h3
tag_object

tag_child = tag_object.b
tag_child

parent_tag = tag_child.parent
parent_tag

tag_object.parent

sibling_1 = tag_object.next_sibling
sibling_1

sibling_2 = sibling_1.next_sibling
sibling_2

sibling_3 = sibling_2.next_sibling
print("Sibling 3 is: ", sibling_3)


table = "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> \
<td>Payload mass</td></tr><tr> <td>1</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td> \
<td>300 kg</td></tr><tr><td>2</td> \
<td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td> \
<td>94 kg</td></tr><tr><td>3</td> \
<td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td> \
<td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, 'html5lib')

table_rows = table_bs.find_all('tr')
table_rows

first_row = table_rows[0]
first_row

first_row.td

for i, row in enumerate(table_rows):
    print("row", i, "is", row)


for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('column', j, "cell", cell)

list_input = table_bs.find_all(name=["tr", "td"])
list_input

list_input = table_bs.find_all(id="flight")
print(list_input)

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

print(table_bs.find_all('a', href=True))

print(table_bs.find_all('a', href=False))

print(table_bs.find_all(string="Florida"))


