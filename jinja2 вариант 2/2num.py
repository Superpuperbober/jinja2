from jinja2 import Environment, FileSystemLoader
import array
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template2.html')
n =100
a = 0
b = 100
step = (b-a)/n
x = a

def f(x):
  return x**2


def y(x):
 return x**3


param = {
 'x': [],
 'f(x)': [],
 'y(x)': []
}

while x <= b:
 param['x'].append(x)
 param['f(x)'].append(f(x))
 param['y(x)'].append(y(x))
 x += step

print(param)

result_html = template.render(list=param, first=7, last=8)
f = open('test.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()