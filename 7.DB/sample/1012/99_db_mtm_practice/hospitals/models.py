from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # 외래키 삭제#
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # 다대다필드 생성 #
    doctors =models.ManyToManyField(Doctor, related_name='patients', through='Reservation') # 환자가 의사를 참조함 Doctor에 넣으면 반대
    name = models.TextField()               # patients_set을 patients로 만듦

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'

