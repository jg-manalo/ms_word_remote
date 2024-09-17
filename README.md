# Opening Microsoft Word through the use of links in a webpage #

_Backend: Flask web framework (Python)_

_Frontend: HTML, CSS_

## Thought Process ##

> - When the user clicks the link, it sends a route that the backend would read it
> - Once it is known what route we are on, there is a corresponding block of code of the program would do
> - Inside the block of code, by utilizing the operating system's shell command (Windows), we invoke the executable file of the application to its installation path
> - The invokation of the shell command is wrapped inside the  Python function
