# coding=utf-8
# Created by sharon
# Copyright © 2019 Bytedance.Inc
# ios_package
import os
import sys
import subprocess

if len(sys.argv) != 5:
    print("please enter package parameters~")
    os._exit(0)

repo_path = sys.argv[1]
branch = sys.argv[2]
ios_version = sys.argv[3]
rust_version = sys.argv[4]

if checkStatus():
    print("please stash first~")
    os._exit(0)

subprocess.check_output(["git","fetch"])







#检查本地工作区
def checkStatus():
    return subprocess.check_output(["git", "status"])

#检查是否已经开了对应的release分支，有就checkout过去，没有就新开一个
def checkBranches(release_branch):

    remote_branches = subprocess.check_output(["git","branch","-r"]).split('\n')

    local_branches = subprocess.check_output(["git","branch"]).split('\n')

    if "origin/"+release_branch in remote_branches:
        subprocess.check_output(["git","co",relase_branch])
        updateLark()
    elif release_branch not in local_branches:
        updateLark()
        subprocess.check_output(["git","co","-b",relase_branch])
        subprocess.check_output(["git","push","-u","origin", relase_branch])
    if true:
        branches
    else:
        new_branch = subprocess.check_output(["git","co","-b",relase_branch]).split('\n')
        if new_branch == ""

    print(len(branches))


    print(branches)

def modifyVersion():
    

def updateLark():
    subprocess.check_output(["git","pull","--rebase"])
    subprocess.check_output(["git","submodule","update"])

def updatePod():
    subprocess.check_output(["pod","install","--repo-update"])


def main():
#    if checkStatus():
#        print("please stash first~")
#        return
    if len(sys.argv) != 5:
        print("please enter package parameters~")
        return
    repo_path = sys.argv[1]
    branch = sys.argv[2]
    ios_version = sys.argv[3]
    rust_version = sys.argv[4]

#    checkBranches(branch)

    print(repo_path)
    print(branch)
    print(ios_version)
    print(rust_version)

    print(os.getcwd())



if __name__ == '__main__':
    main()

