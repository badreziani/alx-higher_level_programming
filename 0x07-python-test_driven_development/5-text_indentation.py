#!/usr/bin/python3
"""Defines the text_indentation function."""


def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters: ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")

