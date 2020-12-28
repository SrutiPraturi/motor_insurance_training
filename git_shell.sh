mkdir gitmove
mkdir gitmove/assets

cp -r assets/* gitmove/assets/
cd gitmove
git init
git config --global user.email "sruti_praturi@gmail.com"
git config --global user.name "Sruti "
git remote rm origin 
git remote add origin https://SrutiPraturi:Git7889@github.com/SrutiPraturi/motor_insurance_serving.git
git pull origin master
git add assets
git commit -m "assets commit"
git push --set-upstream origin master   
