"""
creates a prompt for each trait that an organism has
"""


def generate_prompts(organism):
    prompts = []
    name = f"{organism.genus} {organism.species}"

    for trait in organism.traits:
        trait_name = trait.name
        trait_value_format = trait.value_format
        # TODO: what about traits with units?

        prompts.append(f""" 
        Provide the {trait_name} reference values for {name}.
        Return only valid JSON with this structure:
        {{
        "{trait_name}": "{trait_value_format}",
        }}
        No markdown. No code fences. No extra text. Use null if unknown.
        """)

    return prompts
