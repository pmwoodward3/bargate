#!/usr/bin/python
#
# This file is part of Bargate.
#
# Bargate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Bargate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Bargate.  If not, see <http://www.gnu.org/licenses/>.

import mimetypes

mimemap = {
	'application/msword' : 'Microsoft Word Document',
	'application/vnd.openxmlformats-officedocument.wordprocessingml.document' : 'Microsoft Word Document XML',
	'application/vnd.openxmlformats-officedocument.presentationml.presentation' : 'Microsoft Powerpoint XML',
	'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' : 'Microsoft Excel XML',
	'application/vnd.ms-powerpoint' : 'Microsoft Powerpoint',
	'application/octet-stream' : 'Binary file (executable or image)',
	'application/mathematica' : 'Mathematica File',
	'application/x-shockwave-flash' : 'Shockwave Flash',
	'application/vnd.visio' : 'Microsoft Visio',
	'application/vnd.ms-excel' : 'Microsoft Excel',
	
	'message/rfc822' : 'E-Mail Message',
	'text/calendar' : 'Calendar File',
	'application/x-java-archive' : 'Java Archive',
	'application/vnd.oasis.opendocument.presentation' : 'Open Document Presentation',
	'application/vnd.oasis.opendocument.spreadsheet' : 'Open Document Spreadsheet',
	'application/vnd.oasis.opendocument.text' : 'Open Document Text',

	'text/csv' : 'CSV - Comma Seperated Values',
	'text/css' : 'CSS - Cascading Style Sheet',
	'application/pdf' : 'PDF - Portable Document Format',
	'text/plain' : 'Plain text',
	'application/x-perl' : 'Perl File',
	'text/x-python' : 'Python File',
	'text/xml' : 'XML - eXtensible Markup Language',
	'application/xml' : 'XML - eXtensible Markup Language',
	'application/postscript' : 'Postscript',
	'text/html' : 'HTML - Hypertext Markup Language',
	'application/xhtml+xml' : 'XHTML - XML and HTML',

	'image/vnd.microsoft.icon' : 'Microsoft Icon',
	'image/bmp' : 'Bitmap Image',
	'image/x-xpixmap' : 'Pixmap Image',
	'image/png' : 'PNG Image (Portable Network Graphics)',
	'image/jpeg' : 'JPEG Image',
	'image/gif' : 'GIF Image',
	'image/tiff' : 'TIFF Image',
	'image/svg' : 'SVG Image (Scalable Vector Graphic)',

	'video/mp4' : 'Video - MPEG4',
	'video/mpeg' : 'Video - MPEG2',
	'video/ogg' : 'Video - OGG',
	'video/x-msvideo' : 'Video - AVI',
	'video/quicktime' : 'Video - Quicktime',

	'audio/x-wav' : 'Audio - WAV',
	'audio/x-ms-wma' : 'Audio - WMA - Windows Media Audio',
	'audio/mpeg' : 'Audio - MPEG',
	'audio/basic' : 'Audio - Basic',

	'application/x-gzip' : 'Compressed File - GZIP',
	'application/x-tar' : 'File Archive - TAR',
	'application/zip' : 'Compressed File - ZIP',
	'application/vnd.ms-cab-compressed' : 'Compressed File - Microsoft CABinet',
}

## returns true if this file type should be viewed in browser
def view_in_browser(mtype):
	"""Returns true if the file mime type passed to this function
	means that the file should be shown 'in browser'
	"""
	if mtype == 'application/pdf':
		## changed in oct 2013 becasue browsers like firefox dont have in-browser
		## pdf viewers and so the filename is barfed up - problem with flask's send_file
		return False
	elif mtype == 'text/plain':
		return True
	elif mtype.startswith('image'):
		return True
	else:
		return False

