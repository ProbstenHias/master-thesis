import marshmallow as ma
from qhana_plugin_runner.api.util import FrontendFormBaseSchema


class HyperparamterInputSchema(FrontendFormBaseSchema):
    alpha = ma.fields.Float(
        required=True,
        allow_none=False,
        metadata={
            "label": "Aplha",
            "description": "Alpha variable for Ridge Loss function.",
            "input_type": "textarea",
        },
    )
