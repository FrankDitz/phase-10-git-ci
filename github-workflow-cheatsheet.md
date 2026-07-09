# GitHub Workflow Cheat Sheet

## Start Project
git switch main
git pull

# Create Working Feature Branch
git switch -c feature-branch

## Do Work
work work work

## Track Your Work & Save It Locally
git add .
git commit -m "Describe the work"

## Save Your Work Remotely For Others To See/Use
git push -u origin feature-branch

## Create Merge Request On Github
team reviews and accepts or declines

## Switch To Main Branch Locally & Pull Updated Main
git switch main
git pull

## Delete Feature Branch Locally & Remotely
git branch -d feature-branch
git push origin --delete feature-branch


## You Can Undo Most Recent Commit Like This
git revert --no-edit HEAD

## Or Undo A Specific Older Commit Like This
git revert --no-edit commit_hash

## Or Go Back To A Previous Commit Locally
git reset --hard commit_hash