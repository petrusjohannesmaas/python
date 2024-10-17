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


levels = load_json_data("levels.json")
timeblocks = load_json_data("timeblocks.json")


class ReportData(BaseModel):
    problem: str
    triage1: str
    triage2: str
    triage3: str
    triage4: str
    why1: str
    why2: str
    why3: str
    why4: str
    why5: str
    rootCause1: str
    rootCause2: str
    rootCause3: str
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


@app.get("/levels")
def get_levels_info():
    return JSONResponse(content=json.loads(json.dumps({"levels": levels}, indent=4)))


@app.get("/timeblocks")
def get_timeblocks_info():
    return JSONResponse(
        content=json.loads(json.dumps({"timeblocks": timeblocks}, indent=4))
    )


@app.post("/submit-report")
async def submit_report(report: ReportData):
    report_data = report.dict()
    now = datetime.now()
    file_name = f"{now.strftime('%B')}_{now.year}.txt"
    file_path = os.path.join("../monthly-reports", file_name)

    # Write the report to the file with more human-readable formatting
    with open(file_path, "w") as file:
        file.write("\n========== Report Data ==========\n")
        formatted_report_data = json.dumps(report_data, indent=4)
        file.write(formatted_report_data)

        file.write("\n========== Quests ==========\n")
        formatted_levels = json.dumps(levels, indent=4)
        file.write(formatted_levels)

        file.write("\n========== Current Timeblocking ==========\n")
        formatted_timeblocks = json.dumps(timeblocks, indent=4)
        file.write(formatted_timeblocks)

    return JSONResponse(content={"success": True})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
