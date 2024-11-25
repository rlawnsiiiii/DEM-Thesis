# Student Starter Clues SCCS (SSC SCCS)

* Hate reading markdown files? Use [pandoc](https://pandoc.org) to convert it to pdf / html / you name it: `pandoc TipsTricksTodos.md -o TipsTricksTodos.html`
* All points listed here are general guidelines. Always consult with your advisor for details and their preferences!

--------------------------------------------------------------------------------

## Organizational Matters

* Most projects can start on the 15th of any month. Check the links below if this applies to your project.
* Duration of the project:
    * Bachelor's Thesis (IN, GE): 4 months
    * Bachelor's Thesis (IS): 5 months
    * Master's Thesis: 6 months
    * IDP: no fixed deadline
    * Guided Research: 6 months
* Regular meetings
    * Usually weekly but clarify this with your advisor.
    * Content: talk about the progress since the last meeting, problems encountered and how to tackle them, action plan until the next meeting.
* Ask ask ask!
    * No matter what you heard in any course, asking questions is highly encouraged and most of the time necessary! Discussing things you do not understand is an essential part of every project.
    * If you are stuck anywhere and neither the literature, documentation, nor internet could help you, do not wait for the next meeting but write an email to your advisor.

### Paperwork 

* Forms need to be filled, signed, and handed to the advisor. The advisor will then collect the signature of the professor (supervisor) and forward it to the responsible TUM office.
    * CORONA NOTE: currently it is sufficient to send the advisor a scan / photo of the filled and signed forms.
* Forms should be submitted to the advisor at least ~10 days before the planned start date.
* [Supervision form](https://gitlab.lrz.de/tum-i05/public/supervisionform)
    * Mostly about data protection (GDPR)
    * Also contains some useful guidelines so read it completely.
* Registration form for TUM offices
    * Supervisor = Prof.
    * Advisor = PhD Candidate
    * [Bachelor's or Master's Thesis](https://www.cit.tum.de/en/cit/studies/students/thesis-completing-your-studies/informatics/)
    * [Guided Research](https://www.cit.tum.de/en/cit/studies/degree-programs/master-informatics/)
    * [Interdisciplinary Project](https://www.cit.tum.de/en/cit/studies/degree-programs/master-informatics/interdisciplinary-project/)
* Title
    * Usually it is your responsibility to find a suitable title together with your advisor.
    * Good approach: Make a collection of relevant buzz words and form them into a cool sentence.
    * Don't be overly specific: If your title says "Solving Problem P with Algorithm A" you have to do it this way. Maybe you would like more leeway.
    * Don't be too general: A title like "Writing Code" is just boring.
    * In the end you have to be happy with the title since it is general practice to list it on your CV.
    * If the project diverges away from the title it is possible to change it. If you feel you need this discuss this with your advisor as early as possible and not on the day of submission.
* (IDP only): 1-2 page project description with milestones. Typically written by the advisor with input from the student.
* (Guided Research only): 1-2 page abstract. Typically written by the advisor with input from the student.

--------------------------------------------------------------------------------

## Coding Work

* Use version control
    * If your work is part of an existing project talk about the workflow with your advisor. Usually, you work on your branch that should be merged regularly with the master to avoid a mega merge at the end of the project.
    * If you work on an independent project create a (public) repository on e.g. [GitHub](https://github.com) or [LRZ GitLab](https://gitlab.lrz.de) and give your advisor the appropriate access rights.
    * Be aware not to put anything that is protected intellectual property on a public repository.
* Cluster access: Depending on your project you might require access to highly parallel compute resources. Talk to your advisor about this. Possible Clusters and how to get access:
    * [Linux Cluster](https://doku.lrz.de/display/PUBLIC/Linux+Cluster)
        * Access: Your advisor can ask our chair admins directly. They need your LRZ ID (pattern: ga00az), nationality, and email address.
        * Read the (extensive and good) documentation by LRZ!
        * Don't store huge piles of data (>20GB) in your $HOME. Use $SCRATCH instead.
        * Don't run compute jobs on the login nodes. Use sbatch / salloc instead.
    * [LRZ GPU Cloud](https://doku.lrz.de/display/PUBLIC/Compute+Cloud)

--------------------------------------------------------------------------------

## Thesis

* Your main objective is to write the document. All software development, research, literature review, and so on are additional (but very necessary!) steps toward that objective. Things like cleaning up your code or extensive documentation are still possible after the deadline. For you, everything has to be focused on the document, because this has the highest impact on the grade.
* It is a good idea to start the thesis document at the beginning of your project to collect plans, notes, sources, figures, and plots.
* When you start the main writing phase (usually 1-2 months before submission), set up a schedule for when you want to finish which part of the thesis and discuss it with your advisor. This helps you to focus on the important parts and to keep track of where you are time-wise.
* Use version control (e.g. git) or an online service like [Overleaf](https://www.overleaf.com) or [TUM Share LaTeX](https://latex.tum.de).
* There is no official requirement on the number of pages. Be concise and cover everything in sensible depth.
* As soon as you have a section finished (read: all content you want to cover is in there but details might still change) send it to your advisor for feedback about style, depth, etc.
* Submission
    * Give a physical copy to the Infopoint.
    * Ask your advisor if they require an additional physical copy for the chair. Most of the time the PDF is fine.
    * Check the formal and style requirements of your study program (see links above for registration forms). It is highly recommended to use a printing service like [printy](https://www.printy.de/de) who know about these requirements (e.g. name and title at the back of the binder).

### Templates

* There is no definitive official template for informatics. Choose the one you like best or create your own but make sure it complies with the current [requirements of the department](https://www.cit.tum.de/en/cit/studies/students/thesis-completing-your-studies/informatics/)! Violating these might result in your thesis being rejected.
* Have a look at multiple templates, they usually include some good LaTeX tips and tricks.
* See [ThesisTemplate folder](../ThesisTemplate).
* [TUM Templates on Share LaTeX](https://latex.tum.de/templates/tum-templates)
* [Inofficial template](https://github.com/fwalch/tum-thesis-latex)
* [CSE Thesis template](https://github.com/waltsims/TUM_Thesis_Template_CSE)

### Content

* Language
    * Use the present tense.
    * It is highly recommended to write in English.
    * Use language / grammar checker! [grammarly](https://www.grammarly.com) understands LaTeX and has neat browser extensions.
    * The [TUM language center](https://www.sprachenzentrum.tum.de/sprachen/englisch/english-writing-center) offers thesis writing workshops and advisory services.
* Literature and citations
    * Follow the [TUM Student Code of Conduct](https://www.cit.tum.de/en/cit/studies/students/thesis-completing-your-studies/informatics/).
    * Find relevant papers through search engines like [Google Scholar](https://scholar.google.com), [Connected Papers](https://www.connectedpapers.com), or [iris](https://the.iris.ai).
    * Get BibTeX snippets through Google Scholar: Klick on the Cite button under the paper (Quotes Symbol) -> BibTeX. The information in the snippets is not always completely correct (e.g. dates or journal names) so always check them manually.
* General structure (some points might not always apply so check with your advisor):
    * Abstract: Brief introduction of the problem, your approach, and the findings.
    * Introduction: Relevance of the topic and motivation.
    * Theoretical background: All theory necessary to understand what you did.
    * Technical background: Explanation of a software, library, or framework you build upon.
    * Related work: Summary of other projects similar to yours, their findings, and what you do differently.
    * Implementation: Description of what you actually created.
    * Results: Description of the experiments you conducted, their results, and your interpretation of these.
    * Conclusion: Wrap up of everything above and educated suggestions on how to extend your work.
* Build your thesis to have a comprehensive and logical structure following one central guiding thought.
* Check the figures section below.

--------------------------------------------------------------------------------

## Presentation / Colloquium

* Drop by at the [SCCS Colloquium](https://www.cs.cit.tum.de/en/sccs/news/sccs-colloquium/). It is open for everyone and a nice way to get a feeling of how a talk might look. Ask your advisor if there are upcoming talks related to your topic and look through the list of announced talks.
* Most student projects (BA / MA thesis, IDP) require at least a final talk that may be part of the grade.

### Templates

* Again there is no official template for student presentations. Here you are completely free to choose a style you like.
* There exist [official TUM presentation templates](https://portal.mytum.de/corporatedesign/index_html/vorlagen/index_praesentationen) but using them for the Colloquium is optional.

### Content

* Language
    * It is highly recommended to present in English.
    * In principle German is possible but check with your advisor.
* Start with a motivation slide containing images, videos, or a practical application that introduce your problem statement.
* Build your talk to have a comprehensive and logical structure following one central guiding thought. This does not necessary have to be tha same as the guiding thought of the thesis.
* Check the colloquium page for the length of your talk.
* Don't include a table of content. Your talk is too short for that.
* You cannot present everything that you wrote in your thesis. Focus on the main points of the results sections (and maybe implementation if applicable). Only talk about the absolutely necessary background. Think of the talk as a "too long; didn't read" (TL;DR) of the thesis.
* Plan with 1-2 Minutes per slide. A 20-minute talk should have 10-15 slides.
* Aim at having a figure on every slide, even if it is just the logo of the framework you present. This makes the slides more lively and visually interesting.
* The slides should be understandable without the talk. This means every slide needs to have a minimum amount of text / bullet points to understand the core messages. The talk itself can (and probably should) add to that, so do not just read what is written on the slides.
* Avoid continuous text and avoid too much text. Use bullet points.
* Prefer visual explanations (figures) over formulas.
* Interact with your slides, especially figures. Use pointing devices (Laserpointer > Stick > Finger; Online: Mouse) to highlight the details you are talking about.
* Check the figures section below.
* Good (= clear, descriptive) figures are even more important than in the thesis since the audience cannot consume them at their own pace but must follow the pace of the talk otherwise you lose everyone.
* Close with a summary slide that lists your main contributions and/or findings.
* Bonus points for making the slides color-blind friendly.
* Put references directly on the slides where you are using them, or at least use a citation style that's more descriptive than just numbers.

--------------------------------------------------------------------------------

## Figures

This is relevant for all figures, plots, schematics, etc you produce for any written document or talk throughout the project.

* Every feature of a plot or figure should be labeled or explained somewhere. This includes all lines, points, axis, colors, etc.
* Every plot should have a purpose, meaning a message / finding that you want to convey or prove. This message has to be explicitly written somewhere around the plot (title / caption / on slides a prominent bullet point next to it).
* Showing a plain table of values is (almost) never a good idea. Think of a way to create a plot that highlights what you want to show with the data. If you have trouble finding a good representation discuss it with your advisor. If the actual values are still of some interest you can also put the table in an appendix.
* Be wary about showing source / pseudo code since it is basically a wall of plain text. Could you instead create a figure that represents what is happening? If you must show the code (sometimes it actually is necessary) invest effort in code highlighting and additional highlighting (draw boxes or colors) of the essential parts.
