from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory hike store
hikes = []

@app.route('/')
def home():
    return render_template("index.html", hikes=hikes)

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        distance = request.form['distance']
        description = request.form['description']
        image = request.form['image']  # Get selected image filename

        # Save hike info
        hikes.append({
            'name': name,
            'location': location,
            'distance': distance,
            'description': description,
            'image': image
        })
        return redirect(url_for('home'))

    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
