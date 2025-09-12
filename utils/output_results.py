"""
save the results to a csv file
the data structure for the csv file is as follows:
Genus, Species, Trait, Reference Value, AI Model, AI Response
"""
from config import settings
import os
import csv
import json


def output_results(organism):
    fieldnames = ["genus", "species", "trait", "ref_range", "ai_model", "ai_result"]
    with open(settings.OUTPUT_FILE_PATH, "a", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        if not os.path.exists(settings.OUTPUT_FILE_PATH):
            writer.writeheader()

        for trait in organism.traits:
            ai_responses = trait.values.ai_response

            for model, ai_result_json in ai_responses.items():
                ai_result_data = json.loads(ai_result_json)
                ai_result_value = ai_result_data.get(trait.name)

                row = {
                    "genus": organism.genus,
                    "species": organism.species,
                    "trait": trait.name,
                    "ref_range": trait.values.reference_value,
                    "ai_model": model,
                    "ai_result": ai_result_value
                }
                writer.writerow(row)
