import argparse
import json
import logging
import random
import sys
import os
import shutil
import time
import uuid
from multiprocessing import Pool,RLock
from datetime import datetime
from random import randint as rand


class Cli:
    def __init__(self, argv=None):
        self.DEFAULT_DIRECTORY = 'JSON'
        self.my_parser = argparse.ArgumentParser(epilog='Enjoy the program! :)',prog="Capstone")
        self.p = Pool()
        self.my_parser.version = '1.0'
        self.data = ""
        self.file_name = ''
        self.my_parser.add_argument('-p', '--path_to_save_files', default=[self.DEFAULT_DIRECTORY], action='store'
                                    , type=str, nargs='?',
                                    help='Path where you want your JSON files to be stored '
                                         '(this directory its the default value)')
        self.my_parser.add_argument('-fc', '--file_count', default=[1], action='store'
                                    , type=int, nargs=1, help='Number of JSON files to be generated.')
        self.my_parser.add_argument('-fn', '--file_name', action='store', default=[str(self.my_parser.prog)]
                                    , type=str, nargs=1, help='Base file name.')
        self.my_parser.add_argument('-fp', '--prefix', action='store', default=['count']
                                    , type=str, nargs=1, choices=['count', 'random', 'uuid'],
                                    help='What prefix for file name.')
        self.my_parser.add_argument('-ds', '--data_schema', default="{}", action='store'
                                    , type=str, nargs=1, help='It’s a string with json schema..',required=True)
        self.my_parser.add_argument('-dl', '--data_lines', action='store'
                                    , type=int, nargs=1, default=[1],
                                    help='Count of lines for each file. Default, for example: 1000')
        self.my_parser.add_argument('-cp', '--clear_path', action='store'
                                    , type=bool, nargs=1, default=[True],
                                    help='If this flag is on, before the script starts creating '
                                         'new data files, all files in path_to_save_files that match file_name '
                                         'will be deleted.')
        self.my_parser.add_argument('-mp', '--multiprocessing', action='store'
                                    , type=int, nargs=1, default=[1],
                                    help='The number of processes used to create files.')
        self.args = self.my_parser.parse_args(argv)
        # print(self.args.multiprocessing[0])
        self.p = Pool(processes=self.args.multiprocessing[0])

        self.my_parser.prog = self.args.file_name
        self.my_parser.prog = str(self.my_parser.prog[0] + '_' + self.args.prefix[0])

    def time_stamp(self):
        return datetime.now().timestamp()

    def file_prefix(self, counter, prefix):
        if prefix == 'count':
            return counter
        elif prefix == 'random':
            return random.randint(1000, 1000000)
        elif prefix == 'uuid':
            return str(uuid.uuid4())
        else:
            logging.error('Error with data prefix')
            sys.exit(1)

    def parse_analysis(self):
        # FILES COUNT ERROR
        if self.args.file_count[0] < 0:
            logging.error("You should input a positive number of files to be generated in files_count.")
        # MULTIPROCESSING ERROR
        if self.args.multiprocessing[0] < 0 :
            logging.error("You should input a positive number of multiprocessings to be generated.")
        if self.args.multiprocessing[0] > os.cpu_count(): self.args.multiprocessing[0] = os.cpu_count()

        # DATA SCHEMA
        # Checking if data schema its a path
        if os.path.isfile(self.args.data_schema[0]):
            f = open(str(self.args.data_schema[0]))
            try:
                self.data = json.load(f)
            except:
                logging.error("Can't serialize your JSON file(1).")
                sys.exit(1)
        # If it is not a path, it should a data schema
        else:
            try:
                self.data = json.loads(self.args.data_schema[0])
            except:
                logging.error("Can't serialize your JSON file(2).")
                sys.exit(1)
        return True

    def create_jsons(self):
        if self.args.clear_path[0]:
            if os.path.exists(self.DEFAULT_DIRECTORY):
                shutil.rmtree(self.DEFAULT_DIRECTORY)
        if not os.path.exists(self.DEFAULT_DIRECTORY):
            os.makedirs(self.DEFAULT_DIRECTORY)
        try:
            # ITERATE THRU NUMBER OF FILES
            if int(self.args.file_count[0]) == 0:
                # Writing to JSON File with corresponding prefix
                self.p.apply_async(self.jsons_printing())
            else:
                for i in range(int(self.args.file_count[0])):
                    # Writing to JSON File with corresponding prefix
                    name_difference = self.file_prefix(i,self.args.prefix[0])
                    self.file_name = f"{self.args.path_to_save_files[0]}/{self.args.file_name[0]}_{name_difference}"
                    self.p.apply_async(self.jsons_generation())
                self.p.close()
                self.p.join()
            return True
        except Exception as ex:
            print(ex)
            return False
    def jsons_printing(self):
        for i in range(int(self.args.data_lines[0])):
            # CREATING EACH DICTIONARY TO BE APPENDED TO JSON FILE
            dictionary = self.json_analysis(self.data)
            # Serializing json
            json_object = json.dumps(dictionary)
            print(json_object)

    def jsons_generation(self):
        with open(f"{self.file_name}.json", "w", encoding='utf8') as outfile:
            # ITERATE THRU DATA LINES
            for i in range(int(self.args.data_lines[0])):
                # CREATING EACH DICTIONARY TO BE APPENDED TO JSON FILE
                dictionary = self.json_analysis(self.data)
                # Serializing json
                json_object = json.dumps(dictionary)
                # WRITING LINE TO JSON FILE
                outfile.write(json_object)
                outfile.write('\n')

    def json_analysis(self, json_file):
        unitary_dictionary = {}
        for i in json_file:
            unitary_dictionary[i] = self.sintax_check(i, json_file)
        return unitary_dictionary

    def sintax_check(self, key, expression):
        split_expression = str(expression[key]).split(':')

        # TRYING TO FIND A MATCHING TYPE OF DATA AND GENERATE IT
        try:
            if split_expression[0] == 'str' and split_expression[1] == 'rand':
                return str(uuid.uuid4())
            elif split_expression[0] == 'int' and str(type(eval(str(split_expression[1])))) == "<class 'int'>":
                return eval(str(split_expression[1]).replace('rand','random.randint'))
            elif split_expression[0] == 'str' and str(type(eval(str(split_expression[1])))) == "<class 'list'>":
                return str(random.choice(eval(str(split_expression[1]))))
            elif split_expression[0] == 'int' and str(type(eval(str(split_expression[1])))) == "<class 'list'>":
                return int(random.choice(eval(str(split_expression[1]))))
            elif split_expression[0] == 'timestamp':
                if split_expression[1] != '':
                    logging.error('Timestamp does not support any values and it will be ignored')
                return self.time_stamp()
            elif str(type(eval(split_expression[0]))) == "<class 'list'>":
                return random.choice(eval(str(split_expression[0])))
            elif split_expression[0] == 'str' and split_expression[1] == "":
                return ""
            elif split_expression[0] == 'int' and split_expression[1] == "":
                return None
            else:
                logging.info("There's none data to be generated")
                return eval(f"{split_expression[0]}({split_expression[1]})")

        except:
            logging.error("Not recognize method at data_schema")
            sys.exit(1)


if __name__ == "__main__":
    start_time = time.time()
    cli_object = Cli()
    cli_object.parse_analysis()
    cli_object.create_jsons()
    end_time = time.time()
    print(f"Time taken {end_time - start_time} seconds")

