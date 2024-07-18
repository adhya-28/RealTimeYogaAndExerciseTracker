from flask import Flask, render_template, request, jsonify
import logging
import threading

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exercise.html')
def exercise():
    return render_template('exercise.html')

@app.route('/yoga.html')
def yoga_classification():
    return render_template('yoga.html')

@app.route('/image.html')
def image_classification():
    return render_template('image.html')

@app.route('/webcam.html')
def realtime_yoga_classification():
    return render_template('webcam.html')

def start_exercise(exercise_name, repetitions):
    try:
        logging.debug(f"Starting {exercise_name} with {repetitions} repetitions")
        
        if exercise_name == "Jumping Jacks":
            from exercise import jumping_jack
            jumping_jack(repetitions)
        elif exercise_name == "Squat":
            from exercise import squat
            squat(repetitions)
        elif exercise_name == "Left Leg Rise":
            from exercise import left_leg_rise
            left_leg_rise(repetitions)
        elif exercise_name == "Walking Jog":
            from exercise import walking_jog
            walking_jog(repetitions)
        elif exercise_name == "Lunge":
            from exercise import lunge
            lunge(repetitions)
        elif exercise_name == "Plank":
            from exercise import plank
            plank(repetitions)
        elif exercise_name == "Push Up":
            from exercise import push_up
            push_up(repetitions)
        elif exercise_name == "Crunches":
            from exercise import crunches
            crunches(repetitions)
        elif exercise_name == "Triceps Dip":
            from exercise import triceps_dip
            triceps_dip(repetitions)
        else:
            logging.warning(f"Unknown exercise: {exercise_name}")
    except Exception as e:
        logging.error(f"Error: {e}")

@app.route('/start_exercise', methods=['POST'])
def start_exercise_route():
    try:
        data = request.get_json()
        exercise_name = data.get('exercise_name')
        repetitions = int(data.get('repetitions'))
        logging.debug(f"Received request to start {exercise_name} with {repetitions} repetitions.")
        
        # Start the exercise in a new thread to avoid blocking Flask's main thread
        exercise_thread = threading.Thread(target=start_exercise, args=(exercise_name, repetitions))
        exercise_thread.start()

        return jsonify({"status": f"{exercise_name} started"})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
