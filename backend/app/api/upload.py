from fastapi import APIRouter, UploadFile, File
import os
import shutil

from ..utils.parser import parse_file
from ..services.rule_engine import analyze_security
from ..services.drift_engine import detect_drift
from ..services.risk_engine import calculate_risk_score # type: ignore
from ..core.baseline import BASELINE

router = APIRouter()

UPLOAD_FOLDER = "uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # Allowed file extensions
    allowed_extensions = [".json", ".yaml", ".yml"]

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in allowed_extensions:
        return {
            "status": "error",
            "message": "Only JSON and YAML files are allowed."
        }

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Parse uploaded file
    parsed_data = parse_file(file_path)

    # Run Rule Engine
    findings = analyze_security(parsed_data)

    # Run Drift Detection Engine
    drifts = detect_drift(parsed_data, BASELINE)

    # Calculate Risk Score
    risk = calculate_risk_score(findings)

    # Return response
    return {
        "status": "success",
        "filename": file.filename,
        "parsed_data": parsed_data,
        "findings": findings,
        "drifts": drifts,
        "risk": risk
    }