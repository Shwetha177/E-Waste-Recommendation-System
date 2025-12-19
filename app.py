from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    device = request.form.get('device')
    condition = request.form.get('condition')
    age = int(request.form.get('age'))

    # Recommendation logic
    if condition == "Working" and age <= 3:
        recommendation = "Reuse or Donate the device"
    elif device == "Battery":
        recommendation = "Dispose at an authorized hazardous waste center"
    else:
        recommendation = "Recycle at an authorized e-waste recycling center"

    # Static data
    centers = [
        "Green Earth Recycling Center",
        "EcoTech E-Waste Solutions",
        "City Municipal E-Waste Facility"
    ]

    steps = [
        "Remove all personal data from the device",
        "Separate batteries and accessories",
        "Pack the device safely",
        "Take it to an authorized recycling center"
    ]

    suggestions = [
        "Do not throw e-waste in regular dustbins",
        "Prefer authorized recycling centers",
        "Donate working devices if possible",
        "Recycle responsibly to protect the environment"
    ]

    return render_template(
        'result.html',
        device=device,
        condition=condition,
        age=age,
        recommendation=recommendation,
        centers=centers,
        steps=steps,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run()


