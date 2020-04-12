from flask import render_template, url_for, request
from flask import Flask
import sqlite3
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index/')
@app.route('/start/')
def index():
    return render_template('main_page.html', link=url_for('static', filename='css/style.css'))


@app.route('/compilation', methods=['POST', 'GET'])
def compilation():
    if request.method == 'GET':
        return render_template('compilation.html', link=url_for('static', filename='css/style.css'))
    elif request.method == 'POST':
        twenty_fst = request.form["21"]
        twenty_snd = request.form["22"]
        twenty_trd = request.form["23"]
        twenty_fth = request.form["24"]
        twenty_fifth = request.form["25"]
        twenty_sixth = request.form["26"]
        file = "compilation.txt"
        f = open(file, 'w').close()
        f = open(file, encoding="utf8", mode="w")

        con = sqlite3.connect("tasks.db")
        cur = con.cursor()
        string = """SELECT * FROM '21'"""
        res = cur.execute(string).fetchall()
        result = [elem[1] for elem in res]
        answers = [elem[2] for elem in res]
        lst = []
        for i in range(twenty_fst):
            n = random.choice(range(1, 15))
            while n in lst:
                n = random.choice(range(1, 15))
            lst.append(n)
        for elem in lst:
            print(result[elem])
            print("Ответ:", answers[elem])
            print()

        string = """SELECT * FROM '22'"""
        res = cur.execute(string).fetchall()
        result = [elem[1] for elem in res]
        answers = [elem[2] for elem in res]
        lst = []
        for i in range(twenty_snd):
            n = random.choice(range(1, 15))
            while n in lst:
                n = random.choice(range(1, 15))
            lst.append(n)
        for elem in lst:
            print(result[elem])
            print("Ответ:", answers[elem])
            print()

        string = """SELECT * FROM '23'"""
        res = cur.execute(string).fetchall()
        result = [elem[1] for elem in res]
        answers = [elem[2] for elem in res]
        lst = []
        for i in range(twenty_trd):
            n = random.choice(range(1, 15))
            while n in lst:
                n = random.choice(range(1, 15))
            lst.append(n)
        for elem in lst:
            print(result[elem])
            print("Ответ:", answers[elem])
            print()

        string = """SELECT * FROM '24'"""
        res = cur.execute(string).fetchall()
        result = [elem[1] for elem in res]
        answers = [elem[2] for elem in res]
        lst = []
        for i in range(twenty_fth):
            n = random.choice(range(1, 15))
            while n in lst:
                n = random.choice(range(1, 15))
            lst.append(n)
        for elem in lst:
            print(result[elem])
            print("Ответ:", answers[elem])
            print()

        string = """SELECT * FROM '25'"""
        res = cur.execute(string).fetchall()
        result = [elem[1] for elem in res]
        answers = [elem[2] for elem in res]
        lst = []
        for i in range(twenty_fifth):
            n = random.choice(range(1, 15))
            while n in lst:
                n = random.choice(range(1, 15))
            lst.append(n)
        for elem in lst:
            print(result[elem])
            print("Ответ:", answers[elem])
            print()

        string = """SELECT * FROM '26'"""
        res = cur.execute(string).fetchall()
        result = [elem[1] for elem in res]
        answers = [elem[2] for elem in res]
        lst = []
        for i in range(twenty_sixth):
            n = random.choice(range(1, 15))
            while n in lst:
                n = random.choice(range(1, 15))
            lst.append(n)
        for elem in lst:
            print(result[elem])
            print("Ответ:", answers[elem])
            print()
        f.close()
        f = open(file, encoding="utf8", mode="r")
        print(f.read())
        return render_template('result.html', link=url_for('static', filename='css/style.css'))
                               # comp_file=url_for('static', filename='compilation.txt'))


