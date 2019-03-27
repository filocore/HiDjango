from django.shortcuts import render
from django.http import HttpResponse
from djangoApp import models

from djangoApp.models import Person

# Create your views here.



def hello(request):
    return HttpResponse('Hello World')


def addPerson(request):
    name = request.GET['name']
    age = request.GET['age']
    sex = request.GET['sex']

    # models.Person.addPerson(name, age, sex)

    person = models.Person()
    # person.name = name
    # person.age = age
    # person.sex = sex
    person.insertPerson(name, age, sex)

    return HttpResponse('添加一个 Person name = ' + name + ' age = ' + age + ' sex = ' + sex)


def getPerson(request):
    name = request.GET['name']

    person = models.Person.findPerson(name)
    age = str(person.age)
    sex = str(person.sex)

    return HttpResponse('查询到一个 Person，name = ' + person.name + ' age = ' + age + ' sex = ' + sex)


def updatePerson(request):
    id = request.GET['id']
    name = request.GET['name']
    age = request.GET['age']
    sex = request.GET['sex']

    person = models.Person.updatePerson(id, name, age, sex)

    return HttpResponse('修改了一个 Person，name = ' + person.name + ' age = ' + str(age) + ' sex = ' + str(sex))