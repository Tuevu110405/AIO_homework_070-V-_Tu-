import torch
import math

# Task 1

class Softmax:

    def __call__(self, data):
        self.data = data
        self.result = torch.zeros(self.data.shape)
        exp_data = torch.exp(self.data)
        sum_exp_data = exp_data.sum(dim=-1, keepdim=True)
        self.result = exp_data / sum_exp_data

        return self.result
    
class softmax_stable:
    
    def __call__(self, data):
        self.data = data
        self.result = torch.zeros(self.data.shape)
        # get max value
        m_value, _ = torch.max(self.data, dim = 0)
        #columnize max_value
        m_value = m_value.unsqueeze(0)
        exp_data = torch.exp(self.data-m_value)
        sum_exp_data = exp_data.sum(dim=-1, keepdim=True)
        self.result = exp_data / sum_exp_data

        return self.result

#Task 2
class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade
        self.age = 2024 - self.yob

    def describe(self):
        print(f'Student - Name : {self.name} - YoB : {self.yob} - Grade : {self.grade}')
    
    

class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject
        self.age = 2024 - self.yob

    def describe(self):
        print(f'Teacher - Name : {self.name} - YoB : {self.yob} - Subject : {self.subject}')

class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.spec = specialist
        self.age = 2024 - self.yob

    def describe(self):
        print(f'Doctor - Name : {self.name} - YoB : {self.yob} - Subject : {self.spec}')    

class Ward:
    def __init__(self, ward ):
        self.w = ward
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        print(f'Ward Name:{self.w}\n')
        
        for person in self.people:
            print(f'{person.describe()}\n')
    
    def count_doctor(self):
        count = 0
        for person in self.people:
            if isinstance(person, Doctor):
                count += 1
        
        return count
    
    def sort_age(self):
        #bubble sort 
        sort_a = self.people
        for _ in range(len(sort_a)):
            swapped = False
            for j in range(0, len(sort_a) - _ -1):
                if sort_a[j].age > sort_a[j + 1].age:
                    swapped = True
                    sort_a[j], sort_a[j + 1] = sort_a[j + 1],sort_a[j]
            if not swapped:
                return sort_a

        return sort_a

    def compute_average(self):
        count = 0
        a_age = 0
        for person in self.people:
            if isinstance(person, Teacher):
                count += 1
                a_age += person.age


        return (a_age/ count)                    


#Task 3
class MyStack:
    def __init__(self, capacity):
        self.cap = capacity
        self.list = []
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self.list) == self.cap:
            return True
        return False
    
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            a= self.list[len(self.list)- 1]
            self.list.pop(a)
            return a
        
    def push(self, a):
        if not self.is_full():
            self.list.append(a)
        else:
            print("Cannot push more")
    
    def top(self):
        if self.is_empty():
            print("stack is empty")
        else:
            return self.list[len(self.list)- 1]

#Task 4
class MyQueue:
    def __init__(self, capacity):
        self.cap = capacity
        self.list = []
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self.list) == self.cap:
            return True
        return False
    
    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.list[0]
    
    def enqueue(self, a):
        
        if not self.is_full():
            self.list.insert(0,a)
        else:
            print("Cannot enqueue more")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            a = self.list[0]
            self.list.pop(0)
            return a





        



              






#example
data=torch.Tensor([1 , 2 , 3])
softmax = Softmax()
output = softmax(data)
print(output)

softmax_stable = softmax_stable ()
output = softmax_stable ( data )
print(output)


teacher2 = Teacher (" teacherB ",1995 , " History ")
doctor2 = Doctor ( " doctorB ", 1975 , " Cardiologists ")
ward1 = Ward ( " Ward1 ")

ward1 . add_person ( teacher2 )

ward1 . add_person ( doctor2 )
ward1 . describe ()
print(ward1.count_doctor())
ward1.sort_age()
ward1.describe()
print(ward1.compute_average())
student1 = Student ( name =" studentZ2023 ", yob =2011 , grade ="6")
assert student1 . yob == 2011
student1 . describe ()

teacher1 = Teacher ( name =" teacherZ2023 ", yob =1991 , subject =" History ")
assert teacher1 . yob == 1991
teacher1 . describe ()

queue1 = MyQueue ( capacity =5)
queue1 . enqueue (1)
assert queue1 . is_full () == False
queue1 . enqueue (2)
print ( queue1 . front () )