@app.route('/random_tasks', methods=['POST', 'GET'])
def random_tasks():
    lst = []
    data = []
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM '21'"""
    res = cur.execute(string).fetchall()
    result = [elem[1] for elem in res]
    n = random.choice(range(1, 15))
    lst.append(result[n])
    data.append(res[n])
    string = """SELECT * FROM '22'"""
    res = cur.execute(string).fetchall()
    result = [elem[1] for elem in res]
    n = random.choice(range(1, 15))
    lst.append(result[n])
    data.append(res[n])
    string = """SELECT * FROM '23'"""
    res = cur.execute(string).fetchall()
    result = [elem[1] for elem in res]
    n = random.choice(range(1, 15))
    lst.append(result[n])
    data.append(res[n])
    string = """SELECT * FROM '24'"""
    res = cur.execute(string).fetchall()
    result = [elem[1] for elem in res]
    n = random.choice(range(1, 15))
    lst.append(result[n])
    data.append(res[n])
    string = """SELECT * FROM '25'"""
    res = cur.execute(string).fetchall()
    result = [elem[1] for elem in res]
    n = random.choice(range(1, 15))
    lst.append(result[n])
    data.append(res[n])
    string = """SELECT * FROM '26'"""
    res = cur.execute(string).fetchall()
    result = [elem[1] for elem in res]
    n = random.choice(range(1, 15))
    lst.append(result[n])
    data.append(res[n])
    con.close()
    right = []
    for elem in data:
        right.append(elem[2])
        print(elem[2])
    file = "right.txt"
    f_1 = open(file, encoding="utf8", mode="r")
    if f_1.read() == "":
        f = open(file, encoding="utf8", mode="w")
        f.truncate()
        print(", ".join(right), file=f)
        f.close()
    for elem in lst:
        print(elem)
    if request.method == 'GET':
        return render_template('random_tasks.html', link=url_for('static', filename='css/style.css'), task_1=lst[0],
                               task_2=lst[1], task_3=lst[2], task_4=lst[3], task_5=lst[4], task_6=lst[5], verdict=" ")
    elif request.method == 'POST':
        line = ""
        line += request.form["answer_1"] + ", "
        line += request.form["answer_2"] + ", "
        line += request.form["answer_3"] + ", "
        line += request.form["answer_4"] + ", "
        line += request.form["answer_5"] + ", "
        line += request.form["answer_6"]
        file = "right.txt"
        f = open(file, encoding="utf8", mode="r")
        final = f.read()
        f.close()
        f = open(file, 'w').close()
        print("4", open(file, 'r').read())
        return render_template('result.html', link=url_for('static', filename='css/style.css'), ready=line, verdict=final)


@app.route('/21')
def first():
    return render_template('first.html', link=url_for('static', filename='css/style.css'))


@app.route('/21/<int:number>', methods=['POST', 'GET'])
def first_tasks(number):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM "21"
                WHERE {}""".format("ID = " + str(number))
    result = cur.execute(string).fetchall()
    res = result[0]
    con.close()
    if request.method == 'GET':
        return render_template('21_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                               task=res[1], verdict=" ")
    elif request.method == 'POST':
        if request.form['answer'] == res[2]:
            return render_template('21_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="OK")
        else:
            return render_template('21_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="ERROR")


@app.route('/21/answers')
def first_ans():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM '21'"""
    res = cur.execute(string).fetchall()
    result = [elem[2] for elem in res]
    answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, \
        answer_12, answer_13, answer_14, answer_15 = result
    con.close()
    return render_template('21_ans.html', link=url_for('static', filename='css/style.css'), ans_1=answer_1,
                           ans_2=answer_2, ans_3=answer_3, ans_4=answer_4, ans_5=answer_5, ans_6=answer_6,
                           ans_7=answer_7, ans_8=answer_8, ans_9=answer_9, ans_10=answer_10, ans_11=answer_11,
                           ans_12=answer_12, ans_13=answer_13, ans_14=answer_14, ans_15=answer_15)


@app.route('/22')
def second():
    return render_template('second.html', link=url_for('static', filename='css/style.css'))


@app.route('/22/<int:number>', methods=['POST', 'GET'])
def second_tasks(number):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM "22"
                    WHERE {}""".format("ID = " + str(number))
    result = cur.execute(string).fetchall()
    res = result[0]
    con.close()
    if request.method == 'GET':
        return render_template('22_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                               task=res[1], verdict=" ")
    elif request.method == 'POST':
        if request.form['answer'] == res[2]:
            return render_template('22_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="OK")
        else:
            return render_template('22_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="ERROR")


@app.route('/22/answers')
def second_ans():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM '22'"""
    res = cur.execute(string).fetchall()
    result = [elem[2] for elem in res]
    answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, \
        answer_12, answer_13, answer_14, answer_15 = result
    con.close()
    return render_template('22_ans.html', link=url_for('static', filename='css/style.css'), ans_1=answer_1,
                           ans_2=answer_2, ans_3=answer_3, ans_4=answer_4, ans_5=answer_5, ans_6=answer_6,
                           ans_7=answer_7, ans_8=answer_8, ans_9=answer_9, ans_10=answer_10, ans_11=answer_11,
                           ans_12=answer_12, ans_13=answer_13, ans_14=answer_14, ans_15=answer_15)


@app.route('/23')
def third():
    return render_template('third.html', link=url_for('static', filename='css/style.css'))


@app.route('/23/<int:number>', methods=['POST', 'GET'])
def third_tasks(number):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM "23"
                    WHERE {}""".format("ID = " + str(number))
    result = cur.execute(string).fetchall()
    res = result[0]
    con.close()
    if request.method == 'GET':
        return render_template('23_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                               task=res[1], verdict=" ")
    elif request.method == 'POST':
        if request.form['answer'] == res[2]:
            return render_template('23_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="OK")
        else:
            return render_template('23_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="ERROR")


@app.route('/23/answers')
def third_ans():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM '23'"""
    res = cur.execute(string).fetchall()
    result = [elem[2] for elem in res]
    answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, \
        answer_12, answer_13, answer_14, answer_15 = result
    con.close()
    return render_template('23_ans.html', link=url_for('static', filename='css/style.css'), ans_1=answer_1,
                           ans_2=answer_2, ans_3=answer_3, ans_4=answer_4, ans_5=answer_5, ans_6=answer_6,
                           ans_7=answer_7, ans_8=answer_8, ans_9=answer_9, ans_10=answer_10, ans_11=answer_11,
                           ans_12=answer_12, ans_13=answer_13, ans_14=answer_14, ans_15=answer_15)


@app.route('/24')
def fourth():
    return render_template('fourth.html', link=url_for('static', filename='css/style.css'))


@app.route('/24/<int:number>', methods=['POST', 'GET'])
def fourth_tasks(number):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM "24"
                    WHERE {}""".format("ID = " + str(number))
    result = cur.execute(string).fetchall()
    res = result[0]
    con.close()
    if request.method == 'GET':
        return render_template('24_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                               task=res[1], verdict=" ")
    elif request.method == 'POST':
        if request.form['answer'] == res[2]:
            return render_template('24_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="OK")
        else:
            return render_template('24_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="ERROR")


@app.route('/24/answers')
def fourth_ans():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM '24'"""
    res = cur.execute(string).fetchall()
    result = [elem[2] for elem in res]
    answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, \
        answer_12, answer_13, answer_14, answer_15 = result
    con.close()
    return render_template('24_ans.html', link=url_for('static', filename='css/style.css'), ans_1=answer_1,
                           ans_2=answer_2, ans_3=answer_3, ans_4=answer_4, ans_5=answer_5, ans_6=answer_6,
                           ans_7=answer_7, ans_8=answer_8, ans_9=answer_9, ans_10=answer_10, ans_11=answer_11,
                           ans_12=answer_12, ans_13=answer_13, ans_14=answer_14, ans_15=answer_15)


@app.route('/25')
def fifth():
    return render_template('fifth.html', link=url_for('static', filename='css/style.css'))


@app.route('/25/<int:number>', methods=['POST', 'GET'])
def fifth_tasks(number):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM "25"
                    WHERE {}""".format("ID = " + str(number))
    result = cur.execute(string).fetchall()
    res = result[0]
    con.close()
    if request.method == 'GET':
        return render_template('25_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                               task=res[1], verdict=" ")
    elif request.method == 'POST':
        if request.form['answer'] == res[2]:
            return render_template('25_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="OK")
        else:
            return render_template('25_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="ERROR")


@app.route('/25/answers')
def fifth_ans():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM '25'"""
    res = cur.execute(string).fetchall()
    result = [elem[2] for elem in res]
    answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, \
        answer_12, answer_13, answer_14, answer_15 = result
    con.close()
    return render_template('25_ans.html', link=url_for('static', filename='css/style.css'), ans_1=answer_1,
                           ans_2=answer_2, ans_3=answer_3, ans_4=answer_4, ans_5=answer_5, ans_6=answer_6,
                           ans_7=answer_7, ans_8=answer_8, ans_9=answer_9, ans_10=answer_10, ans_11=answer_11,
                           ans_12=answer_12, ans_13=answer_13, ans_14=answer_14, ans_15=answer_15)


@app.route('/26')
def sixth():
    return render_template('sixth.html', link=url_for('static', filename='css/style.css'))


@app.route('/26/<int:number>', methods=['POST', 'GET'])
def sixth_tasks(number):
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM "26"
                    WHERE {}""".format("ID = " + str(number))
    result = cur.execute(string).fetchall()
    res = result[0]
    con.close()
    if request.method == 'GET':
        return render_template('26_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                               task=res[1], verdict=" ")
    elif request.method == 'POST':
        print(request.form['answer'])
        if request.form['answer'] == res[2]:
            return render_template('26_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="OK")
        else:
            return render_template('26_tasks.html', link=url_for('static', filename='css/style.css'), number=number,
                                   task=res[1], verdict="ERROR")


@app.route('/26/answers')
def sixth_ans():
    con = sqlite3.connect("tasks.db")
    cur = con.cursor()
    string = """SELECT * FROM '26'"""
    res = cur.execute(string).fetchall()
    result = [elem[2] for elem in res]
    answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10, answer_11, \
        answer_12, answer_13, answer_14, answer_15 = result
    con.close()
    return render_template('26_ans.html', link=url_for('static', filename='css/style.css'), ans_1=answer_1,
                           ans_2=answer_2, ans_3=answer_3, ans_4=answer_4, ans_5=answer_5, ans_6=answer_6,
                           ans_7=answer_7, ans_8=answer_8, ans_9=answer_9, ans_10=answer_10, ans_11=answer_11,
                           ans_12=answer_12, ans_13=answer_13, ans_14=answer_14, ans_15=answer_15)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
