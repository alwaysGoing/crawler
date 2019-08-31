# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 16:18
# @Author  : Wang
# @FileName: test1.py
# @Software: PyCharm

from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

print('----------------------')
# 获取所有节点
print('获取所有节点')
result = html.xpath('//*')
print(result)

print('获取li节点')
result = html.xpath('//li')
print(result)
print(result[0])

print('选择li节点的所有直接a子节点')
result = html.xpath('//li/a')
print(result)

print('获取ul所有子孙节点，不包括直接子节点')
result = html.xpath('//ul//a')
print(result)

print('选中href属性为link4.html的a节点，然后获取其父节点，然后在获取其class属性')
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
print('也可以通过parent::来获取父节点')
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

# 利用@符号进行属性过滤
print('选取class为item-0的li节点')
result = html.xpath('//li[@class="item-0"]')
print(result)

print('获取li节点内部的文本，有两种方式')
print('第一种')
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)
print('第二种')
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

print('获取节点属性')
result = html.xpath('//li/a/@href')
print(result)

text = '''
<li class="li li-first"><a href="link.html">first item</li>
'''
html = etree.HTML(text)
print('属性多值匹配')
print("某些节点的属性可能有多个值")
result = html.xpath('//li[@class="li"]/a/text()')
print("li节点有两个属性，li和li-first，失效")
print(result)

result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

print("多属性匹配")
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

print('---------------------------------------------------')
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

print('排序选择')
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)
print('----------------------------------------------')

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
print('节点轴选择')
print('返回所有祖先节点')
result = html.xpath('//li[1]/ancestor::*')
print(result)
print('只返回div这个祖先节点')
result = html.xpath('//li[1]/ancestor::div')
print(result)
print('返回li节点所有的属性值')
result = html.xpath('//li[1]/attribute::*')
print(result)
print('选取直接子节点， 选取href为link1.html的a节点')
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
print('获取所有子孙节点，只选取span')
result = html.xpath('//li[1]/descendant::span')
print(result)
print('选取当前节点之后的所有节点')
result = html.xpath('//li[1]/following::*[2]')
print(result)
print('获取当前节点之后的所有同级节点')
result = html.xpath('//li[1]/following-sibling::*')
print(result)

