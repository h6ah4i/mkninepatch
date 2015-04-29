# Copyright (C) 2015 Haruki Hasegawa
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from argparse import ArgumentParser

class ninepatch_argparser:
	ifile = ""
	ofile = ""
	left = []
	top = []
	right = []
	bottom = []

	def __init__(self, progargs):
		### setup parser
		parser = ArgumentParser()

		parser.add_argument('input_png')
		parser.add_argument('output_png')

		parser.add_argument('-l1', '--left1', nargs=2, type=int)
		parser.add_argument('-l2', '--left2', nargs=2, type=int)
		parser.add_argument('-l3', '--left3', nargs=2, type=int)
		parser.add_argument('-l4', '--left4', nargs=2, type=int)

		parser.add_argument('-t1', '--top1', nargs=2, type=int)
		parser.add_argument('-t2', '--top2', nargs=2, type=int)
		parser.add_argument('-t3', '--top3', nargs=2, type=int)
		parser.add_argument('-t4', '--top4', nargs=2, type=int)

		parser.add_argument('-r', '--right', nargs=2, type=int)

		parser.add_argument('-b', '--bottom', nargs=2, type=int)

		### parse arguments
		args = parser.parse_args(progargs[1:])

		self.ifile = args.input_png
		self.ofile = args.output_png

		if args.left1:
			self.left.append(args.left1)

		if args.left2:
			self.left.append(args.left2)

		if args.left3:
			self.left.append(args.left3)

		if args.left4:
			self.left.append(args.left4)

		if args.top1:
			self.top.append(args.top1)

		if args.top2:
			self.top.append(args.top2)

		if args.top3:
			self.top.append(args.top3)

		if args.top4:
			self.top.append(args.top4)

		if args.right:
			self.right.append(args.right)

		if args.bottom:
			self.bottom.append(args.bottom)
