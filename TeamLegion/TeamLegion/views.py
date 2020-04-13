"""
Routes and views for the flask application.
"""
import os, logging
from datetime import datetime
from flask import render_template, request, jsonify, url_for, send_from_directory
from TeamLegion import app, client, db
from werkzeug import secure_filename

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

"""
    To get all risk data from server
"""
@app.route('/api/v1/base_risk', methods=['GET'])
def base_risk():
    testdata = db.testdata
    output = []
    for q in testdata.find():
        output.append({'lat':q['lat'], 'lon':q['lon'], 'risk':q['risk']})
    return jsonify({'result': output})


"""
    To get risk data for specific risk rank
"""
@app.route('/api/v1/base_risk/risk/<risk_factor>', methods=['GET'])
def base_risk_by_factor(risk_factor):
    testdata = db.testdata
    output = []
    for q in testdata.find({"risk":risk_factor}):
        output.append({'lat':q['lat'], 'lon':q['lon'], 'risk':q['risk']})
    return jsonify({'result': output})


"""
    To get risk data for specific geolocation
"""
@app.route('/api/v1/base_risk/geoloc/<lat>/<lon>', methods=['GET'])
def base_risk_by_geoloc(lat,lon):
    testdata = db.testdata
    output = []
    for q in testdata.find({"lat":lat,"lon":lon}):
        output.append({'lat':q['lat'], 'lon':q['lon'], 'risk':q['risk']})
    return jsonify({'result': output})

"""
    To put risk data in the server
"""
@app.route('/api/v1/base_risk/geoloc', methods=['POST'])
def put_risk_data():
    testdata = db.testdata
    lat = request.json['lat']
    lon = request.json['lon']
    risk = request.json['risk']
    inp = [{"lat": lat, "lon": lon, "risk":risk}]
    return jsonify({'result':testdata.insert(inp)})

"""
    To upload and save image
"""
@app.route('/api/v1/image/<lat>/<lon>/<time>', methods=['POST'])
def upload_image(lat,lon,time):
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.files['image']:
        app.logger.info(app.config['UPLOAD_FOLDER'])
        img = request.files['image']
        img_name = secure_filename(img.filename)
        create_new_folder(app.config['UPLOAD_FOLDER'])
        saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
        app.logger.info("saving {}".format(saved_path))
        img.save(saved_path)
        imagedata = db.imagedata
        inp = [{"lat": lat, "lon": lon, "time":time, "img":img_name, "status": "false"}]
        testdata.insert(inp)
        return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)
    else:
    	return "Where is the image?"

"""
    To download a particular image link with data with processing status set as false
"""
@app.route('/api/v1/image/unprocessed',methods=['GET'])
def get_unprocessed_data():
    imagedata = db.imagedata
    output = []
    for q in imagedata.find({"status": "false"}):
        output.append({'img':q['img'],'lat':q['lat'], 'lon':q['lon'], 'time':q['time'], 'status':q['status']})
    return jsonify({'result': output})

"""
    To update the data of an image from unprocessed to processed
"""
@app.route('/api/v1/image/processed/<img>',methods=['PUT'])
def update_unprocessed_img(img):
    imagedata = db.imagedata
    return jsonify({'result': imagedata.update({'img' : img}, {'$set': {"status": "true"}})})