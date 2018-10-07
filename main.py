from bottle import route, run, template, get, post, request
from bottle import static_file
from api import get_students, get_similar_docs
import logging
import sys


title = "#bettertogether"
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@route('/')
def welcome():
    return template('welcome', title=title)


@get('/inputs')
def inputs():
    info = {'title': title, 'students': get_students()}
    return template('inputs', info)


@post('/plot')
def formhandler():
    student = request.forms.get('student')
    assignment = request.forms.get('assignment')
    similar_docs = get_similar_docs(student, assignment)
    info = {'student': student, 'assignment': assignment, 'similar_docs': similar_docs}
    return template('plot', info)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


if __name__ == '__main__':
    run()
