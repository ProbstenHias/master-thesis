from flask.helpers import url_for
from plugins.optimizer.shared.enums import InteractionEndpointType
from qhana_plugin_runner.api.plugin_schemas import InteractionEndpoint
from . import RIDGELOSS_BLP

interaction_endpoints = (
    [
        InteractionEndpoint(
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
