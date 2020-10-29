from bottle import route, run, static_file


@route('/')
def index():
    return static_file('index.html', root='./public/')

@route('/caddo.json')
def caddo():
    with open('data/caddo.json', 'r') as f:
        data = f.read()
        f.close()
    return data

@route('/bossier.json')
def bossier():
    with open('data/bossier.json', 'r') as f:
        data = f.read()
        f.close()
    return data

run(host='localhost', port=5000)
