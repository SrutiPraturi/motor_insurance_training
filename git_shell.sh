mkdir gitmove
set DATESTR=%date:~10,4%-%date:~-7,2%-%date:~4,2%-%time:~0,2%-%time:~3,2%-%time:~6,2%
mkdir gitmove/%DATESTR% 

cp -r assets/* gitmove/%DATESTR%/
cd gitmove
git init
git config --global user.email "sruti_praturi@gmail.com"
git config --global user.name "Sruti "
git remote rm origin 
git remote add origin https://SrutiPraturi:Git7889@github.com/SrutiPraturi/motor_insurance_serving.git
git pull origin master
git add %DATESTR%
git commit -m "assets commit"
git push --set-upstream origin master   
