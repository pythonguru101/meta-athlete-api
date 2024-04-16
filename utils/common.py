from datetime import datetime

def parse_date(date_string):
    # Use common date format, finds the provided format and returns date in Y-m-d format
    try:
        date_formats = [
            '%Y/%m/%d', '%Y-%m-%d', '%m/%d/%Y', '%m-%d-%Y',
            '%d/%m/%Y', '%d-%m-%Y', '%Y%m%d', '%m%d%Y', '%d%m%Y'
        ]
        for format_string in date_formats:
            try:
                date_object = datetime.strptime(date_string, format_string)
                return date_object.strftime('%Y/%m/%d')
            except ValueError:
                pass
    except ValueError as e:
        print(f'Error parsing date: {e}')
