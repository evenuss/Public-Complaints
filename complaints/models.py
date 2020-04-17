from django.conf import settings
from django.db import models
from django.utils import timezone



class Petugas(models.Model):
    id_petugas = models.AutoField(primary_key=True)
    nama_petugas = models.CharField(max_length=35)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    telp = models.CharField(max_length=13)
    LEVEL_CHOICES = (
        ('admin','Admin'),
        ('petugas','Petugas'),
    )
    level = models.CharField(max_length=20,choices=LEVEL_CHOICES, unique=True)
    
    def __int__(self):
        return self.pk



class Masyarakat(models.Model):
    nik = models.CharField(max_length=16, primary_key=True)
    nama = models.CharField(max_length=35)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=32)
    telp = models.CharField(max_length=13)
    
    def __str__(self):
        return self.nik


class Pengaduan(models.Model):
    id_pengaduan = models.AutoField(primary_key=True)
    tgl_pengaduan = models.DateField()
    nik = models.ForeignKey(Masyarakat, on_delete=models.CASCADE)
    isi_laporan = models.TextField()
    foto = models.ImageField()
    STATUS_CHOICES = (
        ('belum','0'),
        ('sedang','Proses'),
        ('sudah','Selesai'),
    )
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, unique=True)

    def __int__(self):
        return self.pk

class Tanggapan(models.Model):
    id_tanggapan = models.AutoField(primary_key=True)
    id_pengaduan = models.ForeignKey(Pengaduan, on_delete=models.CASCADE)
    tgl_tanggapan = models.DateField()
    tanggapan = models.TextField()
    id_petugas =  models.ForeignKey(Petugas, on_delete=models.CASCADE)

    def __str__(self):
        return self.tanggapan