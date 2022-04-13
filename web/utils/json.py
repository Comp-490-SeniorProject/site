import json
import typing

import orjson


class OrjsonDecoder(json.JSONDecoder):
    """JSONDecoder which uses orjson.

    None of the keyword arguments are supported, though they can still be specified to maintain
    compatibility with the default interface.

    `raw_decode` is not implemented in orjson, so the standard json implementation is used.
    """

    def decode(self, s: str) -> typing.Any:
        return orjson.loads(s)


class OrjsonEncoder(json.JSONEncoder):
    """JSONEncoder which uses orjson.

    `iterencode` is not implemented in orjson, so the standard json implementation is used.
    """

    def __init__(self, *, option: int = 0, **kwargs):
        """Initialises the OrjsonEncoder.

        Accepts the same keyword arguments as `json.JSONEncoder`, but most won't actually do
        anything due to lack of support in orjson. The exceptions are `sort_keys` and `default`,
        which are fully supported, and `indent`, which will always use an indent of 2 if non-zero.

        orjson-specific options can be given with the `option` keyword argument.
        """
        super().__init__(**kwargs)

        self.option = option

        if self.sort_keys:
            self.option |= orjson.OPT_SORT_KEYS

        if self.indent:
            self.option |= orjson.OPT_INDENT_2

    def encode(self, o: typing.Any) -> str:
        return orjson.dumps(o, option=self.option, default=self.default).decode("utf8")
