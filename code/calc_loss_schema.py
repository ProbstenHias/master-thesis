class CalcLossOrGradInputSchema(MaBaseSchema):
    x: NumpyArray = NumpyArray(required=False, allow_none=True)
    y: NumpyArray = NumpyArray(required=False, allow_none=True)
    x0: NumpyArray = NumpyArray(required=True, allow_none=False)


class LossResponseSchema(MaBaseSchema):
    loss = marshmallow.fields.Float(required=True, allow_none=False)
