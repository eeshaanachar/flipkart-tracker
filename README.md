# Flipkart Tracker

A web crawler coupled with a front-end to track prices of products on the Flipkart website.

## Objectives

* The bot must regularly crawl the Flipkart website.
* The bot must notify whenever there's a price drop on any tracked item.
* There must be a front-end to add items to be tracked.

## Setup

* Create a `secrets.py` file with the following class (use your own email id and password) in the project's root directory. Make sure that either less secure apps or app passowrds are enabled if using gmail.

    ```py
    class Credentials:
        email_id = 'yourMailId'
        password = 'yourPassword'
    ```

* Install the packages listed in requirements.txt using pip3 as follows:

    ```bash
    pip3 install -r requirements.txt
    ```

* Run the front-end by running `app.py`
* Access the front-end at <http://localhost:5001>
* The bot `crawler.py` can be run manually or by using tools such as [cron](https://en.wikipedia.org/wiki/Cron) or [Task Scheduler](https://en.wikipedia.org/wiki/Windows_Task_Scheduler)

## Working Principle

The `app.py` provides a front-end to the project using Flask. The details entered there is stored in a sqlite databse. The `crawler.py` uses `bs4` to scrape the Flipkart website, while `smtplib` is used to send emails. The files can be hosted on a server, where Gunicorn3 can be bsed to serve the flask application. The crawler can be scheduled to run at regular intervals using cron.

## Present Scope

* There's no safeguard against DOS attacks.
* Maybe some other security risks.
