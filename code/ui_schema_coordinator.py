import marshmallow as ma
from qhana_plugin_runner.api.util import FileUrl, FrontendFormBaseSchema, PluginUrl


class OptimizerSetupTaskInputSchema(FrontendFormBaseSchema):
    input_file_url = FileUrl(
        required=True,
        allow_none=False,
        data_input_type="*",
        data_content_types=["text/csv"],
        metadata={
            "label": "Dataset URL",
            "description": "URL to a csv file with optimizable data.",
        },
    )
    target_variable = ma.fields.String(
        required=True,
        allow_none=False,
        metadata={
            "label": "Target Variable",
            "description": "Name of the target variable in the dataset.",
            "input_type": "text",
        },
    )
    objective_function_plugin_selector = PluginUrl(
        required=True,
        allow_none=False,
        plugin_tags=["objective-function"],
        metadata={
            "label": "Objective-Function Plugin Selector",
            "description": "URL of objective-function-plugin.",
            "input_type": "text",
        },
    )
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
