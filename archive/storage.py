"""Reading and writing the Archive file.

YOU IMPLEMENT THIS FILE.

The file format is CSV with no header row. One record per line, five fields
separated by commas, in this order:

    id,title,city,year,condition
    MS001,Tarikh al-Sudan,Timbuktu,1655,fragile

Remember Session 1: a file is one long line of characters. The comma
separates fields; the newline separates records. Nothing else is doing
any work.
"""
from archive.validation import validate_record 
from archive.errors import MalformedRecordError

FIELD_NAMES = ["id", "title", "city", "year", "condition"]


def parse_line(line):
    
    values = [val.strip() for val in line.strip().split(",")]
    if len(values) != 5:
        raise MalformedRecordError("Line does not contain exactly 5 fields")
    return dict(zip(FIELD_NAMES, values))


def load_archive(path):
    """Read the file at `path` and return (valid_records, rejected_lines).

    valid_records   list of dicts that passed validate_record
    rejected_lines  list of the ORIGINAL line strings that did not — either
                    because they were malformed, or because validation
                    rejected them

    A file that does not exist is not an error. It means the archive is new.
    Return ([], []) and DO NOT raise. Your program must start on a machine
    where nobody has saved anything yet.

    Blank lines are skipped silently.

    Returns (list, list).
    """
    raise NotImplementedError("load_archive")


def save_archive(path, records):
    """Write every record to `path` as CSV, one per line, no header.

    Field order is FIELD_NAMES. The file is overwritten, not appended to.

    Returns None.
    """
    raise NotImplementedError("save_archive")
