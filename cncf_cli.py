from flask import Flask, request, render_template
import yaml

app = Flask(__name__, static_url_path='/static')

def get_project_name(project_name): 
    project_name = project_name.lower().title()
    with open('projects.yml') as y:
        landscape = yaml.safe_load(y)
        for category in landscape.get('landscape', []):
            subcategories = category.get('subcategories', [])
            for subcategory in subcategories:
                items = subcategory.get('items', [])
                for item in items:
                    if item.get('name') == project_name:
                        category_name = category.get('name')
                        subcategory_name = subcategory.get('name')
                        item_details = {
                            key.capitalize(): value for key, value in item.items()
                        }
                        return category_name, subcategory_name, item_details

        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        project_name = request.form.get('project_name')
        category_name, subcategory_name, item_details = get_project_name(project_name)
        if item_details:
            return render_template('index.html', category=category_name, subcategory=subcategory_name, details=item_details)
        else:
            return render_template('index.html', error_message=f"Project '{project_name}' not found.")
    return render_template('index.html', category=None, subcategory=None, details=None)


if __name__ == '__main__':
    app.run()
