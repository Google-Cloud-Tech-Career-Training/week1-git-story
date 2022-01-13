# Setup

## Local environment setup 
***Windows only***: 
On Windows, you will need to run these commands from git bash ([Git Bash download](https://git-scm.com/downloads)).


1. **Link your github to your local environment**  
  See: [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

    Or complete these steps in order:  
    - [Checking for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)  
    - [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)   (The section about "Generating a new SSH key" and the section "Adding your SSH key to the ssh-agent")
    - [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)  
    <br>  


2. **Add your git `email` and `username` to your local environment**  
    - `$ git config --global user.email "you@example.com"`  
    - `$ git config --global user.name "Your Name"`  


## Clone this repository 

  - Locate and click on the green **CODE** button in the top right of this page 
  - Select **SSH**
  - Copy the url 
  - In your terminal, `cd` into the location where you would like this repo to live. The next command will create a folder containing this repo's files. 
  - Type the following command :   
  ```git clone <url>```   (replace `<url>` with the url)

![git_screenshot_code_link](https://user-images.githubusercontent.com/34327253/149275115-b26a213a-2efe-4165-a8f1-1392b60d9f5f.png)

# Exercise 

1. Create a branch off the `main` branch  
    
    >By creating a branch, you're making a copy of the branch that you're currently on (i.e. `main`), and giving a name to this copy (your branch name). Changes to your branch will not affect the source branch. 

    Command: ```git checkout -b <name-of-your-branch>```  (replace `<name-of-your-branch>` with the name of your branch)
  
  <br>  
  
2. Assign a value to every variable in the file `words.py`

   e.g.: `name1 = "Lenz"`  
<br>

3. **Stage** your changes, preparing for the **commit**  

    >When you make changes to files you must stage them before committing them. Only staged changes will be saved when you commit. If you don't want to save the changes to a specific file for example, you could avoid staging that file. In your next commit, those changes will not be included.   

   Command:  ```git add .```  
   
   The `.` here represents "the current folder", or in other words "all files in the current folder". You could also stage a single file 
   like this: `git add words.py` . 
   
    <br>
    
 4. **Commit** your **staged** changes and write a short descriptive message about your changes.  
     
     >The commit command captures a snapshot of the project's currently staged changes. You can always roll back to this commit later, no matter what other changes you've made.   

    Command:  ```git commit -m "<short description of changes>"```
     
     <br>
     
 5. **Push** your locally committed changes to github.com  
     
     >The push command uploads all your current commits to your github repository.  
     
    Command:  ```git push```  
     ⚠️ The first time you run `git push` on a newly created branch, it does not yet exist on github. You will get an error message showing you the command to run to create this branch on github.com. It should look something like this: ```git push --set-upstream origin <name-of-your-branch>```  
     
  <br>
   
 6. Create a **Pull Request** on github
    
    >By opening a Pull Request you are requesting to merge the changes on your branch into another branch (the base branch). You can think of it as making your "copy" the main version.   
    
    1. In the **Pull Requests** menu, create a new Pull Request   
    <br>
      <!--     ![github_pr_step1](https://user-images.githubusercontent.com/34327253/149280375-693039fe-528b-4a0f-bed7-3892f415f4d2.png)      -->
      <img src="https://user-images.githubusercontent.com/34327253/149280375-693039fe-528b-4a0f-bed7-3892f415f4d2.png">
    <br>
    <br>
    <br>
    
    2. Select `main` as the base branch and your branch as the branch to compare to. Then hit **Create Pull Request**  
    <br>
      <!--     ![github_pr_step2](https://user-images.githubusercontent.com/34327253/149280373-c7da7a21-dfb4-42a0-b578-933d71c28e2b.png) -->
      <img src="https://user-images.githubusercontent.com/34327253/149280373-c7da7a21-dfb4-42a0-b578-933d71c28e2b.png">
    <br>
    <br>
    <br>
    

  
    3. Give your PR a title (use your name for this exercise), and hit **Create Pull Request**  
    <br>
      <img src="https://user-images.githubusercontent.com/34327253/149282656-d95bc2ec-832a-4a2a-b68e-442f72f39a7e.png">
      <!--    ![github_pr_step3](https://user-images.githubusercontent.com/34327253/149282656-d95bc2ec-832a-4a2a-b68e-442f72f39a7e.png) -->
    <br>
    <br>
    <br>    
    


<!-- 
     <img height=200 width=800 src="https://user-images.githubusercontent.com/34327253/149280375-693039fe-528b-4a0f-bed7-3892f415f4d2.png">
     <img height=200 width=800 src="https://user-images.githubusercontent.com/34327253/149280373-c7da7a21-dfb4-42a0-b578-933d71c28e2b.png">
     <img height=200 width=800 src="https://user-images.githubusercontent.com/34327253/149280369-923b3526-c583-47df-83b6-bc1588c2ca79.png"> -->
 
 





# Additional resources
- [Git Cheet Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [About branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)


