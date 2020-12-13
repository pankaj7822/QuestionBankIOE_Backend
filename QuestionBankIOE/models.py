from django.db import models


class Course(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    depart_code = models.ForeignKey('Department', models.DO_NOTHING, db_column='Depart_Code')  # Field name made lowercase.
    semester = models.IntegerField(db_column='Semester')  # Field name made lowercase.
    hours_per_week = models.FloatField(db_column='Hours_per_week')  # Field name made lowercase.
    marks_code = models.ForeignKey('MarkingScheme', models.DO_NOTHING, db_column='Marks_Code')  # Field name made lowercase.
    type_code = models.ForeignKey('CourseType', models.DO_NOTHING, db_column='Type_Code')  # Field name made lowercase.
    program = models.CharField(db_column='Program', max_length=10)  # Field name made lowercase.
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'course'
        


class CourseType(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=2)  # Field name made lowercase.
    type_name = models.CharField(db_column='Type_Name', max_length=10)  # Field name made lowercase.
    
    def __str__(self):
        return self.code+"_"+self.type_name

    class Meta:
        
        db_table = 'course_type'


class Department(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        


class ExamInformation(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=3)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    
    def __str__(self):
        return self.id+"_"+str(self.year)
    

    class Meta:
        db_table = 'exam_information'
        


class MarkingScheme(models.Model):
    code = models.CharField(db_column='Code', primary_key=True, max_length=1)  # Field name made lowercase.
    full_marks = models.IntegerField(db_column='Full_Marks')  # Field name made lowercase.
    pass_marks = models.IntegerField(db_column='Pass_Marks')  # Field name made lowercase.
    duration = models.FloatField(db_column='Duration')  # Field name made lowercase.
    
    def __str__(self):
        return self.code+"_"+str(self.full_marks)

    class Meta:
        db_table = 'marking_scheme'
        


class QuestionPaper(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paper_link = models.TextField(db_column='Paper_link', blank=True, null=True)  # Field name made lowercase.
    exam = models.ForeignKey(ExamInformation, models.DO_NOTHING, db_column='Exam_Id')  # Field name made lowercase.
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='Course_ID')  # Field name made lowercase.
    
    def __str__(self):
        return self.exam.id+"_"+self.course.title
    

    class Meta:
        db_table = 'question_paper'
        
