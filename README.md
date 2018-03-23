进入项目所在文件夹

touch README.md //新建一个记录提交操作的文档

git init //初始化本地仓库

git add README.md //添加

git commit -m "first commit"//提交到要地仓库，并写一些注释

git remote add origin git@github.com:youname/Test.git //连接远程仓库并建了一个名叫：origin的别名

git push -u origin master //将本地仓库的东西提交到地址是origin的地址，master分支下
