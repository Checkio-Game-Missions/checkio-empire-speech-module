from checkio_referee import RefereeRank, ENV_NAME


import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "tell_number"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "tellNumber"
    }
