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

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wand.display import display

def copy_src_image_with_padding(src, padding):
	dest = Image(width=(src.width+2), height=(src.height+2), background=Color('transparent'))

	with Drawing() as draw:
		draw.composite(
			operator='copy', 
			left=padding, top=padding, 
			width=src.width, height=src.height, 
			image=src)
		draw(dest)

	return dest

def draw_left_markers(image, markers, color):
	with Drawing() as draw:
		draw.fill_color = color
		for m in markers:
			draw.line((0, m[0]+1), (0, m[1]+1))
		draw(image)

def draw_top_markers(image, markers, color):
	with Drawing() as draw:
		draw.fill_color = color
		for m in markers:
			draw.line((m[0]+1, 0), (m[1]+1, 0))
		draw(image)

def draw_right_markers(image, markers, color):
	with Drawing() as draw:
		draw.fill_color = color
		for m in markers:
			draw.line((image.width - 1, m[0]+1), (image.width - 1, m[1]+1))
		draw(image)

def draw_bottom_markers(image, markers, color):
	with Drawing() as draw:
		draw.fill_color = color
		for m in markers:
			draw.line((m[0]+1, image.height - 1), (m[1]+1, image.height - 1))
		draw(image)

def gen_ninepatch(src, dest, left=None, right=None, top=None, bottom=None):
	with Image(filename=src) as src_img:
		# make 1 px padding
		with copy_src_image_with_padding(src_img, 1) as dest_img:
			# draw markers
			with Color('black') as marker_color:
				if left:
					draw_left_markers(dest_img, left, marker_color)
				if top:
					draw_top_markers(dest_img, top, marker_color)
				if right:
					draw_right_markers(dest_img, right, marker_color)
				if bottom:
					draw_bottom_markers(dest_img, bottom, marker_color)

			dest_img.save(filename=dest)
