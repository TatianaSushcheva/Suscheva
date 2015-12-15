# encoding=utf-8
import lxml.html as html

page = html.parse('http://www.spletnik.ru/buzz/chronicle')
root = page.getroot()
tag = root.find_class('b-article').pop()

url_list = []

for i in tag.iterlinks():
    if i[2].find('comments') == -1 and i[2].find('jpg') == -1 and i[2].find('html') != -1:
        url_list.append(i[2])

url_list = url_list[::2]

metadata = []
texts = []

for url in url_list:
    page1 = html.parse(url)
    root1 = page1.getroot()
    tag1 = root1.find_class('b-meta').pop()
    an = tag1.text_content().strip()
    metadata.append(an)
    tag2 = root1.find_class('b-article-text clear').pop()
    ben = tag2.text_content().strip()
    texts.append(ben)

a = open('kebab_output.txt', 'w')
for i in range(len(url_list)):
    a.write(url_list[i]+'\n')
    a.write(metadata[i]+'\n')
    a.write(texts[i]+'n')
a.close()

from lxml import etree
root = etree.Element('spletnik_articles')
for i in range(len(url_list)):
    tag = etree.SubElement(root, 'article')
    subtag = etree.SubElement(tag, 'url').text = url_list[i]
    subtag2 = etree.SubElement(tag, 'text').text = texts[i]
    subtag3 = etree.SubElement(tag, 'metadata').text = metadata[i]

new_xml = etree.tostring(root, pretty_print=True, encoding='utf-8')
a = open('kebabi.xml', 'wb')
a.write(new_xml)
a.close()