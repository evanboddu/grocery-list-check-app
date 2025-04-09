from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for grocery items
grocery_list = []

@app.route('/')
def index():
    return render_template('index.html', grocery_list=grocery_list)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        grocery_list.append({'name': item, 'checked': False})
    return redirect(url_for('index'))

@app.route('/check/<int:item_id>')
def check_item(item_id):
    if 0 <= item_id < len(grocery_list):
        grocery_list[item_id]['checked'] = not grocery_list[item_id]['checked']
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    if 0 <= item_id < len(grocery_list):
        grocery_list.pop(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)