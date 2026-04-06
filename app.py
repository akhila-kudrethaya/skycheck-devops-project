from flask import Flask, jsonify, request

# Initialize the Flask application. This line creates your "Application Object." 
# Think of app as the "boss" of your project. 
# Everything we do from here on is registered to this boss.
app = Flask(__name__)


weather_data = {
    "london": {"temp": 15, "condition": "Cloudy"},
    "new york": {"temp": 22, "condition": "Sunny"},
    "mumbai": {"temp": 30, "condition": "Humid"}
}


# @app.route('/'): This is called a Decorator. It tells the boss: 
# "Hey, if someone visits the main address of our website (the / path), run the home() function."
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "project": "SkyCheck DevOps API",
        "message": "Use /weather?city=london to get data"
    })


@app.route('/weather')
def get_weather():
    city = request.args.get('city', '').lower()
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400
    
    result = weather_data.get(city, {"temp": "Unknown", "condition": "Not in database"})
    return jsonify({"city": city, "data": result})


@app.route('/health')
def health():
    """
    A 'Health Check' endpoint used by DevOps tools to see if the app is running.
    """
    return jsonify({"status": "healthy", "container": "active"})


# This tells Python: "If I run this file directly (not importing it elsewhere), start the web server!"
# host='0.0.0.0': This makes the app accessible to other computers on your network 
# port=5000: This is the "door" number on your computer where the app is listening.
if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)