from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return render_template("start_here.html")

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    play = request.args.get("yes")
    # not_play = request.args.get("no")

    if play:
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

    #return """This route worked!"""

@app.route('/madlib')
def show_madlib():
    celeb = request.args.get("celeb")
    thing = request.args.get("thing")
    adj = request.args.get("adj")
    color = request.args.get("color")

    return render_template("madlib.html", celeb=celeb, thing=thing, adj=adj, color=color)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
