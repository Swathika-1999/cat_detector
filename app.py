# importing Flask and other modules
from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__, template_folder='template')


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with Firstname
        first_name = request.form.get("Firstname")
        # getting input with Lastname
        last_name = request.form.get("Lastname")
        # getting input with UploadedImage
        upload_image = request.form.get("uploadImage")
        # getting input with Selected_animal
        selected_animal = request.form.get("animal")
        return "Your name is " + first_name + last_name + upload_image + selected_animal
    return render_template("formValidations.html")


if __name__ == '__main__':
    app.run()