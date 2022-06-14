from django.http import Http404, HttpResponse
from django.conf import settings
from project.noddy.doc import make_pdf
def view_pdf(reqquest):
    try:
        content = make_pdf()
        resp = HttpResponse(content=content, content_type='application/pdf')
        download_name = "django-view.pdf"
        resp['Content-Disposition'] = 'inline; filename=%s' % download_name
        return resp
    except:
        raise Http404("view_pdf failed")
