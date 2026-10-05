"""YOUR test suite — Part B (15 marks).

This file is graded by what it CATCHES, not by how much you write.

After the deadline your suite is run against five secret broken versions of
the Archive. Each contains exactly one realistic bug of a kind we have
discussed in class. You score 3 marks for each broken version your suite
detects — meaning at least one of your tests FAILS against it.

Two rules that decide whether you score at all:

  1. Your suite must PASS COMPLETELY against a correct implementation.
     A suite that fails everything "catches" all five bugs and scores ZERO.

  2. For validate_year you must include all four kinds of test data from
     Session 2: normal, abnormal, extreme, and boundary either side.

Where are the bugs? Where careless code always breaks: the edges. Test
1099/1100 and 1900/1901. Test empty strings and whitespace. Test a field
count that is wrong. Test upper case where you assumed lower.

Run yours with:   pytest tests/test_yours.py -v
"""

import pytest

from archive.errors import MalformedRecordError
from archive.storage import parse_line, load_archive, save_archive
from archive.validation import (
    validate_id,
    validate_title,
    validate_city,
    validate_year,
    validate_condition,
    validate_record,
)
from archive.queries import count_before, find_by_city, oldest, cities_summary


# ====================================================== WORKED EXAMPLE
# The four kinds of test data from Session 2, shown on validate_condition.
# Study the PATTERN here, then apply it yourself to the other fields.
# These five are given. They are not enough to catch anything on their own.

def test_condition_normal():
    """NORMAL — an ordinary accepted value."""
    assert validate_condition("fragile")[0] is True


def test_condition_normal_other():
    """NORMAL — the other accepted values matter too."""
    assert validate_condition("good")[0] is True


def test_condition_abnormal():
    """ABNORMAL — a value of the wrong kind entirely."""
    assert validate_condition("excellent")[0] is False


def test_condition_empty():
    """ABNORMAL — nothing at all is still the wrong kind."""
    assert validate_condition("")[0] is False


def test_condition_case():
    """A rule the brief states: the check is case-insensitive."""
    assert validate_condition("GOOD")[0] is True


# ============================================= NOW DO THIS FOR validate_year
# Required for Part B. The year rules are where the marks are, because the
# year rules are where careless code breaks. Write all four kinds:
#
#   NORMAL     a year from the middle of the range
#   ABNORMAL   something that is not a year at all
#   EXTREME    1100 and 1900 — valid, sitting exactly on the edge
#   BOUNDARY   1099 and 1901 — one step outside, must be rejected

def test_year_normal():
    """NORMAL — a value in the middle of the allowed range."""
    assert validate_year("1655")[0] is True


def test_year_abnormal():
    """ABNORMAL — not a year at all."""
    assert validate_year("c.1590")[0] is False


def test_year_extreme():
    """EXTREME — the boundary values are valid when inclusive."""
    assert validate_year("1100")[0] is True
    assert validate_year("1900")[0] is True


def test_year_boundary():
    """BOUNDARY — values just outside the range must be rejected."""
    assert validate_year("1099")[0] is False
    assert validate_year("1901")[0] is False


# ============================================================== your tests
# Everything below is yours. Suggested coverage, in the order the marks are
# easiest to earn:
#
#   validate_id          format, length, case, empty
#   validate_title       whitespace-only, exactly 3 characters, shorter
#   validate_city        known, unknown, different case
#   validate_condition   each valid value, upper case, an invalid one
#   validate_record      a clean record, and one with several faults at once
#   parse_line           5 fields, 4 fields, 6 fields, whitespace around values
#   load_archive         missing file, the clean file, the messy file
#   save_archive         round trip: save then load gives back what you saved
#   queries              empty list, ties, case-insensitive city
