import pandas as pd
import google.generativeai as genai
import json
import time
# ==========================================
# GEMINI API KEY
# ==========================================

genai.configure(api_key="AIzaSyCF25QEFOTftB-oc-e7GnlHH04XhMPV8EM")

# ==========================================
# MODEL
# ==========================================

model = genai.GenerativeModel("gemini-3.5-flash")

# ==========================================
# CSV FILE
# ==========================================

CSV_FILE = "manual_boq_dataset.csv"

# ==========================================
# CREATE CSV IF NOT EXISTS
# ==========================================

try:
    df = pd.read_csv(CSV_FILE)

except:
    df = pd.DataFrame(columns=[
        "BOQ_TEXT",
        "GEMINI_OUTPUT",
        "TIME_TAKEN_SEC"
    ])

# ==========================================
# EXTRACTION FUNCTION
# ==========================================

def extract_attributes(boq_text):

    prompt = f"""
You are an expert civil construction BOQ extraction system.

Extract all possible attributes from the BOQ item.

Rules:
- Return ONLY valid JSON
- No explanation
- Keep attribute names short
- Extract dimensions, grade, material, thickness, type, etc.

BOQ Item:
{boq_text}
"""

    try:

        start_time = time.time()

        response = model.generate_content(prompt)

        end_time = time.time()

        execution_time = round(end_time - start_time, 2)

        text = response.text.strip()

        text = text.replace("```json", "").replace("```", "").strip()

        return text, execution_time

    except Exception as e:

        return json.dumps({
            "error": str(e)
        }), 0

# ==========================================
# LOOP
# ==========================================

while True:

    print("\n==============================")

    boq_text = input("Enter BOQ Description:\n")

    output, exec_time = extract_attributes(boq_text)

    print("\n===== GEMINI EXTRACTION =====")
    print(output)

    print(f"\nTime Taken: {exec_time} sec")

    save_choice = input("\nAppend in CSV? (yes/no): ").lower()

    if save_choice == "yes":

        new_row = {
            "BOQ_TEXT": boq_text,
            "GEMINI_OUTPUT": output,
            "TIME_TAKEN_SEC": exec_time
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv(CSV_FILE, index=False)

        print("Saved to CSV!")

    more = input("\nMore Examples? (yes/no): ").lower()

    if more != "yes":

        if len(df) > 0:

            avg_time = round(df["TIME_TAKEN_SEC"].mean(), 2)

            print(f"\nAverage Execution Time: {avg_time} sec")

        print("Process Finished!")

        break