from flask import Flask, request, session, redirect, jsonify
from flask.templating import render_template
from entries_manager import EntriesManager


app = Flask(__name__)
# app.secret_key = 'ildar'  

# переделать
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/create-entrie', methods=['GET'])
def create_get():
    return render_template('create.html')

@app.route('/create-entrie', methods=['POST'])
def create_post():
    entry_data = EntriesManager.request_data(request.form)
    EntriesManager.create_entry(**entry_data)
    return redirect('/entries-list')

# отдал джейсоны
@app.route('/entries-list')
def entires_list():
    return jsonify(EntriesManager.find_all())

# отдал джейсон
@app.route('/entry/<int:id>')
def entry(id):
    return EntriesManager.json_find_by(id=id)

# отдал джейсон
@app.route('/entry/<int:id>/change', methods=['GET'])
def change(id):
    return EntriesManager.json_find_by(id=id)

# принимаю джейсон, меняю и сохраняю в базу
@app.route('/entry/<int:id>/change', methods=['POST'])
def change_post(id):
    new_entry_data = EntriesManager.request_data(request.form)
    editing_entry = EntriesManager.find_by(id=id)
    EntriesManager.change_entry(editing_entry, new_entry_data)

@app.route('/entry/<int:id>/delete')
def remove_entrie(id):
    removing_entrie = EntriesManager.find_by(id=id)
    EntriesManager.remove_file(removing_entrie)
    return redirect('/entries-list')

















