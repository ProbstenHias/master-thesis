from enum import Enum

class InteractionEndpointType(Enum):
    minimization = "minimization"
    calc_loss = "calc_loss"
    calc_grad = "calc_grad"
    calc_loss_and_grad = "calc_loss_and_grad"
    of_pass_data = "of_pass_data"
