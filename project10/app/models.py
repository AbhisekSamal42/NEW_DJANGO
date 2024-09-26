from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=14)
    LOC=models.CharField(max_length=13)
    #def _str_(self):
    #    return self.DNAME
    def _str_(self):
        return str(self.DEPTNO)
    '''def _str_(self):
        return self.LOC'''
class EMP(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=10)
    JOB=models.CharField(max_length=9)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    HIREDATE=models.DateField()
    SAL=models.FloatField(max_length=7)
    COMM=models.FloatField(max_length=7,null=True,blank=True)
    DEPTNO=models.ForeignKey(DEPT,on_delete=models.CASCADE)
    # def _str_(self):
    #     return str(self.EMPNO)
    def _str_(self):
        return self.ENAME
    # def _str_(self):
    #     return str(self.MGR)
    # def _str_(self):
    #     return self.JOB
    # def _str_(self):
    #     return self.HIREDATE
    # def _str_(self):
    #     return self.SAL
    # def _str_(self):
    #     return self.COMM
class BONUS(models.Model):
    ENAME=models.CharField(max_length=10)
    JOB=models.CharField(max_length=9)
    SAL=models.IntegerField()
    COMM=models.IntegerField()
    def _str_(self):
        return self.ENAME
    # def _str_(self):
    #     return self.JOB
    # def _str_(self):
    #     return str(self.SAL)
    # def _str_(self):
    #     return str(self.COMM)
class SALGRADE(models.Model):
    GRADE=models.IntegerField()
    LOSAL=models.IntegerField()
    HISAL=models.IntegerField()
    def _str_(self):
        return str(self.GRADE)
    # def _str_(self):
    #     return self.LOSAL
    # def _str_(self):
    #     return self.HISAL