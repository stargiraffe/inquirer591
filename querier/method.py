from django.http import HttpResponse
from querier import env


def default(request, id):
    query = request.GET.getlist(id, '')
    if query == '':
        query = {'$exists': True}
    else:
        query = {'$in': query}
    return query


def splitPlus(request, id):
    query = request.GET.get(id, '')
    if query == '':
        query = {'$exists': True}
    else:
        query = {'$in': query.split('+')}
    return query


def makeResponse(houseDatas):
    resp = HttpResponse(content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename=' + env.fileName

    for row in houseDatas:
        resp.write("%s\n" % str(row))
    return resp
