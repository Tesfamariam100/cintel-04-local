# Project: Interactive Reactive App Development
## Objectives:
* Follow the typical workflow of a real interactive development project.
* Create a repository on GitHub, clone it locally, and set up a virtual environment.
* Design and implement interactive apps focusing on Python development.
* Utilize Shiny to build client-side web apps without requiring web development skills.
* Keep track of progress and notes in README.md.

## Before Beginning:
* Complete orientation and installations as per CC4.1 to CC4.5.
* Ensure your project repository contains:
* README.md
* .gitignore
* requirements.txt
* penguins/app.py

## Workflow:
### Verify App Runs:
* Run the Shiny app locally using:
`shiny run --reload --launch-browser penguins/app.py`

### Build Client-Side App:

* Export the app to the docs folder:
`shiny static-assets remove`
`shinylive export penguins docs`

* Serve the app locally:
`py -m http.server --directory docs --bind localhost 8008`
* Test the app at http://localhost:8008.

### Git Add / Commit / Push to GitHub:
* Add, commit, and push changes:

`git add .`
`git commit -m "Your commit message"`
`git push -u origin main`

### Publish GitHub Pages for the Repo:
* Configure GitHub Pages in repository settings:
* Select main branch as the source.
* Change publication source to docs.
* Update repository "About" section with the hosted web app link.

### Post-Development Tasks:
* Modify the browser tab title in docs/index.html.
* Optionally, add a custom favicon:
* Generate favicon using https://favicon.io/.
* Paste favicon.ico into the docs folder.
* Update docs/index.html with favicon link.

## Conclusion:
* Upon completion, you'll have a functional penguin dashboard locally and hosted online. 