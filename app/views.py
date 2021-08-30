from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from . models import *
# Create your views here.

class StudentsView(APIView):        #class students details view here student_details_serializer
    serializer_class = student_details_serializer

    def get(self, request, *args, **kwargs):
        stud_info = student_details.objects.all()
        serializer = student_details_serializer(stud_info, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = student_details_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)#, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddMarks(APIView):
    serializer_class = student_details_serializer
    def get_object(self, pk):
        try:
            return student_details.objects.get(pk=pk)
        except student_details.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, pk, format=None):
        detail = self.get_object(pk)
        serializer = student_details_serializer(detail)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        stud = self.get_object(pk)
        serializer = student_details_serializer(stud, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           


class ParticularStudentMarks(APIView):
    def get(self, request, pk, format=None):
        try:
            detail = student_details.objects.filter(id=pk).values('Name', 'marks')
            return Response(detail)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class MarkAllStudents(APIView):        #Mark of all students
    serializer_class = student_details_serializer

    def get(self, request, *args, **kwargs):
        stud_info = student_details.objects.all().values('Name', 'marks')
        return Response(stud_info)

class StudentsResults(APIView):
    
    serializer_class = student_details_serializer

    def get(self,request, *args, **kwargs):

        numberofstudents=student_details.objects.count()
        stud_info = student_details.objects.all().values('marks')
        serializer = student_details_serializer(stud_info, many=True)
        grade=list()

        for i in serializer.data:
            info = i['marks']
            print(type(info))
            # if info != None:
            if (info>=91 and info<=100):
                grade.append("A")
            elif (info >=81 and info<=90):
                grade.append("B")
            elif (info >=71 and info<=80):
                grade.append("C")
            elif (info >=61 and info<=70):
                grade.append("D")
            elif (info >=51 and info<=60):
                grade.append("E")
            elif (info<55):
                grade.append("F")

        obj = {
            "a": grade.count("A"),
            "b": grade.count("B"),
            "c": grade.count("C"),
            "d": grade.count("D"),
            "e": grade.count("E"),
            "f": grade.count("F")
        }

        distinction=(obj['a']/numberofstudents)*100
        firstclass=(obj['b']+obj['c'])/numberofstudents*100
        pass_=(numberofstudents-obj['f'])/numberofstudents*100

        return Response({
            "TOTAL NUMBER OF STUDENTS":numberofstudents,
            "DISTINCTION": distinction,
            "FIRST CLASS": firstclass,
            "PASS": pass_
        })
        
        
        
        
        