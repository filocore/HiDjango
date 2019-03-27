import uuid
from django.db import models

# Create your models here.


class Person(models.Model):
    class Meta:
        db_table = 'person'

    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.IntegerField()

    # 增

    # 实例方法方式
    def insertPerson(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

        print('向数据库添加一个 Person，name = ' + self.name + ' age = ' + self.age + ' sex = ' + self.sex)
        done = self.save(force_insert=True)
        if done:
            print("数据库插入成功")

    # 类方法方式
    @classmethod
    def addPerson(cls, name, age, sex):
        person = Person()
        person.name = name
        person.age = age
        person.sex = sex
        print('向数据库添加一个 Person，name = ' + person.name + ' age = ' + person.age + ' sex = ' + person.sex)
        done = person.save()
        if done:
            print('数据库保存成功')


    # 查

    @classmethod
    def findPerson(cls, name):

        # 查询所有
        # personList = Person.objects.all()

        # 查询单条数据
        person = Person.objects.get(name=name)
        return person


    # 改

    @classmethod
    def updatePerson(cls, id, name, age, sex):
        person = Person.objects.get(id = id)
        person.name = name
        person.age = age
        person.sex = sex
        done = person.save(force_update=True)
        if done:
            print('数据库保存成功')
        return person