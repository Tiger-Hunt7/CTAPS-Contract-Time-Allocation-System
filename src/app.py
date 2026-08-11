from flask import Flask, render_template, request, send_file
import os
import tempfile

from ctaps_engine import (
    process_lite_ranking,
    create_advanced_assessment,
    process_advanced_assessment,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/lite", methods=["POST"])
def lite():
    uploaded = request.files.get("file")
    if not uploaded or not uploaded.filename:
        return "Please upload an Excel workbook.", 400

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, uploaded.filename)
        output_path = os.path.join(tmpdir, "CTAPS_Lite_Ranking.xlsx")
        uploaded.save(input_path)
        process_lite_ranking(input_path, output_path)
        return send_file(output_path, as_attachment=True, download_name="CTAPS_Lite_Ranking.xlsx")


@app.route("/assessment/create", methods=["POST"])
def assessment_create():
    uploaded = request.files.get("file")
    if not uploaded or not uploaded.filename:
        return "Please upload an Excel workbook.", 400

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, uploaded.filename)
        output_path = os.path.join(tmpdir, "CTAPS_Advanced_Assessment.xlsx")
        uploaded.save(input_path)
        create_advanced_assessment(input_path, output_path)
        return send_file(output_path, as_attachment=True, download_name="CTAPS_Advanced_Assessment.xlsx")


@app.route("/assessment/process", methods=["POST"])
def assessment_process():
    uploaded = request.files.get("file")
    if not uploaded or not uploaded.filename:
        return "Please upload a completed assessment workbook.", 400

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, uploaded.filename)
        output_path = os.path.join(tmpdir, "CTAPS_Final_Ranking.xlsx")
        uploaded.save(input_path)
        process_advanced_assessment(input_path, output_path)
        return send_file(output_path, as_attachment=True, download_name="CTAPS_Final_Ranking.xlsx")


if __name__ == "__main__":
    app.run(debug=True)
