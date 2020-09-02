# LIZ HICKEY LIFEDIGN

# Table of Contents:


# UX
## User Stories
* As a user, I would expect the website to be secure.
* As a user, I would expect the website to be responsive on different devices.
* As a user I would expect to be able to view the courses offered.
* As a user I would expect there to be information on the business.
* As a user I would expect there to be information on the business owner.
* As a user, I would expect the website to have a contact page and links to social media.
* As a user, I would expect to be able make online payments.
* As a user, I would expect to receive details about my order.
* As a user, I would expect to see the location of the company on a map.
* As a user, I would expect there to be a booking system with a calender to pick an available day and time for a consultation.
* As a user, I would expect to be able to view and modify my order in the cart before completing it.
* As a user, I would expect to be able to view a total price of my purchases.
* As a user, I want to create my own account, so that I can save, view and edit my profile details and view my order history.
* As a user, I would expect to view reviews other customers.



## User Goals
* Website to be easy to use and visually appealing.
* The Website will ensure safe storage of user details.
* Purchase courses/services shown on the website in a safe and secure way.

# Strategy:

# Scope:

# Structure:

* Navbar

# Surface:
## Design Choice

**Typography-**

**Colours-**
Purple, green, pink and orange.
**Images-**

## Features

## Future Features

# Skeleton:
## Wireframes

# Information Architecture:
**Profile**     



| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
| Full Name       | CharField | max_length=20, blank=False |
| Number    | CharField      |  max_length=20, null=True, blank=True  |
| Address Line1 |  CharField  |   max_length=60, null=True, blank=True |
| Address Line |  CharField   |   max_length=60, null=True, blank=True  |
| Town/City |   CharField   |  max_length=50, null=True, blank=True   |
| County |  CharField  |  max_length=50, null=True, blank=True   |
| Postcode |  CharField   |  max_length=20, blank=True   |
| Country |  CountryField    |  max_length=30, blank=True   |




**User login/register**


| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
| email      | EmailField      |   OneToOneField 'User' |
| password | CharField     |    $OneToOneField 'User'|

**Contact**   



| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
| Full Name       | CharField | max_length=20, blank=False |
| email      | EmailField      |   OneToOneField 'User' |
| password | CharField     |    $OneToOneField 'User'|
| body     | CharField | max_length=50, null=True, blank=True | 


# Technologies Used:
## Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)

## Frameworks
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Django](https://www.djangoproject.com/)


## Tools
* [GitHub](https://github.com/)
* [GitPod](https://www.gitpod.io/)
* [Git](https://git-scm.com/about)
* [W3C Markup Validation](https://validator.w3.org/)
* [WSC CSS Validaion](https://jigsaw.w3.org/css-validator/)
* [Python Formatter](https://pythoniter.appspot.com/)
* [Heroku](https://dashboard.heroku.com/apps)
* [Stripe](https://stripe.com/gb)
* [Django Secret Key Generator ](https://miniwebtool.com/django-secret-key-generator/)

## Databases
* [PostgreSQL](https://www.postgresql.org/) - Production database
* [SQlite3](https://www.sqlite.org/index.html) - Development database

# Testing:

# Bugs:


# Deployment:
## **Run Locally:**

## **Deploy to Heroku:**
1. **Create** a **requirements.txt** file using the command
```
pip3 freeze > requirements.txt
```

2. **Create** a **Procfile** . Procfile must start with a capital 'P'
```
echo web: python app.py > Procfile
```

3. Push these to your Git repository.

4. Create a new app on Heroku, assign a unique name and set your region (I used Europe)

5. To start the web process, put the following command into the terminal to scale dynos:
```
heroku ps:scale web=1
```

6. From the Heroku dashboard, **click Deploy -> Deployment method -> GitHub**

7. Connect to your Github repository by adding your **repo name** and clicking the search button.

8. In the heroku dashboard for the application, click on **Settings -> Reveal Config Vars** and set the following config vars:
    * DATABASE_URL: *your_database_url*
    * SECRET_KEY: *your secret key* 
    *

9. **Deploy -> Manual Deploy** select the master branch and click **deploy branch** button.

10. Click **Open App** to view the app.

# Credits
To created the allauth social media login in i followed [Codev Youtube video](https://www.youtube.com/watch?v=-TUEM2NCuVE)




# Disclaimer
**This websit is for educational purposes only.**

