from flask import Flask, render_template, request, jsonify
from services import gemini, deepseek, llama
import markdown

app = Flask(__name__)

# Dictionary to map service names to their functions
SERVICES = {
    "gemini": gemini.get_response,
    "deepseek": deepseek.get_response,
    "llama": llama.get_response,
}


@app.route("/")
def index():
    return render_template("index.html", services=list(SERVICES.keys()))


@app.route("/process", methods=["POST"])
def process():
    data = request.json
    prompt = data.get("prompt")
    selected_services = data.get("services", [])
    summary_prompt = data.get("summary_prompt", "")
    summary_service = data.get("summary_service")

    if not prompt or not selected_services:
        return jsonify(
            {"error": "Please provide a prompt and select at least one service"}
        ), 400

    # Get responses from selected services
    responses = []
    for service in selected_services:
        if service in SERVICES:
            response = SERVICES[service](prompt)
            responses.append(response)

    # If summary is requested
    if summary_prompt and summary_service and summary_service in SERVICES:
        combined_responses = "\n\n".join(responses)
        final_prompt = f"{summary_prompt}:\n\n{combined_responses}"
        final_response = SERVICES[summary_service](final_prompt)
        # Convert markdown to HTML
        final_response_html = markdown.markdown(final_response)
        return jsonify({"response": final_response_html})

    # If no summary requested, return all responses
    return jsonify({"responses": responses})


if __name__ == "__main__":
    app.run(debug=True)
