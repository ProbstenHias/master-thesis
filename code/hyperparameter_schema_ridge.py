class HyperparamterInputSchema(FrontendFormBaseSchema):
    alpha = marshmallow.fields.Float(
        required=True,
        allow_none=False,
        metadata={
            "label": "Aplha",
            "description": "Alpha variable for Ridge Loss function.",
            "input_type": "textarea",
        },
    )
