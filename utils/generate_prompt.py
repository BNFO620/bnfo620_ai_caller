"""
creates a prompt for each trait that an organism has
"""
from models import Trait


def generate_prompts(organism) -> list[tuple[Trait, str]]:
    prompts = []
    organism_name = f"{organism.genus} {organism.species}"

    for trait in organism.traits:
        prompt = (
            f'Provide the {trait.name} reference values for {organism_name}.\n'
            f'Return only valid JSON with this exact structure. '
            f'No markdown, no code fences, no extra text:\n'
            f'{{"{trait.name}": "{trait.value_format}"}}'
        )
        prompts.append((trait, prompt))
    return prompts
