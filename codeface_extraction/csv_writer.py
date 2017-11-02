# coding=utf-8
"""
This file provides the needed functions for standardized CSV writing
"""

import csv


def write_to_csv(file_path, lines):
    """Write the given lines to the file with the given file path."""

    # write lines to file for current kind of artifact
    with open(file_path, 'wb') as csv_file:
        wr = csv.writer(csv_file, delimiter=';', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
        for line in lines:
            lineres = ()
            for column in line:
                print type(column)
                if type(column) is unicode:
                    lineres += (column.encode("utf-8"),)
                else:
                    lineres += (column,)
            wr.writerow(lineres)
