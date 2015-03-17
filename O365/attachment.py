# Copyright 2015 by Toben "Narcolapser" Archer. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its documentation for any purpose 
# and without fee is hereby granted, provided that the above copyright notice appear in all copies and 
# that both that copyright notice and this permission notice appear in supporting documentation, and 
# that the name of Toben Archer not be used in advertising or publicity pertaining to distribution of 
# the software without specific, written prior permission. TOBEN ARCHER DISCLAIMS ALL WARRANTIES WITH 
# REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT 
# SHALL TOBEN ARCHER BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES 
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE 
# OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
This file contains the functions for working with attachments. Including the ability to work with the
binary of the file directly. The file is stored locally as a string using base64 encoding. 
"""

import base64
import logging
import json
import requests

logging.basicConfig(filename='o365.log',level=logging.DEBUG)

log = logging.getLogger(__name__)

class Attachment( object ):
	'''
	Attachment class is the object for dealing with attachments in your messages. To add one to
	a message, simply append it to the message's attachment list (message.attachments). 
	'''
	def __init__(self,json):
		self.json = json
		self.content = json['ContentBytes']
		self.name = json['Name']
		self.isPDF = '.pdf' in self.name.lower()

#	def __getattr__(self,name):
#		return self.json[name]

#	def __setattr__(self,name,value):
#		self.json[name] = value
	
	def save(self,location):
		'''
		Location: path to where the file is to be saved.

		Save the attachment locally to disk.
		'''
		if not self.isPDF:
			log.debug('we only work with PDFs.')
			return False
		try:
			outs = open(location+'/'+self.Name,'wb')
			outs.write(base64.b64decode(self.ContentBytes))
			outs.close()
			log.debug('file saved locally.')
			
		except Exception as e:
			log.debug('file failed to be saved: %s',str(e))
			return False

		log.debug('file saving successful')
		return True

	def byteString(self):
		'''
		fetch the binary representation of the file. useful for times you want to
		skip the step of saving before sending it to another program. This allows
		you to make scripts that use linux pipe lines in their execution.
		'''
		if not self.isPDF:
			log.debug('we only work with PDFs.')
			return False

		try:
			return base64.b64decode(self.ContentBytes)

		except Exception as e:
			log.debug('what? no clue went wrong here. cannot decode')

		return False

#To the King!
