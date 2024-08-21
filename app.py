from flask import Flask, render_template, request

# Create an instance of the Flask class for the web application
app = Flask(__name__)

# Define the main route for the application, which handles both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():

    # Initialize a variable to store the calculated woman's age, default is 0
    result_age = 0
    
    if request.method == 'POST':
        try:
            # Retrieve the man's age input from the form and convert it to an integer
            man_age = int(request.form['age'])
            # Calculation: Woman's Age = Man's Age / 2 + 7
            result_age = man_age // 2 + 7
        except ValueError:
            # If the input is not a valid integer, return an empty string
            result_age = ""
            
    # Render the index.html template and pass the processed age to it
    return render_template("index.html", age=result_age)

# Run the Flask application in debug mode when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
