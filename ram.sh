mkdir trainer
cd trainer
wget https://github.com/rohit888866/ram/releases/download/v1.2/trainer.yml
cd ..
wget https://raw.githubusercontent.com/rohit888866/ram/main/face_recognition.py
wget https://raw.githubusercontent.com/rohit888866/ram/main/haarcascade_frontalface_default.xml
python3 face_recognition.py
