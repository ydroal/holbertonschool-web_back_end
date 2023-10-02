#!/usr/bin/env python3
'''
Module to returns the log message obfuscated:
'''
import re


def filter_datum(fields, redaction, message, separator):
    '''
    returns the log message obfuscated

    Args:
        fields (list): List of strings representing all fields to obfuscate
        redaction (string): String to be replaced
        message (string): String representing the log line
        separator (string): Character separating fields in log line

    Returns:
         log message obfuscated
    '''
    for field in fields:
        regex = f'{field}=([^ {separator}]*)'
        message = re.sub(regex, f"{field}={redaction}", message)
    return message
