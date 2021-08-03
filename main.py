from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from recipe_search import recipe_serch
import uvicorn

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")



@app.route('/recipe', methods=['POST', 'GET'])  # route to show the review comments in a web UI
@cross_origin()
def find_recipe():
    if request.method == 'POST':
        try:
            user_input=(request.form['search-input'])
            recipe_list=recipe_serch(user_input)
            print(recipe_list)
            return render_template('index.html', recipe_list=recipe_list)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=8001, debug=True)

    # to run on cloud Heroku
    app.run(debug=True)