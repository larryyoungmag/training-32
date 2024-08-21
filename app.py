from flask import Flask, render_template, request

# Create an instance of the Flask class for the web application
app = Flask(__name__)

# Define the main route for the application, which handles both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():

    # Initialize a variable to store the processed age value, default is 0
    result_age = 0
    
    if request.method == 'POST':
        try:
            # Retrieve the age input from the form and convert it to an integer
            age = int(request.form['age'])
            # Calculation: Add 6 to the input age and store the result
            result_age = age + 6
        except ValueError:
            # If the input is not a valid integer, return an empty string
            result_age = ""
            
    # Render the index.html template and pass the processed age to it
    return render_template("index.html", age=result_age)

# Run the Flask application in debug mode when the script is executed directly
if __name__ == '__main__':
  app.run(debug=True)
