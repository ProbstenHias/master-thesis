class MinimizerInputSchema(MaBaseSchema):
    x0 = NumpyArray(required=True, allow_none=False)
    x = NumpyArray(required=True, allow_none=False)
    y = NumpyArray(required=True, allow_none=False)
    hyperparameters = marshmallow.fields.Dict(required=True, allow_none=False)
    calc_loss_endpoint_url = marshmallow.fields.Url(required=True, allow_none=False)
    calc_gradient_endpoint_url = marshmallow.fields.Url(required=False, allow_none=True)
    calc_loss_and_gradient_endpoint_url = marshmallow.fields.Url(required=False, allow_none=True)
    callback_url = marshmallow.fields.Url(required=False, allow_none=True)
