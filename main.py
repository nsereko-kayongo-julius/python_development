from bs4 import BeautifulSoup

with open('resume.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# print(soup.prettify())

# print(soup.title)
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

# using css selector

id = soup.select("#name")
print(id)

heading= soup.select(".heading")
print(heading
      )