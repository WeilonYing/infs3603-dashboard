# infs3603-dashboard

Putting my SAS VA dashboard report for INFS3603 here for easier version control.

Pls don't plagiarise.

Report download link: [Download](https://github.com/WeilonYing/infs3603-dashboard/raw/master/printReport.pdf)

# User Guide
## Overview
The dashboard/report is designed to give an operational and strategic overview of a
hypothetical company's car insurance sales. Each tab in the dashboard has an array of
filters on the top bar to allow for drilling down into specific customer demographics
and subsets.

When a filter is set, every graph in the tab is updated to only consider the subset
of customers that match the criteria set in the filter. Each tab has the following
filters:
* Age
* Job occupation
* Education level
* Month customer was last contacted (LastContactMonthNum)
* Call outcome (failure, other or success)

## Success Rate
The Success Rate tab displays the status of the company's KPI
at a glance. We have determined that our main KPI, or "North Star Metric" to be
the percentage of customer contacts that result in a successful outcome
(i.e. car insurance was able to be sold/renewed).
* Success Rate - Gauge for showing how well the company is performing in selling
  car insurance overall.
* Success Outcome Amount by Month - Bar chart for showing the raw numbers of
  successful insurance sales, grouped by new sale (HasCarInsurance = No)
  and renewal (HasCarInsurance = Yes)

This tab an extra filter "HasCarInsurance" to filter success rate by renewal
or new sale.

![success rate tab](https://raw.githubusercontent.com/WeilonYing/infs3603-dashboard/master/screenshots/tab1-successrate.PNG)

## Call Outcomes
The Call Outcomes tab shows the number of calls and the proportion of outcomes
for each month.
* Outcomes grouped by Month - Shows the percentage of failure, other and success
  outcomes from calls in a particular month.
* Call Frequency each Month grouped by Month - Shows the raw number of calls made
  each month, grouped by outcome.

![call outcomes tab](https://raw.githubusercontent.com/WeilonYing/infs3603-dashboard/master/screenshots/tab2-calloutcomes.PNG)

## Sales Operations
The Sales Operations shows customer calling statistics. It is used to track how
efficiency of a hypothetical sales team at making car insurance sales.
* Average Call Duration over time grouped by Outcome - Pretty self explanatory.
  Shows the average call duration for each day, with one line for each possible
  outcome.
* Number of calls per day grouped by Outcome - Shows how many calls were made each
  day, with one line for each possible outcome.

![sales operations](https://raw.githubusercontent.com/WeilonYing/infs3603-dashboard/master/screenshots/tab3-salesoperations.PNG)

## Customer Demographics
The Customer Demographics tab functions as a quick overview of the nature and
background of our customers. It should be used as a tool for creating marketing
strategies for future sales.
* Customer Job Occupation - Shows the amount of customers in each job occupation
* Method of Communication to Customers - Self explanatory
* Customers' Marital Status - Self explanatory
* Relationship with Customers - Shows the proportion of customers that have
  already purchased an insurance policy with the company, and which policy/ies
  they have purchased.

![customer demographics](https://raw.githubusercontent.com/WeilonYing/infs3603-dashboard/master/screenshots/tab4-customerdemographics.PNG)
