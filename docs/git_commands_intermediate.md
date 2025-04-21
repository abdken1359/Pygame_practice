
---

### **1. `git status`**  
**What it does:**  
Shows the current status of your repository. This command will let you know:
- Which files have been **modified**, **staged**, or are **untracked**.
- If there’s anything that hasn’t been committed yet.

**Use case:**  
Whenever you're working on something, you can check to see what’s changed and what hasn’t.

---

### **2. `git diff`**  
**What it does:**  
Shows the differences between your working directory and the last commit. It tells you **exactly** what lines were added or removed in the files you’ve changed.

**Use case:**  
Before committing, you can run `git diff` to preview your changes and make sure you're only committing what you want.

---

### **3. `git log`**  
**What it does:**  
Shows the commit history of your repository. By default, it lists commits in reverse chronological order.

You can also use:
- `git log --oneline` for a simpler, more compact view.
- `git log --graph` to see a visual representation of your commit history.

**Use case:**  
When you need to review the commit history, track changes, or find a previous commit.

---

### **4. `git branch`**  
**What it does:**  
Shows all the branches in your repository. By default, you'll have a `master` (or `main`) branch.

You can also:
- Create a new branch with `git branch <branch_name>`.
- Switch branches with `git checkout <branch_name>` (or `git switch <branch_name>`).
- Delete a branch with `git branch -d <branch_name>`.

**Use case:**  
When working on new features or bug fixes, it’s best practice to work in a **separate branch** rather than directly in `master`. This keeps your codebase clean and organized.

---

### **5. `git checkout`**  
**What it does:**  
- Switches branches.
- Can also be used to **discard changes** in your working directory.

**Use case:**
- `git checkout <branch_name>` — Switch to a different branch.
- `git checkout -- <file>` — Discard changes to a specific file (revert it to the last committed state).

---

### **6. `git merge`**  
**What it does:**  
Merges changes from one branch into another. For example, if you’ve been working on a **feature branch** and you want to merge it into `main`, you use `git merge`.

**Use case:**  
You finish working on a feature or fix and want to bring those changes into the `main` branch.

---

### **7. `git rebase`**  
**What it does:**  
Rebases a branch onto another. It allows you to take the changes from one branch and "reapply" them on top of another branch, usually to make the history cleaner.

**Use case:**  
Use `git rebase` to keep a clean history and avoid the "merge commit" clutter. It can be a bit tricky because it rewrites history, so use it with caution. For example:
- `git rebase main` — Rebases your current branch on top of `main` branch.

---

### **8. `git stash`**  
**What it does:**  
Temporarily saves changes that you’re not ready to commit yet. Think of it like a **temporary clipboard** for your uncommitted work.

**Use case:**  
If you need to switch to another branch, but you have uncommitted changes, you can `git stash` those changes, then `git stash pop` when you're ready to apply them again.

---

### **9. `git remote`**  
**What it does:**  
Manages the connections to remote repositories. It shows the remote repositories associated with your project.

For example:
- `git remote -v` — Lists all remotes and their URLs.
- `git remote add <remote_name> <url>` — Adds a new remote repository.
- `git remote remove <remote_name>` — Removes a remote repository.

**Use case:**  
When collaborating with others, you may need to manage multiple remote repositories (like GitHub, GitLab, etc.).

---

### **10. `git fetch`**  
**What it does:**  
Fetches the latest changes from the remote repository without modifying your local working directory. It updates the remote tracking branches.

**Use case:**  
When you want to check if there are any updates on the remote repository, but you don’t want to merge those changes yet.

---

### **11. `git pull`**  
**What it does:**  
Fetches the latest changes from the remote repository **and** merges them into your local working directory.

**Use case:**  
When you're ready to pull in the latest changes made by other collaborators.

---

### **12. `git reset`**  
**What it does:**  
Resets your current branch to a specific commit, effectively **undoing** commits and changes.

For example:
- `git reset --hard <commit_id>` — Resets everything (both staged and working directory changes) to a specific commit.
- `git reset --soft <commit_id>` — Resets just the commit history but keeps changes staged.

**Use case:**  
When you want to **undo** a commit or set of commits. Be careful with `--hard` as it discards changes in your working directory!

---

### **13. `git cherry-pick`**  
**What it does:**  
Applies a specific commit from another branch onto your current branch.

**Use case:**  
When you want to apply a **single commit** from a different branch (without merging the whole branch).

---

### **14. `git tag`**  
**What it does:**  
Tags a specific commit in your project’s history with a meaningful name (e.g., a version tag like `v1.0`).

**Use case:**  
You can use tags to mark release points (like versions) or milestones in your project.

---

### **15. `git clean`**  
**What it does:**  
Removes untracked files from your working directory (files that aren’t being tracked by Git).

**Use case:**  
When you have leftover files (e.g., generated files, temp files, build artifacts) that you no longer need.

---

### Recap:  
These intermediate Git commands will allow you to be much more **efficient**, **organized**, and **collaborative** in your workflow. By understanding and mastering these tools, you’ll be able to handle larger projects, work with others smoothly, and maintain a clean and manageable Git history. 

Do you want a deeper dive into any of these commands? Or maybe you have a particular situation you want to handle with Git? Let me know! 👨‍💻📚
