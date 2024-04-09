"""SimpleApp.py"""
from pyspark.sql import SparkSession

import argparse
import sys

class SimpleApp(object):
    def __init__(self, args):
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", help="File to process", required=True)
        parser.add_argument("--char01", help="Character 01", required=False)
        parser.add_argument("--char02", help="Character 02", required=False)
        self.args = parser.parse_args(args=args)

        self.file = self.args.file
        self.char_01 = self.args.char01
        self.char_02 = self.args.char02

    def process(self):
        logFile = self.file  # Should be some file on your system
        spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
        logData = spark.read.text(logFile).cache()

        num01 = logData.filter(logData.value.contains(self.char_01)).count()
        num02 = logData.filter(logData.value.contains(self.char_02)).count()

        print(f'Lines with {self.char_01}: {num01}, lines with {self.char_02}: {num02}')

        spark.stop()

    def main(self):
        """main"""
        self.process()

def main():
    """main"""
    SimpleApp(sys.argv[1:]).main()


if __name__ == '__main__':
    SimpleApp(sys.argv[1:]).main()
