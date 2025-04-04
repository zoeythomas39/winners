from flask import Flask, render_template
from modules import convert_to_dict

app = Flask(__name__)
application = app

# create a list of dicts from a CSV
actresses_list = convert_to_dict("actresses.csv")

# create a list of tuples in which the first item is the number
# (Presidency) and the second item is the name (President)
pairs_list = []
for p in actresses_list:
    pairs_list.append( (p['actressrank'], p['winner']) )

# first route

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Actresses Index")

# second route

@app.route('/actress/<num>')
def detail(num):
    try:
        actress_dict = actresses_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Actress Rank: {num}</h1>"
    # a little bonus function, imported on line 2 above
    return render_template('actress.html', actress=actress_dict,the_title=actress_dict['winner'])


# keep this as is
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999, debug=True)