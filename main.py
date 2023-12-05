import base64
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from io import BytesIO

from chapter3 import *
from chapter5 import *
from chapter6 import *
from chapter7 import *

app = Flask(__name__)
app.secret_key = "intelligent"
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/negative', methods=['POST'])
def negative():
    try:
        image_file = request.files['image']
        negative_image = negative_transform(image_file)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/api/threshold', methods=['POST'])
def thresholding():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = thresholding_image(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/logarit', methods=['POST'])
def logarit():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = logarit_transform(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/powerlow', methods=['POST'])
def power_law():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = power_law_transform(img_array, 2)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/histogram', methods=['POST'])
def histogram():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = histogram_equalizing(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/average', methods=['POST'])
def average():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = average_filter(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/weight', methods=['POST'])
def weight():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = weighted_averaging(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/median', methods=['POST'])
def median():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = median_filter(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/roberts', methods=['POST'])
def roberts():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = roberts_operator(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/sobels', methods=['POST'])
def sobels():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = sobels_operator(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/laplace', methods=['POST'])
def laplace():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = laplacian_operator(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/prewitt', methods=['POST'])
def prewitt():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = prewitt_operator(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/canny', methods=['POST'])
def canny():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = canny_operator(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/otsu', methods=['POST'])
def otsu():
    try:
        image_file = request.files['image']

        img_array = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        negative_image = otsu_algorithm(img_array)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/rlc', methods=['POST'])
def rlc():
    try:
        image_file = request.files['image']

        originalImage = Image.open(image_file).convert("L")

        negative_image = rlc_coding(originalImage)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/lzw', methods=['POST'])
def lzw():
    try:
        image_file = request.files['image']

        originalImage = Image.open(image_file).convert("L")

        negative_image = lzw_compress(originalImage)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/erosion', methods=['POST'])
def erosion():
    try:
        image_file = request.files['image']

        originalImage = np.array(Image.open(image_file))
        negative_image = erosion_image(originalImage)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/dilate', methods=['POST'])
def dilate():
    try:
        image_file = request.files['image']

        originalImage = np.array(Image.open(image_file))
        negative_image = dilation_image(originalImage)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/open', methods=['POST'])
def open():
    try:
        image_file = request.files['image']

        originalImage = np.array(Image.open(image_file))
        negative_image = opening_image(originalImage)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})
    
@app.route('/api/close', methods=['POST'])
def close():
    try:
        image_file = request.files['image']

        originalImage = np.array(Image.open(image_file))
        negative_image = closing_image(originalImage)

        img_buffer = BytesIO()
        negative_image.save(img_buffer, format="JPEG")
        img_str = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

        return jsonify({'image_data': img_str})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)