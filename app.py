from bottle import route, run, static_file


@route('/')
def index():
    return static_file('index.html', root='./public/')

@route('/scripts/<filename>')
def scripts(filename):
    return static_file(filename, root='./public/')
    # this can't be a great idea but i don't wanna figure out the template stuff rn tbqh

@route('/data/<filename>')
def return_data(filename):
    return static_file(filename, root='./data/')

@route('/caddo.json')
def caddo():
    return static_file('caddo.json', root='./data/')

@route('/bossier.json')
def bossier():
    return static_file('bossier.json', root='./data/')


run(host='localhost', port=5000)
