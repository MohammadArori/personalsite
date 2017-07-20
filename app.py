from flask import Flask, render_template
import random
app= Flask(__name__)

@app.route('/<name>')
def about1(name):
	title= "About me "
	return render_template("about.html", title=title, name= name)

@app.route('/about.html')
def about():
	title= "About "
	return render_template("about.html", title=title, )


@app.route('/albums.html')
def albums():
	
	return render_template("albums.html", title= "albums", )


@app.route('/list.html')
def listEX():
	test= ["riff cohen" , "naom chomsky" , "steven hawkings" , "van gogh" , "fadi abuhomos"]
	display= True
	return render_template("list.html", display=display, list=test, )



# @app.route('/hey')
# def hello():
# 	Q1="The best preparation for tomorrow is doing your best today."
# 	Q2="<h2>Put your heart, mind,  soul into even your smallest acts. This  the secret of success.  </h2>"
# 	Q3="Don't cry because it's over, smile because it happened."
# 	Q4="Be yourself; everyone else is already taken"
# 	Q5="Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
# 	Q= [Q1,Q2,Q3,Q4,Q5]
# 	return random.choice(Q)




if __name__ == "__main__":
	app.run()