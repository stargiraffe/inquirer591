from django.shortcuts import render
from querier import method, models


def home(request):
    if request.method == 'GET' and request.GET != {}:
        houseDatas = models.findHouseDatas(request)
        return method.makeResponse(houseDatas)
    else:
        return render(request, 'querier/home.html')

        # for houseData in houseDatas:
        #     a = {'name': houseData['name'], 'identity': houseData['identity'],
        #          'houseCondition': houseData['houseCondition'], 'houseType': houseData['houseType'],
        #          'sex': houseData['sex'], 'phone': houseData['phone']}
        #     writer = csv.DictWriter(response)
        #     writer.writerow(a)
