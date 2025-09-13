"""
save the results to a csv file
the data structure for the csv file is as follows:
Genus, Species, Trait, Reference Value, AI Model, AI Response
"""
from config import settings
import os
import csv


def output_results(organism):
    output_file_path = settings.OUTPUT_FILE_PATH
    fieldnames = ["genus", "species", "trait", "ref_range", "model", "result"]
    is_new_file = not os.path.exists(output_file_path) and os.path.getsize(output_file_path) == 0

    with open(output_file_path, "a", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        if is_new_file:
            writer.writeheader()

        for trait in organism.traits:
            results = trait.values.results

            for model, model_result in results.items():

                row = {
                    "genus": organism.genus,
                    "species": organism.species,
                    "trait": trait.name,
                    "ref_range": trait.values.reference,
                    "model": model,
                    "result": model_result
                }
                writer.writerow(row)


                # TODO: fixing the writing to the csv file
