import os, io
import preppy
from rlextra.rml2pdf import rml2pdf
def make_pdf():
	rmldir = os.path.join(os.path.dirname(__file__),'rml')
	mod = preppy.getModule('template.prep',rmldir,savePyc=False,importModule=False)
	rml = mod.getOutput(dict(
							rmldir = rmldir,
							pdfImage = 'excel-colors.pdf',
							V = 'I am a variable',
							),
			quoteFunc=preppy.bStdConv)
	out = io.BytesIO()
	rml2pdf.go(rml,outputFileName=out)
	return out.getvalue()

def generate(ofn,verbosity=1):
	dirn = os.path.dirname(ofn)
	if not os.path.isdir(dirn):
		os.makedirs(dirn)
	with open(ofn,'wb') as f:
		f.write(make_pdf())
	if verbosity:
		print(f'##### generated {ofn}')

if __name__=='__main__':
	generate(os.path.join(os.path.dirname(__file__),'out','cli-out.pdf'))
