# Overview

Pages were taken from a pdf and copied, stripped of newlines, and dumped a paragraph at a time into markdown.

The shell script displayDemon handles displaying the page, prompting the reader for notes, and saving those notes to a file after a confirmation prompt. 

The shell script displayAngel deploys the Demons to move the read write operations. At present this only involves an iteration process by page index. More nuanced ways of shell scripting can be employed. In no way are Angel scripts to touch read write operations related to the texts in question. If there is any corruption of files, it must be via the work of a Demon script.

 The notes directory is initialized as empty and is populated as the user interacts with the text through the form of note-taking. As such, the state of the notes directory is designed to give a vauge and fuzzy view into user attention. It is the outgoing edge which maps the entirety of the domain that the user leaves traces within.
