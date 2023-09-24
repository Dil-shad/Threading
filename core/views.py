from django.shortcuts import render
from .models import *
from faker import Faker
fake=Faker()
import random
from .thread import CreateBulkStudentsThread


def home(request):
    count =1000
    # for i in range(count):
    #     print(i)
    #     Student.objects.create(
    #         student_name = fake.name(),
    #         Student_email =fake.email(),
    #         address =fake.address(),
    #         age =random.randint(10,50),
    #     )
    # Create and start a thread to create 100 fake students
    thread = CreateBulkStudentsThread(total=1000)
    thread.start()

    # Wait for the thread to finish (optional)
    #thread.join()

    # The thread will create the student records in the background.
    qs=Student.objects.all()
    print("Threading started")
    context={"status":"creating students ",'students':qs}
    return render(request,'index.html',context)