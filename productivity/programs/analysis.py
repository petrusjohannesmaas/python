from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()


# Load JSON data from the files
def load_json_data(filename):
    with open(os.path.join("../data", filename), "r") as file:
        return json.load(file)


environment_data = load_json_data("environment_variables.json")
tactics_data = load_json_data("tactics.json")


class ReportData(BaseModel):
    why1: str
    why2: str
    why3: str
    why4: str
    why5: str
    idea1: str
    idea2: str
    idea3: str
    success: str
    metric1: str
    metric2: str
    metric3: str
    evaluation: str


@app.get("/")
def serve_html():
    return FileResponse("tapie_analysis.html")


@app.get("/environment_data")
def get_environment_data():
    return JSONResponse(content=environment_data)


@app.get("/tactics_data")
def get_tactics_data():
    return JSONResponse(content=tactics_data)


@app.post("/submit-report")
async def submit_report(report: ReportData):
    report_data = report.dict()

    now = datetime.now()
    file_name = f"tapie_report_{now.strftime('%B')}_{now.year}.txt"

    # Write the report to the file
    with open(file_name, "w") as file:
        file.write("Environment Variables:\n")
        for key, value in environment_data.items():
            file.write(f"{key}: {value}\n")
        file.write("\nTactics:\n")
        for key, value in tactics_data.items():
            file.write(f"{key}: {value}\n")
        file.write("\nReport Data:\n")
        for key, value in report_data.items():
            file.write(f"{key}: {value}\n")

    return JSONResponse(content={"success": True})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
