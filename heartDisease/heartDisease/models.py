from django.db import models



class Patient(models.Model):
        age = models.IntegerField()
        sex = models.IntegerField()
        cp = models.IntegerField()
        trestbps = models.IntegerField()
        chol = models.IntegerField()
        fbs = models.IntegerField()
        restecg = models.IntegerField()
        thalach = models.IntegerField()
        exang = models.IntegerField()
        oldpeak = models.FloatField()
        slope = models.IntegerField()
        ca = models.IntegerField()
        thal = models.IntegerField()
    
        def __str__(self):
            return 'Age:'+str(self.age)+'  ' + 'Sex:'+str(self.sex)+"  " + 'Cp:'+str(self.cp) +" "+ 'Trestbps:'+str(self.trestbps)+" " + 'Chol:'+str(self.chol)+" "+ 'Fbs:'+str(self.fbs)+" " + 'Restecg:'+str(self.restecg)+ "  " + 'Thalach:'+str(self.thalach) + 'Exang:'+str(self.exang) + " "+'Oldpeak:'+str(self.oldpeak)+ "  " + 'Slope:'+str(self.slope)+"  " + 'Ca:'+str(self.ca)+" " + 'Thal:'+str(self.thal)