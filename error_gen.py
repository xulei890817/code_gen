import sys

import argparse

parser = argparse.ArgumentParser(prog="代码生成器", description='自动生成错误类')
parser.add_argument('json_list', metavar='json_file_list', type=str, default=["*"], nargs='*',
                    help='json template 文件')
parser.add_argument('-c', '--check', dest='check',
                    help='检查json文件', action="store_true")
parser.add_argument('-g', '--gen', dest='gen',
                    help='构建文件', type=str, choices=['class', 'docs', 'markdown'],)
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0')
args = parser.parse_args()

print(args.check)
