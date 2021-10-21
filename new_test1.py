vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git branch
* master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git branch --list
* master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git checkout -b dev
Switched to a new branch 'dev'

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git branch
* dev
  master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git branch --list
* dev
  master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git branch
  dev
* master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git checkout -b dev
fatal: A branch named 'dev' already exists.

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git checkout dev
Switched to branch 'dev'

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git branch
* dev
  master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git fetch

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git status
On branch dev
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.txt

nothing added to commit but untracked files present (use "git add" to track)

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git add hello.txt

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git status
On branch dev
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.txt


vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git commit -m "this is first commit message"
[dev 19c15ad] this is first commit message
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git status
On branch dev
nothing to commit, working tree clean

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git push origin dev
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 296 bytes | 74.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'dev' on GitHub by visiting:
remote:      https://github.com/MuleCustomerModule2021/authorization-sapi-app-v1/pull/new/dev
remote:
To https://github.com/MuleCustomerModule2021/authorization-sapi-app-v1.git
 * [new branch]      dev -> dev

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git status
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello1.txt

no changes added to commit (use "git add" and/or "git commit -a")

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git diff hello.txt
diff --git a/hello.txt b/hello.txt
index c7802a8..f2aa86d 100644
--- a/hello.txt
+++ b/hello.txt
@@ -1 +1 @@
-helloworlds
+hello

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git diff hello1.txt

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git add .

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git status
On branch dev
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   hello.txt
        new file:   hello1.txt


vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git commit -m "this is second commit"
[dev eb24dfa] this is second commit
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 hello1.txt

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git push origin dev
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 343 bytes | 85.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/MuleCustomerModule2021/authorization-sapi-app-v1.git
   19c15ad..eb24dfa  dev -> dev

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git status
On branch dev
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    hello.txt

no changes added to commit (use "git add" and/or "git commit -a")

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git add hello.txt

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git commit -m "this is file deletd"
[dev c5811fa] this is file deletd
 1 file changed, 1 deletion(-)
 delete mode 100644 hello.txt

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git push origin dev
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 221 bytes | 55.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/MuleCustomerModule2021/authorization-sapi-app-v1.git
   eb24dfa..c5811fa  dev -> dev

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git status
On branch dev
nothing to commit, working tree clean

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git branch master
fatal: A branch named 'master' already exists.

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (dev)
$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git branch
  dev
* master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git merge dev
Updating c6fcc2a..c5811fa
Fast-forward
 hello1.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 hello1.txt

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$ git push origin master
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/MuleCustomerModule2021/authorization-sapi-app-v1.git
   c6fcc2a..c5811fa  master -> master

vinay@VINAY-PC MINGW64 /d/MULE_PRACTICE_DATA/authorization-sapi-app-v1 (master)
$
