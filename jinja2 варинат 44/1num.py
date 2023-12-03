from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template1.html')

param =[
 {'name': 'color',
 'list': ["синий", "зеленый","красный","оранжевый"],
 'cur': 1}
]
#result_html = template.render(param[0])
result_html = template.render(name="color",list=["синий", "зеленый","красный","оранжевый"],cur=2)
f = open('test.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
