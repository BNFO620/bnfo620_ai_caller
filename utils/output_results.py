"""
save the results to a csv file
the data structure for the csv file is as follows:
Genus, Species, Trait, Reference Value, AI Model, AI Response
"""
from config import settings
import csv
import json


def output_results(organisms):
    fieldnames = ["Genus", "Species", "Trait", "Reference_Value", "AI_Model", "AI_Response"]
    with open(settings.OUTPUT_FILE_PATH, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for organism in organisms:
            for trait in organism.traits:
                values = trait.values
                ai_responses = values.ai_response.get(trait.name, {})

                for model, response in ai_responses.items():
                    if isinstance(response, str):
                        parsed_response = json.loads(response)
                        if isinstance(parsed_response, dict):
                            ai_value = parsed_response.get(trait.name, "")
                        else:
                            ai_value = str(parsed_response)
                    else:
                        ai_value = str(response)

                    row = {
                        "Genus": organism.genus,
                        "Species": organism.species,
                        "Trait": trait.name,
                        "Reference_Value": trait.values.reference_value,
                        "AI_Model": model,
                        "AI_Response": ai_value
                    }
                    writer.writerow(row)
