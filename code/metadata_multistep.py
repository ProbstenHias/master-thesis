interaction_endpoints = (
    [
        InteractionEndpoint(
            # define the type of interaction endpoint
            type=InteractionEndpointType.of_pass_data.value,
            # define the endpoint URL
            href=url_for(
                f"{RIDGELOSS_BLP.name}.{PluginsView.__name__}",
                _external=True,
            )
            + "<int:task_id>/pass-data/",
        ),
        InteractionEndpoint(
            type=InteractionEndpointType.calc_loss.value,
            href=url_for(
                f"{RIDGELOSS_BLP.name}.{PluginsView.__name__}",
                _external=True,
            )
            + "<int:task_id>/calc-callback-endpoint/",
        ),
    ],
)
