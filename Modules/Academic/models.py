from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Career(models.Model):
    code = models.CharField(max_length=3, primary_key=True  ) 
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)
    
    #when an instance of this model is shown this text will be shown
    def __str__(self):
        txt = "{0} (Duration: {1} years(s))"
        return txt.format(self.name, self.duration)
    

class Student(models.Model):
    id= models.CharField(max_length=8, primary_key=True)
    surname = models.CharField(max_length=35)
    secondSurname = models.CharField(max_length=35)
    name = models.CharField( max_length=35)
    birthDate=models.DateField()
    genders= [('F', "Female"), ('M', "Male")]
    gender = models.CharField(max_length= 1, choices=genders, default= 'F')
    career = models.ForeignKey(Career, null= False, blank=False, on_delete=models.CASCADE) #cascade means if 
                                                                                            #career is delete so does the student
    vigencia = models.BooleanField(default=True)   
    
    def fullName(self):
        txt = "{0} {1}, {2}" 
        return txt.format(self.surname, self.secondSurname, self.name)     
    
    def __str__(self):
        txt = "{0} /Career: {1} / {2}"
        if self.vigencia:
            studentState = "ACTIVE"
        else:
            studentState = "INACTIVE"
        return txt.format(self.fullName(), self.career, studentState)

class Course(models.Model):
    code = models.CharField(max_length=6,  primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.PositiveBigIntegerField()
    teacher = models.CharField(max_length=100)
    
    def __str__(self):
        txt = "{0} ({1}) / Teacher: {2}"    
        return txt.format(self.name, self.code, self.teacher)
    
class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null = False, blank = False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null = False, blank=False, on_delete= models.CASCADE)
    dateEnrollment = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        txt = "{0} Enrolled in the course {1} / Date: {2}" 
        dateEnr = self.dateEnrollment.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.student.fullName(), self.course, dateEnr)
        
