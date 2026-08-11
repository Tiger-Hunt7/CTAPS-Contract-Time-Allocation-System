from flask import Flask, render_template, request, send_file

from ctaps_engine import (
    create_advanced_assessment,
    process_completed_assessment,
    process_lite_workbook,
)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/lite", methods=["POST"])
def lite_ranking():
    uploaded_file = request.files.get("file")

    if not uploaded_file or uploaded_file.filename == "":
        return "Please select an Excel file.", 400

    try:
        output_file = process_lite_workbook(uploaded_file)

        return send_file(
            output_file,
            as_attachment=True,
            download_name="CTAPS_Lite_Ranking_Results.xlsx",
            mimetype=(
                "application/vnd.openxmlformats-officedocument."
                "spreadsheetml.sheet"
            ),
        )

    except Exception as error:
        return f"CTAPS could not process the file: {error}", 400


@app.route("/advanced-initial", methods=["POST"])
def advanced_initial():
    uploaded_file = request.files.get("file")

    if not uploaded_file or uploaded_file.filename == "":
        return "Please select an Excel file.", 400

    try:
        output_file = create_advanced_assessment(uploaded_file)

        return send_file(
            output_file,
            as_attachment=True,
            download_name="CTAPS_Advanced_Assessment.xlsx",
            mimetype=(
                "application/vnd.openxmlformats-officedocument."
                "spreadsheetml.sheet"
            ),
        )

    except Exception as error:
        return f"CTAPS could not create the assessment: {error}", 400


@app.route("/advanced-completed", methods=["POST"])
def advanced_completed():
    uploaded_file = request.files.get("file")

    if not uploaded_file or uploaded_file.filename == "":
        return "Please select a completed assessment workbook.", 400

    try:
        output_file = process_completed_assessment(uploaded_file)

        return send_file(
            output_file,
            as_attachment=True,
            download_name="CTAPS_Advanced_Final_Ranking.xlsx",
            mimetype=(
                "application/vnd.openxmlformats-officedocument."
                "spreadsheetml.sheet"
            ),
        )

    except Exception as error:
        return f"CTAPS could not calculate the final ranking: {error}", 400


if __name__ == "__main__":
    app.run(debug=True)
