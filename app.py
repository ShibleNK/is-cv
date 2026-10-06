from flask import Flask, request, render_template, redirect, url_for
import cv2
import os

from edge_detection import sobel, edges

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
OUTPUT_FOLDER = 'static/outputs/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            return 'No file selected', 400
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        process_image(file.filename)
        return redirect(url_for('display_result', filename=file.filename))

    return render_template('upload.html')

def process_image(filename):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image = cv2.imread(image_path)

    # Save outputs
    cv2.imwrite(os.path.join(app.config['OUTPUT_FOLDER'], 'sobel_'+ filename),sobel)
    cv2.imwrite(os.path.join(app.config['OUTPUT_FOLDER'], 'edges_'+ filename),edges)
    
@app.route('/result/<filename>')
def display_result(filename):
    return render_template('result.html',
                           original_image= 'uploads/' + filename,
                           sobel_image='outputs/sobel_'+filename,
                           edges_image='outputs/edges_'+ filename)


if __name__ == '__main__':
    app.run(debug=True)