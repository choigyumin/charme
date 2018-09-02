echo 'git automation push, argument is commit message.'
git add .
git commit -m $1
git push origin master
