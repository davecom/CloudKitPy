#
# value.py
# CloudKitPy
#
# Created by James Barrow on 27/04/2016.
# Copyright (c) 2013-2016 Pig on a Hill Productions. All rights reserved.
#

# !/usr/bin/env python

import datetime
import time


def CKValue(value):  # noqa
    """Describes the CloudKit web services protocol.

    Several common dictionaries are used by multiple requests and responses
     throughout CloudKit web services.
    """
    # References for Types and Dictionaries can be found at:
    # https://developer.apple.com/library/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/Types/Types.html

    # TODO: Work out how to correctly use `type` without
    # getting BAD_REQUEST errors.

    value_type = None

    if type(value) == str:
        value_type = 'STRING'
    elif type(value) == float:
        value_type = 'DOUBLE'
    elif type(value) == int:
        value_type = 'INT'
    if type(value) == bool:
        value = int(value)
    elif type(value) == datetime.datetime:
        value = int(time.mktime(value.timetuple()))

    if value_type is None:
        return {
            'value': value
        }
    else:
        return {
            'value': value,
            'type': value_type
        }