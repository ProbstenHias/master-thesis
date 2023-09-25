class CalcLossOrGradInputSchema(MaBaseSchema):
    x: NumpyArray = NumpyArray(required=True, allow_none=False)
    y: NumpyArray = NumpyArray(required=True, allow_none=False)
    x0: NumpyArray = NumpyArray(required=True, allow_none=False)
    hyperparameters: dict = marshmallow.fields.Dict(required=True, allow_none=False)
