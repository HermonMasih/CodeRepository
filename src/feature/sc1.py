from loguru import logger
from configparser import ConfigParser

def read_file(filepath):
    try:
        config = ConfigParser()
        config.read(filepath)  # Parse the file
        return config  # Return the ConfigParser object
    except Exception as e:
        raise Exception("Unable to read file from path") from e

def main():
    student_details = {
        1: ['Maths', 'History'],
        2: ["Physics", "Chemistry", "Biology"],
        3: ['Science']
    }
    datafile = read_file(r"C:\Users\hermo\CodeRepository\config.ini")
    
    try:
        marks = datafile['Marks']  # Access the 'Marks' section in the config file
        for seq, subject in student_details.items():
            logger.info(f"For student {seq}")
            total_marks = 0
            for sub in subject:
                total_marks += int(marks[sub])  # Access marks for each subject
            logger.info(f"Total marks for student {seq} :- {total_marks}")
    except KeyError as e:
        raise Exception(f"Key {e} not present in config file") from e
    except Exception as e:
        raise Exception("An error occurred while processing the data") from e

def start():
    main()

start()