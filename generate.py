import sys
import yaml
import itertools

data_file = "data.yml"
html_template_file = "template.html"
output_file = "build/index.html"

item_template = """
<li class="item">
	<span class="li-content">
		<span>{year}</span>
		–
		<span>{name}</span>
	</span>
</li>
"""

empty_item = """<li class="empty">&nbsp;</li>"""

with open(html_template_file) as f:
	html_template = f.read()

with open(data_file) as f:
	data = yaml.safe_load(f)

data_by_year = dict((y, list(item)) for y,item in itertools.groupby(data, lambda x: x['year']))
max_per_year = max(len(x) for x in data_by_year.values())
max_year = max(data_by_year.keys())

content = ""
for year in range(min(data_by_year.keys()), max_year + 1):
	items = data_by_year.get(year, list())
	for item in items:
		content += item_template.format(year=item['year'], name=item['name'])
	if (year != max_year):
		for _ in range(max_per_year-len(items)):
			content += empty_item

with open(output_file, "w") as f:
	f.write(html_template.format(content=content))


