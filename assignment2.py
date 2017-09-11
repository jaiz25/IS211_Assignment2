#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""Assignnment 2 for IS211"""

import urllib2
import datetime
import logging
import csv
import argparse


def main():
    logging.basicConfig(file_name = 'error.log')

    def downloadData(url):
        response = urllib2.urlopen(url)
        html = response.read()
        return html

    def processData(data):
        csv_file = csv.reader(data)
        my_dict = {}
        date_format = '%d/%m/%Y'

        for row in csv_file:
            if row[0] == 'id':
                continue
            else:
                try:
                    row[2] = datetime.datetime.strptime(row[2], date_format)

                except ValueError:
                    id_num = int(row[0]) + 1
                    ids = int(row[0])

                    logger = logging.getLogger('assignment2')
                    logger.error('Error processing line #{} for ID #{}'.format(line_num, ids))

                finally:
                    my_dict[int(row[0])] = (row[1], row[2])

        return my_dict

    def displayPerson(id, personData):
        try:
            response = 'Person #{idnum} is {name} with a birthday of {date}'
            print response.format(idnum=ids, name=personData[ids][0],
                                  date=personData[id][1])
        except KeyError:
            print 'No person found with that ID #.'

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='The URL to fetch a CSV file.')
    args = parser.parse_args()
    logging.basicConfig(filename='error.log', level=logging.ERROR)

    if args.url:
        csvData = downloadData(args.url)
        personData = processData(csvData)
        message = 'Please enter an ID #. Enter 0 or a negative # to exit. '

        while True:
            try:
                user = int(raw_input(message))
            except ValueError:
                print 'Invalid input. Please try again.'
                continue
            if user > 0:
                displayPerson(user, personData)
            else:
                print 'Thank you.'
                sys.exit()
    else:
        print 'Please use --url parameter'


if __name__ == '__main__':
    main()
