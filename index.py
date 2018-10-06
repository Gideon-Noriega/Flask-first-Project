from flask import Flask, flash,render_template, request, redirect, url_for, session
from project import Projectpy
import pygal
from user import Userpy
import json
import re

app = Flask(__name__)
app.secret_key = 'hsie7ry84yre8goiu928kdjhflho£"$£$%^'


def auth():
    if session:
        return True
    else:
        return False

@app.route('/register', methods=['POST'])
def register():
    #check if email exists
    try:
        Userpy.get(Userpy.email == request.form['email'])
        flash('User already Exists')
        return render_template('auth.html')
    except:
        if request.form['password']== request.form['confirm-password']:
        #if not exits create user
            user1 = Userpy(name = request.form['username'],
                email= request.form['email'],
                password = request.form['password'])
            user1.save()
        #set session
            session['Amen'] = True
            session['id'] = user1.id
            return  redirect(url_for('hello_world'))
        else:
            flash('Bad Credentials')
            return redirect(url_for('hello_world'))

@app.route('/login', methods=['POST'])
def login():
    try:
        user = Userpy.get(Userpy.email == request.form['email'], Userpy.password == request.form['password'])
        session['mse'] = True
        session['id'] = user.id
        flash('Logged in Succesfully')
        return redirect(url_for('hello_world'))
    except:
        flash('Bad Credentials')
        return render_template('auth.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('hello_world'))

@app.route('/')
def hello_world():
    if auth():
        return render_template('index.html',projectHtml = Projectpy.select().order_by(Projectpy.id),
                               bar_chart = barChart() ,piechart = piechart())
    else:
        return render_template('auth.html')

def barChart():
    bar_chart= pygal.StackedBar()
    datalist = []
    proselect = Projectpy.select()
    for amountkdj in proselect:
        datalist.append(amountkdj.amount)
    label1 = 'amount'
    bar_chart.add(label1, datalist)
    bar_chart = bar_chart.render_data_uri()
    return bar_chart

def piechart():
    piechart = pygal.Pie()
    piechart.title = 'Projects Pie'
    internal = 0
    external = 0
    none = 0
    proselect = Projectpy.select()
    for row in proselect:
        if row.type == 'Internal':
            internal = internal+1
        else:
            external = external+1

    piechart.add('External', external)
    piechart.add('Internal', internal)

    #piechart.add('None', none)
    pie_chart= piechart.render_data_uri()
    return pie_chart

# @app.route('/delete', methods=['POST', 'GET'])
# def deldata():
#     to_del = Projectpy.get(Projectpy.id == request.form['titleid'])
#     to_del.delete_instance()
#    # flash("Part deleted!", "success")
#     return redirect(url_for('hello_world'))


@app.route('/save', methods=['POST'])
def save():

    ProjectOne = Projectpy(title = request.form['titleform'],
                       startfrom = request.form['startDateForm'],
                       endat = request.form['endDateForm'],
                        type = request.form['typeForm'],
                       description = request.form['descriptionForm'],
                       amount = request.form['amountForm'],
                       status = 1)

    # save the insert data
    ProjectOne.save()
    flash("Project Save Successfully!", "success")
    return redirect(url_for('hello_world'))

@app.route('/update/<int:id>', methods=['POST'])
def updateproj(id):
    project = Projectpy.get(Projectpy.id == id)
    project.title = request.form['titlemodalform']
    project.startfrom = request.form['startDateForm']
    project.endat = request.form['endDateForm']
    project.type = request.form['typeForm']
    project.description = request.form['descriptionForm']
    project.amount = request.form['amountForm']
    project.status = 1
    project.save()
    flash("Projected Updated Successfully!", "success")
    return  redirect(url_for('hello_world'))
    #return str(id)

@app.route('/delete/<int:id>', methods=['GET'])
def deleteproject(id):
    #try:
        project = Projectpy.get(Projectpy.id == id)
        project.delete_instance()
        flash("Part deleted!", "success")
        return redirect(url_for('hello_world'))
    #except:
       # return 'Server Error'


@app.route('/chart')
def chart():
    #bar_chart = pygal.StackedBar
    # data = Projectpy.select()
    # datalist = []
    # for amountkdj in data:
    #     datalist.append(amountkdj.amount)
    # label1 = 'amount'
    # label2  = 'Fibonacci'
    # bar_chart.add(label1, datalist)
    # bar_chart = bar_chart.render_data_uri()
    #return render_template('chart.html', bar_chart = bar_chart)

    piechart = pygal.Pie()

    dataList = []
    internal = 0
    external = 0
    proselect = Projectpy.select()
    for row in proselect:
        if row == 'Internal':
            internal = internal+1
        else:
            external = external+1

    piechart.add('Internal', internal)
    piechart.add('External', external)
    piechart=piechart.render_data_uri()

    return render_template('chart.html', bar_chart = piechart)


@app.route('/data')
def data():
    return Projectpy.data



if __name__ == '__main__':
    app.run(debug = True)