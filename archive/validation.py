"""Validation rules for manuscript records.

YOU IMPLEMENT THIS FILE.

Every validate_* function takes a raw string (exactly as it came out of the
CSV file) and returns a tuple:

    (True, "")              the value is trustworthy
    (False, "reason here")  the value is not, and here is why

The reason is a short human-readable string. The autograder checks the
boolean, not your exact wording — but a teammate reading your rejection log
should understand it, so write it for them.

READ THIS BEFORE YOU START
--------------------------
The year range is INCLUSIVE at both ends: 1100 and 1900 are VALID.
1099 and 1901 are not. Most marks lost in Part A are lost on that line.
"""

from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]
citylower = ["timbuktu", "djenne", "gao", "walata", "chinguetti"]
VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 1100
MAX_YEAR = 1900


def validate_id(value):
      
    if not value :
        return (False,"Empty")
    if len(value)!=5:
        return (False,"The length of ID is not 5")
    if value[:2]!="MS":
        return (False,"First two letters not \'MS\'")
    try:
        int(value[2:5])
        return("True","")
    except ValueError:
        return ("False","Last three letters not all integers")

    



def validate_title(value):
    try:
        work=True
        
        #check for numbers in the string
        checknum= any(char.isdigit() for char in value)
        if not value.strip() or len(value.strip())<3 or checknum==True:
            work =False
            st="This is not a valid title"
        else:
            st="This is a valid title"   
        return (work,st)
    except ValueError:
        return(False,"This is not a valid title")

def validate_city(value):
  try:
    value = value.lower()
    for i in citylower:
        if value == i:
            return (True, "This is a valid city")
    return (False, "This is not a valid city")
  except ValueError:
      return (False,"This is not a valid city")

def validate_year(value):
 if isinstance(value,str) and not value.strip():
        return(False,"Empty year")
 else:      
        try:    
            number = int(value)
            if 1100<=number and number<=1900:
                return(True,"Valid")
            else:
                return(False,"this is either too old or too recent")
        except ValueError:
            return(False,"Its not even an integer") 

               


def validate_condition(value):
    
    value =value.lower()
    if value not in VALID_CONDITIONS:
        return (False,"Condition not Valid")
    return (True,"")
    


def validate_record(record):
    st=[]
    if(validate_condition(record["condition"])==False):
        st.append( "Condition not Valid")
    if(validate_year(record["year"])==False):
        st.append("Year not Valid")
    if(validate_city(record["city"])==False):
        st.append("City not Valid")
    if(validate_title(record["title"])==False):
        st.append("Title not Valid")
    if(validate_id(record["id"])==False):
        st.append("ID not Valid")
    return st
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """