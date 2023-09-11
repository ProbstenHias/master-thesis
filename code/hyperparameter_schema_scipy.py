from dataclasses import dataclass
from enum import Enum

from qhana_plugin_runner.api.extra_fields import EnumField
from qhana_plugin_runner.api.util import FrontendFormBaseSchema


class MinimizerEnum(Enum):
    nelder_mead = "Nelder-Mead"
    powell = "Powell"
    # more methods ...


@dataclass
class MinimizerSetupTaskInputData:
    method: MinimizerEnum


class MinimizerSetupTaskInputSchema(FrontendFormBaseSchema):
    method = EnumField(
        MinimizerEnum,
        required=True,
        allow_none=False,
        metadata={
            "label": "Minimization Method",
            "description": "The method used for minimization.",
            "input_type": "select",
        },
    )
