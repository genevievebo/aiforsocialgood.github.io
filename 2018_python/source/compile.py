## -*- coding: utf-8 -*-
import re
import os
import sys
import json

from mako.template import Template
from mako.lookup import TemplateLookup

reg = "\$\{[^$]*\}"

custom = json.loads(open('custom.json').read())

mylookup = TemplateLookup(directories=['.'],strict_undefined=False, input_encoding='utf-8')

sections = [s for s in os.listdir(".") if "compile" not in s and not s.startswith('.')]
sections.remove("custom.json")
sections.remove("header")
sections.remove("footer")


for section_name in sections :
	attributes = custom['default'] 
	attributes.update(custom.get(section_name, {}))
	
	html = """<%include file="header"/> <%include file="{}"/>  <%include file="footer"/>""".format(section_name)
	
	section = Template(html, lookup=mylookup, strict_undefined=False)
	
	
	try : 
		s = section.render(**attributes)
		outfile = open('../new/%s.html' % section_name, "w")
		outfile.write(str(s))
		outfile.close()


	except Exception as e: 
		print("Missing value")
		print(section_name, re.findall(reg, open(section_name).read()))
		print(section_name, re.findall(reg, open("footer").read()))
		print(section_name, re.findall(reg, open("header").read()))




