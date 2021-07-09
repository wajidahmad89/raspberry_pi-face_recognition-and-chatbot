
#!/bin/bash


cd /home/pi/Desktop/trivchat

> camera-output-raw.txt

> hello_camera-output.txt

> goodbye_camera-output.txt


cd /home/pi/Desktop/facrec

> initiate.txt



cd /home/pi/Desktop/rexy_master

for((i=1;i<100;i++)); do bash runit${i}.sh & done


