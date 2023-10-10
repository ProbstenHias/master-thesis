class HyperparamterInputSchema(FrontendFormBaseSchema):
    alpha = marshmallow.fields.Float(
        required=True,
        allow_none=False,
        metadata={
            "label": "Alpha",
            "description": "Alpha variable for Ridge Loss function.",
            "input_type": "textarea",
        },
    )
