from flask import Flask, request, jsonify

app = Flask(__name__)

marks = [{'name':'A', 'maths':'90'},
        {'name':'B', 'maths':'78'},
        {'name':'C', 'maths':'80'},
        {'name':'D', 'maths':'70'},
        {'name':'E', 'maths':'96'}]

@app.route('/', methods=['GET'])
def hello_flask():
    return jsonify({'message':'Hello Flask'})
#http://127.0.0.1:5000

@app.route('/marks', methods=['GET'])
def marks_all():
    return jsonify({'marks':marks})
#http://127.0.0.1:5000/marks


@app.route('/marks/<string:name>', methods=['GET'])
def marks_name(name):
    m1 = marks[0]
    for i, q in enumerate(marks):
        if q['name']==name:
            m1 = marks[i]
    return jsonify({'marks':m1})
#http://127.0.0.1:5000/marks/A


@app.route('/marks', methods=['POST'])
def marks_Add():
    A1 = request.get_json(force=True)
    marks.append(A1)
    return jsonify({'marks':marks})
#http://127.0.0.1:5000/marks
#{"name":"Z", "maths":"70"}

@app.route('/marks/<string:name>', methods=['PUT'])
def marks_update(name):
    m1 = request.get_json(force=True)
    for i, q in enumerate(marks):
        if q['name']==name:
            marks[i] = m1
    qs = request.get_json()
    return jsonify({'marks':marks})
#http://127.0.0.1:5000/marks/A
#{"name":"A", "maths":"90"}

@app.route('/marks/<string:name>', methods=['DELETE'])
def marks_delete(name):
    m1 = request.get_json(force=True)
    for i, q in enumerate(marks):
        if q['name']==name:
            del marks[i]  
    return jsonify({'marks':marks})
#http://127.0.0.1:5000/marks/Z


if __name__== '__main__':
    app.debug=True
    app.run()