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
    valid_records = []
    rejected_lines = []    
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for line_number, raw_line in enumerate(file, start=1):
                cleaned_line = raw_line.strip()

                if not cleaned_line:
                    continue

                try:
                    entries = validate_record(raw_line, expected_count=len(FIELD_NAMES))
                    record = parse_line(entries, FIELD_NAMES)
                    valid_records.append(record)

                except MalformedRecordError as err:
                    rejected_lines.append({
                        "line_number": line_number,
                        "raw_line": cleaned_line,
                        "error": str(err)
                    })

    except FileNotFoundError:
        return ([], [])
    return (valid_records, rejected_lines)


def save_archive(path, records):
    with open(path, mode="w", encoding="utf-8") as file:
        for record in records:
            values = [str(record[field]) for field in FIELD_NAMES]
            line = ",".join(values) + "\n"
            file.write(line)
 
