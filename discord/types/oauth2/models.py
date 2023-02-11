# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2021-present mccoderpy

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from __future__ import annotations

from datetime import datetime
from typing import (
    List,
    Optional,
    TypeAlias,
    Union
)

from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict
)

from ..snowflake import SnowflakeID

__all__ = (
    'DatetimeLike',
    'AccessTokenData'
)

DatetimeLike: TypeAlias = Union[int, str, datetime]
RoleConnectionMetadataType = Literal[1, 2, 3, 4, 5, 6, 7, 8]


class AccessTokenData(TypedDict):
    access_token: str
    expires_at: DatetimeLike
    refresh_token: NotRequired[str]
    scopes: NotRequired[List[str]]
    user_id: NotRequired[SnowflakeID]
    ...