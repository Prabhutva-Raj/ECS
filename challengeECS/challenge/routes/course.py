"""Routes for the course resource.
"""

from run import app
from flask import request, render_template, redirect
from http import HTTPStatus
import data
import json
import datetime



@app.route("/courselist")		##
def get_course_list():
    return render_template('course.html',result=data.courses.values())

@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    if request.method=='GET':
        result = {}
        try:
            result.update(data.courses[id])
        except:
            pass
    return result
    

@app.route("/filter_courses", methods=['POST','GET'])
def get_courses():
    words = []
    filtered_result = []
    if request.method == 'POST':
        words = request.form
        
    words = list(map(str,words['words'].split(",")))
    
    for item in data.courses.values():
        for w in words:
            if w.lower() in item['title'].lower():
                filtered_result.append(item)
    return render_template('course.html',result=filtered_result )    
    
    


@app.route("/add")
def add():
    return render_template('add.html')  

@app.route("/course", methods=['POST'])
def create_course():
    if request.method == 'POST':
        item = request.form
        #item.update({"date_created":datetime.datetime.now()})
        data.courses.update({item['id']:item})
    print("Item added")
    return redirect("/courselist")  
    

@app.route("/update/<int:id>")
def update(id):
    return render_template('update.html',result=data.courses[id])  

@app.route("/course_update/<int:id>", methods=['POST'])
def update_course(id):
    #id = str(id)
    item = request.form
    if item['title']!="":
        data.courses[id]['title']=item['title']
    if item['description']!="":
        data.courses[id]['description']=item['description']
    if item['price']!="":
        data.courses[id]['price']=item['price']
    if item['discount_price']!="":
        data.courses[id]['discount_price']=item['discount_price']
    if item['on_discount']!="":
        data.courses[id]['on_discount']=item['on_discount']
    data.courses[id]['date_updated']=datetime.datetime.now()
    return redirect("/courselist")




@app.route("/course_delete/<int:id>")
def delete_course(id):
    del data.courses[id]
    print("Item deleted")
    return redirect("/courselist")

