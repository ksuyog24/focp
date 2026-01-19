git init

git add .

git commit -m "First commit"

git branch -M main (Add this! It ensures your branch is named 'main' so the push doesn't fail)

git remote add origin <PASTE_YOUR_LINK_HERE>

git push -u origin main




or 



git clone <URL_OF_OLD_REPO>

cd <NAME_OF_FOLDER>

git remote remove

git remote add origin <github.com/YOUR_USERNAME/NEW_REPO.git>

git add .

git commit -m "added practice"

git push -u origin main
