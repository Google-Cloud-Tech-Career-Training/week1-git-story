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
  - Type the following command (replace `<url>` with the url):   
  ```git clone <url>```

![git_screenshot_code_link](https://user-images.githubusercontent.com/34327253/149275115-b26a213a-2efe-4165-a8f1-1392b60d9f5f.png)

# Exercise 

1. Create a branch off the `main` branch  (replace `<name-of-your-branch>` with the name of your branch)  
  ```git checkout -b <name-of-your-branch>```
  <br>
  
2. Assign a value to every variable in the file `words.py`

   e.g.: `name1 = "Lenz"`  
<br>

3. **Stage** your changes, preparing for the **commit**  

   ```git add .``` The `.` here represents "the current folder", or in other words "all files in the current folder". You could also stage a single file 
   like this `git add words.py`. 
   
 4. **Commit** your **staged** changes and write a short descriptive message about your changes.  
 
     ```git commit -m "<short description of changes>"```
   
 5. **Push** your locally committed changes to github.com  
  
     ```git push```  
     ⚠️ The first time you run `git push` on a newly created branch, it does not yet exist on github. You will get an error message showing you the command to run to create this branch on github.com. It should look something like this: ```git push --set-upstream origin <name-of-your-branch>```  
   
 6. Create a **Pull Request** on github
 
   
   


# Additional resources
- [Git Cheet Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [About branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
- 

