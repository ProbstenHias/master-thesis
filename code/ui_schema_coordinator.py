from qhana_plugin_runner.api.util import FrontendFormBaseSchema, PluginUrl


class OptimizerSetupTaskInputSchema(FrontendFormBaseSchema):
    minimizer_plugin_selector = PluginUrl(
        required=True,
        allow_none=False,
        plugin_tags=["minimization"],
        metadata={
            "label": "Minimizer Plugin Selector",
            "description": "URL of minimizer-plugin.",
            "input_type": "text",
        },
    )

    # more fields...
