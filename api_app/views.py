# Description: This file contains the views for the Flask application.
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import os
import json
from . import app, logger

@app.route("/")
def home():
    tag_line_value = os.getenv("TAG_LINE", "*** Unable to retrieve value ***")
    logger.info("Home page accessed")
    return render_template("home.html", tag_line=tag_line_value)

@app.route("/about/")
def about():
    logger.info("About page accessed")
    logger.error("*** Simulating ERROR from the Contact page ***")
    return render_template("about.html")

@app.route("/contact/")
def contact():
    logger.info("Context page accessed")
    logger.exception("~~~ Simulating EXCEPTION from the Contact page ~~~")
    return render_template("contact.html")

@app.route("/data/")
def show_data():
    logger.info("Data page accessed")
    logger.warning("=== Simulating WARNING from the Data page ===")

    data_filename = f"{app.static_folder}/atp_ranking.json"
    print(f"I will read the JSON file from {data_filename}")
    logger.info(f"I will read the JSON file from {data_filename}")
    with app.open_resource(data_filename) as f:
        atp_data = f.read()
    json_data = json.loads(atp_data)
    return render_template("data.html", atp_json=json.dumps(json_data, indent=4))

@app.route("/api/data")
def get_data():
    logger.info("API called")
    return app.send_static_file("atp_ranking.json")

@app.errorhandler(404)
def not_found_error(error):
    requested_page = request.path  # This gives you the path that was not found
    return render_template("404.html", requested_page=requested_page)

@app.errorhandler(Exception)
def generic_error_handler(error):
    logger.error(f"An uncaught error occurred: {error.description}")
    return jsonify({"Error": f"{error.description}"}), 500