# Nugit Data Scientist Task

Calculating cannibalization of organic search visits when SEM advertising is purchased

## Quick Terminology
* SEM = Paid Search = sponsored ads within the same search results
* SEO = Organic Search = non-paid listings presented in the search results

## Aim
 For every visit generated through SEM advertising, what is the impact on SEO visits?

## Background
Organic Search drives substantial visits to a company's website, in the order of 20% - 40% of total traffic.

It is believed that when a company purchases SEM advertising, there may be a decrease in Organic Search visits because users that would normally navigate to the companies website via the natural listing use the paid listing instead.

Nugit wishes to get a better understanding of this relationship between results from SEM and SEO with regression analysis.

## Files and Data
To get the files, you can either clone the repository:

```sh
$ git clone git@github.com:nugit/datascientist-task.git
```

##### Provided:

* `main.py` Python file for you to get started and is the main executable file.
* `requirements.txt` file for you to list any 3rd-party modules.
* `data/sample_data_Oct.csv` sample CSV data files. Each CSV file contains the daily number of visits for SEO (organic/non-paid) and SEM (paid) in 2014. If you prefer to work with JSON, you may use my Csv-Json switcher python file on github: [cjswitch](https://github.com/alyssaq/cjswitch)
* `data/sampleoutput.json` sample output JSON file

##### Rules:
* Points marked with [Program] are to be completed in Python. Outputs are in JSON.
* Points marked with [Question] are optional and are for you to show case your statistical/machine learning knowledge. Please keep it short in dot points.
* Feel free to create more python files as necessary. Just make sure that `main.py` is the only file that gets executed.
* Feel free to use any python module(s) as necessary. Just remember to add it in `requirements.txt`
* Ensure that your .py files follow the [pep8](http://legacy.python.org/dev/peps/pep-0008/) coding style guide.

##### Submission:
* `main.py` + other `python files` - for you to show-off your logic
* `requirements.txt` - to list any 3rd-party modules
* `output.json` - your JSON results. Please see `data/sampleoutput.json` for an example submission.
* `submission.md` or `submission.html` or `submission.txt` or `submission.pdf` - for you to write your answers/comments/suggestions. We recommend using the online notebook [wakari](http://wakari.io).

Please do not write your answers in a word doc.

Submit your completed task to terry@nugit.co by providing a link to a private [bitbucket](https://bitbucket.org) or [github](https://github.com) repository or somewhere online to view the files.
Feel free to email me any questions.

## Analysis/Statistics Task

#### (A) [Linear Regression](http://en.wikipedia.org/wiki/Linear_regression)

Using the **last 26 weeks of data** in `data/sample_data_Oct.csv`:

1. [Program] Fit the data into a regression function of the form `y = mx + b`
2. [Program] Using the function, calculate the impact (the SEO value) when SEM has the *highest* number of visits
3. [Program] Using the function, calculate the impact (the SEO value) when SEM has the *median* number of visits
4. [Question] Are there other statistical methods that can show the impact of SEM visits on SEO visits?

##### Regression Function:

    y = mx + b

    where:  y is the dependent variable SEO
            x is the independent variable SEM
            m is gradient
            b is the y-intercept


##### Sample Output (these are made-up numbers. Note the decimal places):
Round  `gradient` and `yintercept` to 2 decimal places and `maxSEM` and `maxSEMimpact` are integer number of visits.


    {
        "filename": "sample_data_Oct.csv",
        "datarange": "12weeks"
        "gradient": 0.02
        "yintercept": 2004.45
        "maxSEM": 3000
        "maxSEMimpact": 1000
        "medianSEM": 1250
        "medianSEMimpact": 2200
    }

#### (B) [Model Validation](http://mathbits.com/MathBits/TISection/Statistics2/correlation.htm)

1. [Program] Calculate the Correlation Coefficient and the Coefficient of Determination
2. [Question] What does the result of the coefficients tell you about the regression function and the data?
3. [Question] Determining how well the data fits into your regression function can be done  by calculating the correlation coefficient. However, it is also known that this is not a good measure of model validation.
What other approaches could you use? Feel free to program this if you wish.

##### Sample Output (these are made-up numbers. Please round to `3dp`):

    {
        "r": 0.922,
        "rsquared": 0.850
    }

#### (C) Different date ranges

1. [Program] Perform the same analysis as in (A) and (B), but over a **26 week period**

## Bonus Points!
2. Provide tests to accompany your python functions. At nugit, we use [unittest](https://docs.python.org/2/library/unittest.html) and [nose](https://nose.readthedocs.org/en/latest/) with [codecoverage](http://www.nedbatchelder.com/code/modules/coverage.html)

3. Provide an approach to remove outliers. Feel free to program this.

4. You will notice that there is a difference in results by using 3 and 6 months of data for trend estimation. How would you go about de-trending the data to produce a more accurate picture of the relationship?

5. Chart your results using any JavaScript library 