def mimetype_to_icon(mtype):
	"""Converts a file mime type into an icon
	to be displayed next to the file name.
	"""

	## default type
	ficon = 'icomoon-file4'

	## IMAGES, AUDIO, VIDEO
	if mtype.startswith('image'):
		ficon = 'icomoon-image2'
		
	elif mtype.startswith('audio'):
		ficon = 'icomoon-music'
		
	elif mtype.startswith('video'):
		ficon = 'icomoon-film'
		
	elif mtype.startswith('message'):
		ficon = 'icomoon-mail4'
		
		
	## VISIO
	elif mtype.startswith('application/vnd.visio'):
		ficon = 'icomoon-tree'		
		
	## EXECUTABLE FILES
	elif mtype.startswith('application/octet-stream'):
		ficon = 'icomoon-cog2'
		
	## ARCHIVE FILES
	elif mtype.startswith('application/x-gzip'):
		ficon = 'icomoon-file-zip'
	elif mtype.startswith('application/x-gtar'):
		ficon = 'icomoon-file-zip'
	elif mtype.startswith('application/x-tar'):
		ficon = 'icomoon-file-zip'
	elif mtype.startswith('application/zip'):
		ficon = 'icomoon-file-zip'
	elif mtype.startswith('application/vnd.ms-cab-compressed'):
		ficon = 'icomoon-file-zip'
	elif mtype.startswith('application/x-rpm'):
		ficon = 'icomoon-file-zip'
		
	## SPREADSHEETS
	elif mtype.startswith('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
		ficon = 'icomoon-file-excel'
	elif mtype.startswith('application/vnd.ms-excel'):
		ficon = 'icomoon-file-excel'
	elif mtype.startswith('application/vnd.oasis.opendocument.spreadsheet'):
		ficon = 'icomoon-libreoffice'
				
	## WORD / WRITER
	elif mtype.startswith('application/msword'): 
		ficon = 'icomoon-file-word'
	elif mtype.startswith('application/vnd.openxmlformats-officedocument.wordprocessingml.document'): 
		ficon = 'icomoon-file-word'
	elif mtype.startswith('application/vnd.oasis.opendocument.text'): 
		ficon = 'icomoon-libreoffice'		
			
	## PRESENTATIONS		
	elif mtype.startswith('application/vnd.ms-powerpoint'):
		ficon = 'icomoon-file-powerpoint'
	elif mtype.startswith('application/vnd.openxmlformats-officedocument.presentationml.presentation'):
		ficon = 'icomoon-file-powerpoint'
	elif mtype.startswith('application/vnd.oasis.opendocument.presentation'):
		ficon = 'icomoon-libreoffice'
		
	## PDF
	elif mtype.startswith('application/pdf'):
		ficon = 'icomoon-file-pdf'	

	## Text/html
	elif mtype.startswith('text/html'):
		ficon = 'icomoon-file-xml'
	elif mtype.startswith('application/xhtml+xml'):
		ficon = 'icomoon-file-xml'
	elif mtype.startswith('text/css'):
		ficon = 'icomoon-file-css'
		
	## XML
	elif mtype.startswith('text/xml') or mtype.startswith('application/xml'):
		ficon = 'icomoon-file-xml'
		
	## Code
	elif mtype.startswith('application/x-perl'):
		ficon = 'icomoon-code'
	elif mtype.startswith('application/x-python'):
		ficon = 'icomoon-code'
	elif mtype.startswith('application/x-perl'):
		ficon = 'icomoon-code'
	elif mtype.startswith('application/x-sh'):
		ficon = 'icomoon-console'
		
	elif mtype.startswith('text/plain'):
		ficon = 'icomoon-file3'
		
	## generic application
	elif mtype.startswith('application'):
		ficon = 'icomoon-drawer2'
		
	return ficon

def filename_to_mimetype(filename):
	"""Takes a filename and returns the mime type for the file based
	upon the file extension only.
	"""
	
	## Load in /etc/mime.types on Linux
	#mimetypes.init()

	## guess a mimetype from python mime types
	(mtype,enc) = mimetypes.guess_type(filename,strict=False)

	## If mimetypes module didn't detect anything
	if mtype == None:
		return ("Unknown file type","unknown")
	
	try:
		friendly = mimemap[mtype]
	except KeyError as e:
		friendly = mtype

	return (friendly,mtype)


