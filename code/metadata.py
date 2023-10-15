interaction_endpoints = (
    [
        InteractionEndpoint(
            # define the type of interaction endpoint
            type=InteractionEndpointType.of_pass_data.value,
            href=url_for(
                f"{RIDGELOSS_BLP.name}.{PassDataEndpoint.__name__}",
                _external=True,
            ),
        ),
        InteractionEndpoint(
            type=InteractionEndpointType.calc_loss.value,
            href=url_for(
                f"{RIDGELOSS_BLP.name}.{CalcCallbackEndpoint.__name__}",
                _external=True,
            ),
        ),
    ],
)
