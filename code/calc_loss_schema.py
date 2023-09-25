class CalcLossOrGradInputSchema(MaBaseSchema):
    x0: NumpyArray = NumpyArray(required=True, allow_none=False)
