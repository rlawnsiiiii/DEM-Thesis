# Git

Remember the last time you worked on a project, of which the submitted version was called `Project_FINAL2-new-thisTimeForReal.cpp`? There is an easier way to track versions and revert to previous states at any time! This is especially important when collaborating on a larger project.

In the Git version control system, every state is called a **commit**, which describes the changes from the previous version. Every file in the project, together with the history, is stored in a **repository** (a directory). You can manage Git repositories either from your IDE, or from the command line (here examples in Linux).

Before you are able to create Git commits, you need to tell Git who you are. Run in your terminal:

```shell
git config --global user.name "My Name"
git config --global user.email "my.name@tum.de"
```
You can see and edit your configuration with `git config --global -e`.

To start a repository in the current directory, use `git init`. Afterwards, the usual development cycle is:

- Check that you don't have any changed files: `git status`.
- Get the latest changes from the remote repository: `git pull` or `git pull origin master`.
- Work on your project until you have a small, self-contained improvement (that compiles).
- See your changed files: `git status` or `git diff`.
- Collect the files you want to save with `git add file1.cpp file2.cpp`.
- Create a new saved state: `git commit -m "Add a short and descriptive message"`. The same `git commit` with a flag will start your editor, with which you can write a longer message body in a second paragraph. It is common in this to also refer to **issues**.

When working on different todos in your code (or with different people on the same code), it makes a lot of sense to work on different **branches**, which start from a common base, but try to implement different features of a project, often in the same files.
The main branch has usually the name **master** and one can see the name of the current branch
using `git branch`. To create a new branch, use `git checkout -b my-branch-name`.
To change to an existing branch (or any other previous state), use `git checkout my-branch-name`.

To merge another branch into your branch, use `git merge other-branch-name`.
If both branches changed the same line of a file, you will get a **merge conflict**.
Open the file in your editor, adapt the affected line and then use the usual add-commit procedure.

### Example: keeping versions of your first C++ program locally

Watch this recording to learn how to make you first local commits:

[![asciicast](https://asciinema.org/a/8Ff5RDw7waqtSZExA7qKYYRL3.png)](https://asciinema.org/a/8Ff5RDw7waqtSZExA7qKYYRL3)

### Machine-readable information in commit messages

We often use commit messages to refer to other people, discussions, or even give messages to a continuous integration system.

In pair programming, it is good practice to credit our co-authors. We can just write:

```
co-authored-by: Linus Torvalds <torvalds@example.com>
```

somewhere in our commit message. For multiple co-authors, add multiple lines. GitLab/GitHub parse this information and show all involved authors next to the commit.

Similarly, when we want our commit to link to issues of the same project on GitLab/GitHub, we can just mention their numbers. Special keywords can also mark these issues as complete, and close them when the commit is merged to the main branch. For example: `closes #123`.

When we are pushing trivial commits and we don't want that they trigger a CI pipeline, we can just write `[ci-skip]`.

## Working with remotes (GitLab)

On the [GitLab](https://gitlab.lrz.de/) server of LRZ you can [create new projects](https://docs.gitlab.com/ee/gitlab-basics/create-project.html). To clone your new project, or another remote repository, use `git clone <URL>`. (hint: use the `https` link in the beginning. If you [add your ssh key](https://docs.gitlab.com/ee/gitlab-basics/create-your-ssh-keys.html), you can use the `ssh` link and avoid typing your password)

To learn if there are any new changes in the remote repository, use [git fetch](https://www.git-scm.com/docs/git-fetch). To merge any new changes from the remote repository, use [git pull](https://www.git-scm.com/docs/git-pull).

To publish your changes to the remote repository: `git push` or `git push origin master`. If, in the meantime, someone else has published changes, your **push** may be rejected. In that case, a **rebase** usually helps: `git pull --rebase` and then [git push](https://www.git-scm.com/docs/git-push). This is a potentially dangerous operation (as it rewrites the history), so read first about it.

## Troubleshooting

### Oh, no! Something broke!

Git is known for having very helpful error messages, with a typically useful suggestion at the end of each error message. Whenever something happens, a good first reaction would be to read the complete error message, or run `git status`. Git will most probably tell you how to get out of that trouble.

When following fractions of advice you find online, try to understand what you are trying to do before taking action (general principle of life). Be particularly careful with anything that overwrites history (e.g., rebasing or force-pushing).

### The authenticity of host can't be established

```
The authenticity of host <hostname and address> can't be established.
ED25519 key fingerprint is <key hash>.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

This is expected every time you connect to a new server. If you trust the connection and server (typically yes), just type `yes` to continue.

### Could not read from remote repository

```
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

This typically means one of the following:

1. You are trying to clone using an SSH connection (e.g., `git clone git@gitlab.lrz.de:namespace/repository.git`), but you have not added your SSH key to GitLab / GitHub or similar. You can either [generate and add an SSH key](https://docs.gitlab.com/ee/user/ssh.html) (which helps to not always have to write your password) or you can clone using an HTTPS connection (e.g., `git clone https://gitlab.lrz.de/namespace/repository.git`). You can get this link from the "Clone" button on the respective web tool.
2. You are trying to clone a private repository you do not have access to.

Note that, in case you use two-factor authentication (you should, if you are involved in some production project), you have to use an SSH connection (HTTPS gets significantly complicated).

### You have divergent branches and need to specify how to reconcile them

```
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint: 
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint: 
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

This typically means that you are trying to pull a branch on which both you and the remote have added new commits. Usually, instead of merging, you can do a rebase:

```shell
git pull --rebase
```

This will fetch the latest changes from the remote branch and apply your changes on top, as if the new remote changes were already there when you started editing. Note that this operation is difficult to undo, since it rewrites the history, so you should only rebase if you know why you need that.

Advice: Do not change your Git configuration unless you know what you are doing and why.

### There is no tracking information for the current branch

```
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> main
```

If you create a branch locally and then try to push it to or pull it from a remote, Git does not assume that you want to overwrite a remote branch with the same name. For this reason, the first time we need to specify which remote branch we mean. For example, when pushing:

```shell
git push --set-upstream origin main
```

You could even make this the default behavior for all branches and repositories (`--global`):

```shell
git config --global --bool push.autoSetupRemote true
```

### Refusing to merge unrelated histories

```
fatal: refusing to merge histories
```

It looks like you initialized the repository both locally and in your remote (e.g., GitLab) and have worked on both repositories. These two repositories have histories that are unrelated: They don't have a common starting point.

You are in a complicated situation, [StackOverflow might help](https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase), or (if trivial), start again from scratch. The easiest is to initialize first on GitLab, clone the repository, and start committing to that.

## Resources

- [Git documentaton](https://git-scm.com/book/en/v2)
- [GitLab documentation](https://docs.gitlab.com/)
- [The Missing Semester: Git](https://missing.csail.mit.edu/2020/version-control/)
- [GIT PURR! Git Commands Explained with Cats!](https://girliemac.com/blog/2017/12/26/git-purr/)
- [More learning resources for Git](https://try.github.io/)
- [Demo of the typical Git workflow](https://www.in.tum.de/fileadmin/w00bws/i05/FG_uploads/Gratl_WorkshopGIT.pdf)
- [Interactive tutorial mainly focused on branching](https://learngitbranching.js.org/). For slightly advanced users.
- [Codeacademy tutorial](https://www.codecademy.com/learn/learn-git). This covers all the basics but requires registration.
- [Git Command Explorer](https://gitexplorer.com/) (Seems to be down but the [backup on WayBackMachine](https://web.archive.org/web/20230503062141/https://gitexplorer.com/) still works)
