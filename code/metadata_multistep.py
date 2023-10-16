interaction_endpoints = (
    [
        InteractionEndpoint(
            # define the type of interaction endpoint
            type=InteractionEndpointType.of_pass_data.value,
            # define the endpoint URL
            # use the url_for_ie function to generate the URL with a task_id placeholder
            href=url_for_ie(f"{RIDGELOSS_BLP.name}.{PassDataEndpoint.__name__}"),
        ),
        InteractionEndpoint(
            type=InteractionEndpointType.calc_loss.value,
            href=url_for_ie(f"{RIDGELOSS_BLP.name}.{CalcLossEndpoint.__name__}"),
        ),
    ],
)
