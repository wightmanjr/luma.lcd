# -*- coding: utf-8 -*-
# Copyright (c) 2017-2022 Richard Hull and contributors
# See LICENSE.rst for details.

import pytest
from unittest.mock import Mock

import luma.core.error

serial = Mock(unsafe=True)


def setup_function(function):
    """
    Called before a test runs.
    """
    serial.reset_mock()
    serial.command.side_effect = None


def assert_invalid_dimensions(deviceType, serial_interface, width, height):
    """
    Assert an invalid resolution raises a
    :py:class:`luma.core.error.DeviceDisplayModeError`.
    """
    with pytest.raises(luma.core.error.DeviceDisplayModeError) as ex:
        deviceType(serial_interface, gpio=Mock(), width=width, height=height)
    assert f"Unsupported display mode: {width} x {height}" in str(ex.value)
