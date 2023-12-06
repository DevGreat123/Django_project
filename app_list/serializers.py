from rest_framework import serializers
from app_list.models import student,subject

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ['subject_in_school', 'student']

class studentSerializer(serializers.ModelSerializer):
    # subject_data = subject.objects.all()
    subjects = serializers.SerializerMethodField('subject_count', read_only=True)

    class Meta: 
        model = student
        fields = ['id','name','address','roll_numbers','subjects']

    def subject_count(self, obj):
        all_subjects=subject.objects.filter(student = obj.id)
        print(all_subjects,"Mmmmmmmmmm")
        array=[]

        for sub in all_subjects:
            array.append({"id":sub.id, "subject":sub.subject_in_school})
        return array