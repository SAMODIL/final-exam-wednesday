"""
Test code for Split Array

Sardor Gulyamov 2022
"""

import json
import os
import sys

import pytest

import prod

# Handle the fact that the grading code may not
# be in the same directory as rotate.py
sys.path.append(os.getcwd())

# Get the name of the directory that holds the grading code.
BASE_DIR = os.path.dirname(__file__)
TEST_DIR = os.path.join(BASE_DIR, "tests")


def read_config_file(filename):
    """
    Load the test cases from a JSON file.

    Inputs:
      filename (string): the name of the test configuration file.

    Returns: (list) test cases
    """

    with open(os.path.join(TEST_DIR, filename)) as f:
        return json.load(f)


def gen_none_error(recreate_msg):
    """
    Generate the error message for an unexpected return value of None.

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "The function returned None."
    msg += " Did you forget to include a return statement?\n"
    return msg + recreate_msg + "\n"


def gen_type_error(recreate_msg, expected, actual):
    """
    Generate the error message for a return value of the wrong type

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n"
    msg += "  Actual return type: {}.\n"
    msg += recreate_msg + "\n"
    return msg.format(type(expected), type(actual))


def gen_mismatch_error(recreate_msg, expected, actual):
    """
    Generate the error message for the case whether the expected and
    actual values do not match.

    Inputs:
      recreate_msg (string): a string with the information needed to
        rerun the test in ipython.

    Returns (string): error message
    """

    msg = "Actual ({}) and expected ({}) values do not match.\n"
    msg += recreate_msg + "\n"
    return msg.format(actual, expected)



@pytest.mark.parametrize(
    "params",
    read_config_file("prefix_prod.json"))
def test_prefix_prod(params):
    """
    Test harness for prefix_prod function.

    Inputs:
      params (dictionary): the test parameters:
        array and the expected prefix array
    """

    actual_prefix = prod.prefix_prod(params["array"])

    recreate_msg = "To recreate this test in python3 run:\n"
    recreate_msg += f'  prod.prefix_prod({params["array"]})'

    assert actual_prefix is not None, \
        gen_none_error(recreate_msg)

    expected_prefix = params["expected"]
    assert isinstance(actual_prefix, type(expected_prefix)), \
        gen_type_error(recreate_msg,
                       expected_prefix,
                       actual_prefix)

    assert actual_prefix == expected_prefix, \
        gen_mismatch_error(recreate_msg,
                           expected_prefix,
                           actual_prefix)




@pytest.mark.parametrize(
    "params",
    read_config_file("segment_prod.json"))
def test_segment_prod(params):
    """
    Test harness for segment_prod function.

    Inputs:
      params (dictionary): the test parameters:
        array, k, and the expected array
    """

    actual_prod = prod.segment_prod(params["array"], params["left"], params["right"])

    recreate_msg = "To recreate this test in python3 run:\n" \
                   f'  prod.segment_prod({params["array"]}, {params["left"]}, {params["right"]})'

    assert actual_prod is not None, \
        gen_none_error(recreate_msg)

    expected_prod = params["expected"]
    assert isinstance(actual_prod, type(expected_prod)), \
        gen_type_error(recreate_msg,
                       expected_prod,
                       actual_prod)

    assert actual_prod == expected_prod, \
        gen_mismatch_error(recreate_msg,
                           expected_prod,
                           actual_prod)


@pytest.mark.parametrize(
    "params",
    read_config_file("max_prod_segment.json"))
def test_max_prod_segment(params):
    """
    Test harness for max_prod_segment function.

    Inputs:
      params (dictionary): the test parameters:
        array and the expected maximum
    """

    max_prod = prod.max_prod_segment(params["array"])

    recreate_msg = "To recreate this test in python3 run:\n" \
                   f'  prod.max_prod({params["array"]})'

    assert max_prod is not None, \
        gen_none_error(recreate_msg)

    expected_prod = params["expected"]
    assert isinstance(max_prod, type(expected_prod)), \
        gen_type_error(recreate_msg,
                       expected_prod,
                       max_prod)

    assert max_prod == expected_prod, \
        gen_mismatch_error(recreate_msg,
                           expected_prod,
                           max_prod)
