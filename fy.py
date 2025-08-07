from datetime import datetime   # Import the datetime class to parse/validate real calendar dates
import re   # Import regex module to enforce exact yyyy-mm-dd shape

strDate = input("Enter Date (format yyyy-mm-dd): ") # Prompt user to enter date; stores raw input text in strDate(a str)
format_string = "%Y-%m-%d"  # Parse: 4-digit year, dash, 2-digit month, dash, 2 digit day

## Validate exact shape AND real calendar dates##
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", strDate): # Check the entire input if matches exactly ####-##-## (automatically adding zero if need be)
    print("Error: use exact format yyyy-mm-dd (e.g., 2025-08-07).") # If missmatch, print error
else:
    try:
        dtDate = datetime.strptime(strDate, format_string)  # parse text: datetime / raise ValueError on impossible dates
    except ValueError:  # handle (bad month/day)
        print("Error: date is not valid (check month/day/leap year)") # print error to user
    else:
        # Desired output: FY####
        cutoff_month = 7    # new FY year starts Jul 1
        fy_year = dtDate.year + 1 if dtDate.month >= cutoff_month else dtDate.year # If month >= cutoff_month, FY is the next calendar year otherwise it's the same year. Year, month, and day are attributes of the datetime object; dtDate is a datetime.datetime instance, and it has built-in fields: dtDate.year(int), dtDate.month(int), dtDate.day(int)
        print(f"FY{fy_year}") # print the fy
