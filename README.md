# PythonSeleniumBDD2024

A Behavior-driven development testing framework based on Python, Selenium, Pytest

* Follow [link](https://www.youtube.com/watch?v=t8T5LWIO24I&t=1s) for practice

* Install Gherkin plugin for Pycharm

* Running BDD tests is very easy. Run command `behave features` to execute all tests/feature-files
  OR `behave features/login.feature` to execute specific tests/feature-file.

* For tag-based runs, execute command `behave --tags=smoke-testing`

* By default, behave does not support running tests in parallel. However, to cross this limitation, we can make use
  of `behavex` plugin. Package has already been added in requirements.txt file.

```
behavex features --parallel-processes 4 --output-folder Reports

Runs 4 tests in parallel and generates a html report in `Reports` directory
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* Go through
  this [video](https://himanshu-sheth.medium.com/selenium-python-tutorial-getting-started-with-bdd-in-behave-7089e90ac91f)
  at the end

* For passing browser name and URL
  through [commandline](https://pravin-alhat7.medium.com/selenium-python-launch-any-browser-and-url-via-the-command-line-arguments-fb5585dc1d77) 