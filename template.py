import os
from pathlib import Path
import logging
#Loggin ayarlarının yapılması: bilgileri zaman aralığı ile birlikte loglayacaktır
logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]: %(message)s:")
#Projemizin adı                    
project_name = "textSummarizer"

#Oluşturalacak Projede Adım adım klasörlerin oluşturulması
#Oluşturacağımız listede projemiz için gerekli olan tüm klasörleri eklemiş olacağız
list_of_files = [
    ".github/workflows/.gitkeep", #Github için bir çalışma dosyası oluşturuyoruz.(Git ignore)
    f"src/{project_name}/__init__.py",#Buradaki amacı şu olacak python modülü olarak işlev görecek 
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",#Genellikle yardımcı fonksiyonlar içerir
    f"src/{project_name}/loggin/__init__.py",#Bilgileri loglar halinde gösterecek
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",#Projenin yapılandırma klasörü olacak
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/contans/__init__.py",
    "config/configuration.yaml",#Proje yapılandırma dosyası (YAML formatında olması)
    "params.yaml",#Modelin Paramaetrelerinin bulunduğu alan
    "app.py",#Uygulamanın başlatılacağı dosya
    "main.py",#Projenin ana çalışma dosyası
    "Dockerfile", #Docker container'ı oluşturmak için kullanılır
    "requirements.txt",#Python gereksinimleri yani bağımlılıkları bu proje kullanacağı kütüphaneleri
    "setup.py",#Python paketleri kurmak için kullanılan dosya
    "research/trials.ipynb",#Araştırma ve denemeler için kullanılan jupyter Notebook
]

#Dosya dizinlerinin oluşturulması için 
#For döngüsü ile dizinleri kontrol edecek ve var olanlara ekleme yapmayacak olmayanları ise kurulumunu yapacak
for filepath in list_of_files:
    filepath = Path(filepath)#dosya yolunu path objesine dönüştürmek için kullanırız
    filedir, filename = os.path.split(filepath)#Dosya yolu ve dosya adı olarak ayırır.

    #Eğer dizinde mevcut değil ise bu dizini oluştur.
    #exist_ok = True parametre dizinimiz var ise bize hata döndürmeden işlemi sonlandıracak
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creatind directory:{filedir} for the file {filename}")#Loglama işlemi diyoruz.

    #Eğer dosya yoksa yada boyutu 0 ise, boş bir dosya oluşturacak koşulumuzu ekliyoruz.
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass #Dosya oluşturulduğu için içerisine birşey yazılmaz
        logging.info(f"Creatind directory:{filedir} for the file {filename}")
    else:
        logging.info(f"{filename} is already exist") # Eğer dosya zaten var ise loglanacak