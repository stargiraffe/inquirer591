from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from django import forms

client = pymongo.MongoClient('mongodb://localhost:27017')
mongodb = client['db591']


def home(request):
    if request.method == 'GET' and request.GET != {}:
        name = request.GET.get('last-name', '')
        if name == '':
            name = {'$exists': True}
        else:
            name = {'$in': name.split('+')}

        identity = request.GET.getlist('identity', '')
        if identity == '':
            identity = {'$exists': True}
        else:
            identity = {'$in': identity}

        houseCondition = request.GET.getlist('house-condition', '')
        if houseCondition == '':
            houseCondition = {'$exists': True}
        else:
            houseCondition = {'$in': houseCondition}

        houseType = request.GET.getlist('house-type', '')
        if houseType == '':
            houseType = {'$exists': True}
        else:
            houseType = {'$in': houseType}

        sex = request.GET.getlist('tenant-sex', '')
        if sex == '':
            sex = {'$exists': True}
        else:
            sex = {'$in': sex}

        phone = request.GET.get('phone', '')
        if phone == '':
            phone = {'$exists': True}
        else:
            phone = {'$in': phone.split('+')}

        houseDatas = mongodb.coll.find(
            {'name': name, 'identity': identity,
             'houseCondition': houseCondition, 'houseType': houseType,
             'sex': sex, 'phone': phone}, {'_id': 0})

        context = {
            'houseDatas': houseDatas
        }

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        for row in houseDatas:
            response.write("%s\n" % str(row))
        return response

        # for houseData in houseDatas:
        #     a = {'name': houseData['name'], 'identity': houseData['identity'],
        #          'houseCondition': houseData['houseCondition'], 'houseType': houseData['houseType'],
        #          'sex': houseData['sex'], 'phone': houseData['phone']}
        #     writer = csv.DictWriter(response)
        #     writer.writerow(a)

    else:
        return render(request, 'querier/home.html')


def about(request):
    return render(request, 'querier/about.html', {'title': 'About'})
