# LIZ HICKEY LIFEDIGN

LIFEDESIGN was created by Liz which is a process that helps people to overcome different life challenges. It will give you tools to be able to move forward from all kind of experiences and to find creative and innovative solutions to your problems.

# Table of Contents:
* [UX](https://github.com/SophieH93/lizHickeyLifeDesign#ux)    
    * Project Goals
    * User Stories
    * User Goals
* [Strategy](https://github.com/SophieH93/lizHickeyLifeDesign#strategy)
* [Scope](https://github.com/SophieH93/lizHickeyLifeDesign#scope)
* [Structure](https://github.com/SophieH93/lizHickeyLifeDesign#structure)
* [Surface](https://github.com/SophieH93/lizHickeyLifeDesign#surface)
    * Design Choices
        * Typography
        * Colours
        * Styling
        * Images
    * [Feautres](https://github.com/SophieH93/lizHickeyLifeDesign#features)
* [Skeleton](https://github.com/SophieH93/lizHickeyLifeDesign#skeleton)
    * Wireframes    
        * Website Layout
        * Flowchart
* [Information Architecture](https://github.com/SophieH93/lizHickeyLifeDesign#information-architecture)
    * [Database Choice](https://github.com/SophieH93/lizHickeyLifeDesign#database-choice)
    * [Data Models](https://github.com/SophieH93/lizHickeyLifeDesign#data-models)
* [Technologies Used](https://github.com/SophieH93/lizHickeyLifeDesign#technologies-used)
    * [Languages](https://github.com/SophieH93/lizHickeyLifeDesign#languages)
    * [Frameworks](https://github.com/SophieH93/lizHickeyLifeDesign#frameworks)
    * [Tools](https://github.com/SophieH93/lizHickeyLifeDesign#tools)
    * [Databases](https://github.com/SophieH93/lizHickeyLifeDesign#databases)
* [Testing](https://github.com/SophieH93/lizHickeyLifeDesign#testing)
* [Bugs](https://github.com/SophieH93/lizHickeyLifeDesign#bugs)
* [Deployment](https://github.com/SophieH93/lizHickeyLifeDesign#deployment)
    *  [Locally run the project](https://github.com/SophieH93/lizHickeyLifeDesign#run-locally)
    * [Deploying to Heroku](https://github.com/SophieH93/lizHickeyLifeDesign#deploy-to-heroku)
* [Credits](https://github.com/SophieH93/lizHickeyLifeDesign#credits)
* [Disclaimer](https://github.com/SophieH93/lizHickeyLifeDesign#disclaimer)



# UX

## Project Goals


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

The goal of this website is to provide users with a background to the Service offered by Liz with a user-friendly design.
The users have the option to book a session with Liz directly, purchase a Course available and contact Liz via a contact form or through Liz's Social Media Sites.


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
testing
## Future Features

# Skeleton:
## Wireframes

# Information Architecture:
## Database choice
During the development phase I worked with **[sqlite3](https://docs.djangoproject.com/en/3.1/ref/databases/#sqlite-notes)** database which is installed with Django.
For deployment(production), a **[PostgreSQL](https://docs.djangoproject.com/en/3.1/ref/databases/#postgresql-notes)** database is provided by Heroku as an add-on.

## Data Models
The **User Model** usied in this project is provided by Django as a part of defaults **django.contrib.auth.models**.
Click [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/) to read more information about Django’s authentication system.

### **Profile**     



| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
|  auth_user      | ForeignKey | max_length=20, blank=False |
| Full Name       | CharField | max_length=20, blank=False |
| Phone Number    | CharField      |  max_length=20, null=True, blank=True  |
| Address Line1 |  CharField  |   max_length=60, null=True, blank=True |
| Address Line |  CharField   |   max_length=60, null=True, blank=True  |
| Town/City |   CharField   |  max_length=50, null=True, blank=True   |
| County |  CharField  |  max_length=50, null=True, blank=True   |
| Postcode |  CharField   |  max_length=20, blank=True   |
| Country |  CountryField    |  max_length=30, blank=True   |




### **User login/register/contact**


| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
| email      | EmailField      |   OneToOneField 'User' |
| password | CharField     |    $OneToOneField 'User'|
| Full Name       | CharField | max_length=20, blank=False |
| email      | EmailField      |   OneToOneField 'User' |
| password | CharField     |    $OneToOneField 'User'|
| body     | CharField | max_length=50, null=True, blank=True | 

### **Course**   



| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
|  name   | CharField | max_length=254|
| description      | TextField      |   max_length=800 |
| image | ImageField     |   upload_to="static/images"|
| price     | DecimalField | max_digits=6, decimal_places=2 | 




### **Order**   
The Order model within the checkout app holds the following data for the orders.



| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
|  Related User    | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='orders' |
|  Full Name   | CharField | max_length=254|
| Phone Number    | CharField      |  max_length=20, null=True, blank=True  |
| email      | EmailField      |   OneToOneField 'User' |
| Address Line1 |  CharField  |   max_length=60, null=True, blank=True |
| Address Line |  CharField   |   max_length=60, null=True, blank=True  |
| Town/City |   CharField   |  max_length=50, null=True, blank=True   |
| Postcode |  CharField   |  max_length=20, blank=True   |
| Country |  CountryField    |  max_length=30, blank=True   |
| Date |  DateTimeField    |  auto_now_add=True |
| Total Price |  DecimalField    | max_digits=10, decimal_places=2 |


### **Order Item Detail**   
A row of Order Item Detail is created for each item existing in the shopping bag which then gets saved with the order.



| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
|  Order   | ForeignKey |Order, null=False|
|  Product  | ForeignKey | Product, null=False|
| Purchase Date |  DateTimeField    |  auto_now_add=True |
| Total Price |  DecimalField    | max_digits=10, decimal_places=2 |

### **Reviews**   




| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
|  Related User   | ForeignKey | serProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='reviews'|
|  Related Product  | ForeignKey | Product, blank=False, Null=False, related_name='reviews' |
| Review content |  TextField    |  null=False, blank=False, default=''|


### **Blog**   




| Name        | Field Type           | Validaion  |
| ------------- |:-------------:| -----:|
|  Title   | CharField | max_length=50 |
|  slug  | SlugField | max_length=250, unique_for_date='publish'|
| publish |  DateTimeField    | default=timezone.now|
| author |  ForeignKey    | User, on_delete=models.CASCADE, related_name='blog_posts'|
| content |  TextField    |  null=False, blank=False, default=''|
| image_url |  URLField    |  max_length=1024, null=True, blank=True|
| status |  CharField    |  max_length=10,  choices=options, default='draft'|


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
* [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/overview)
* [Whitenoise](https://devcenter.heroku.com/articles/django-assets)

## Databases
* [PostgreSQL](https://www.postgresql.org/) - Production database
* [SQlite3](https://www.sqlite.org/index.html) - Development database

# Testing:

## Navbar/Footer:
* **Plan-**  I will need to ensure all the links work properly so when the user clicks on one they are brought to the correct page. To ensure the navbar will collapse and the side bar shows up when the hamburger menu is clicked.

* **Implementation-** 

* **Testing-** 

* **Result-** 



## Authentication Pages:
* **Plan-**  I will need to implement a way that a user will be able to create an account and that their information is stored in a database, to log in and logout.   
This invloves checking that the users passwords match when they create a password and confirm the password and their details are correct when they go to login.


* **Implementation-** I will use Django allauth package to create Authentication for the Register and Login Pages.   
I will create several sample accounts to test that validation works by entering two different passwords in registration form,   
creating an account and try to login with correct and incorrect details.
If the customer wishes to log out of their account I will need to ensure the logout link works.

* **Testing-** I used [Temp Mail](https://temp-mail.org/en/view/1a5285c005d2a6b0baf4c354391c4d6e) to create a temporary email and used my **Gmail** account to send real emails with Django. When the user register's on the website, an email will be sent to them asking them to verify their email. Once the user verifies their email they are able to log into the website.  
When verification link is clicked in the email, user is redirected to the confirmation page, clicking "Confirm" button, success message is displayed and user is automatically logged in

![](static/images/emailConfirmation.JPG)
* **Result-**  Test passed. All the functionality works as expected, no bugs were found during the testing.




## Courses & Courses detail Page:
* **Plan-** I will need to ensure that all the following work:
    * I will need to ensure that if a user clicks on the **"View Details"** button or the image of a specific course that they are brought to the correct details of that course.  
    * The course description appers in the detail page.    
    * Login with **superuser** credentials and verify that the **Edit/Delete buttons appear** in both courses and course details pages under the image.
    * The **"Add to Cart" button** on the course details pages works.
    * The quantity range button works and calculate the total correctly.
    
* **Implementation-** I will setup the **course model** and **migrate** the table into the database, then create the view within the courses app that sends a GET request to the database and returns all the courses into the courses variable, making this available to the front end via the context in the return statement meant that I could loop through each course from the database and render the details using Djangos template language in the HTML.

* **Testing-** All courses within the database were correctly rendered to the courses.html page and course detail page.

* **Result-** Test **passed**. All the functionality works as expected, no bugs were found during the testing.

## Shopping Cart Page:
* **Plan-** I will need to ensure that all the revelevent buttons work properly e.g continue shopping or proceed to payment'.    
That if a user wishes to proceed to the checkout that they are brought to the Registration page to create an account first.   
The user is able to remove an item.


* **Implementation-** 

* **Testing-** 

* **Result-** 


## Checkout:
* **Plan-**  


* **Implementation-** 

* **Testing-** 

* **Result-** 





# Bugs:
* **The Bug:** I encountered an issue within the Blog app, where the **Blog url** was not linking to the page when I added the url to the navbar. I was getting a **NoReverseMatch** error message. I followed a Youble video to build the Blog.  
**The Fix:** With the help of the Tutor's and Students we discovered that I was to remove **app_name = 'blog'** in the blog url file, the **blog** from the models file so it just returns reverse for post_single and **namespace** from the main url file.   

* **The Bug:** I experienced a bug in the **checkout app** where I was getting the error **'no such column:checkout_orderlineitem.lineitem_total'** and a **ValidationError: '“2020-09-16 21:15:57.447790+00:00” value must be a decimal number.'**
**The Fix:** I was able to eventually find the solution on Slack. I **deleted** my **current migrations** so I was back at the initial state in the migrations folder and deleted the models file in pycache folder and ran migrations again for the checkout app which solved the error.



# Deployment:
## **Run Locally:**
* Open your prefered IDE (I used Gitpod)
* Install [Python](https://www.python.org/), [Pip](https://pip.pypa.io/en/stable/installing/) and [Git](https://git-scm.com/).
* Create a [Stripe](https://stripe.com/en-ie) account.

**Directions**:
1. Clone this repository into your IDE of your choice by pasting this command into the terminal
```
git clone https://github.com/SophieH93/lizhickeylifedesign
```
**Alternatively**, you can **save a copy** of this repository by clicking the green button **"Clone or download"** , then **"Download Zip"** button, and after extract the Zip file to your folder.

2. In your terminal **change direcrory** (cd) to the correct file location or open a terminal session in the unzip folder.

3. Enter the following commannd
```
python -m .venv venv
```
4. **Initilaize** the environment by using the following command.
```
venv\bin\activate 
```

5. **Install** all **requiremetns** by putting this command into your terminal:
```
pip3 install -r requirements.txt
```
6. **Set up environment variables:**
    * Create a env.py file in the root directory.
    * Create a .gitignore file.
    * Add .env to the .gitignore file in your project's root directory
    * Add the following environments to the eny.py file:
    ```
    import os 
    os.environ["SECRET_KEY"] = "YourSecretKey"
    os.environ["STRIPE_PUBLIC_KEY"] = "YourStripePublicKey"
    os.environ["STRIPE_SECRET_KEY"] = "YourStripeSecretKey"
    os.environ["STRIPE_WH_SECRET"] = "YourStripeWHKey"
    os.environ["GOOGLE_MAP_KEY"] = "YourGoogleMapKey"
    os.environ["DEVELOPMENT"] = "True"
    os.environ["DATABASE_URL"] = "YourDatabaseURL"
    os.environ["EMAIL_HOST_PASS"] = "EmailHostPassword"
    os.environ["EMAIL_HOST_USER"] = "Youremail"
    ```

  7. **Creat** your **database**.
        ```
        python3 manage.py makemigrations
        python3 manage.py migrate

        ```
8. **Load** the data **fixtures** (courses)
    ```
    python3 manage.py loaddata courses

    ```
9. 8: Create a **superuser** for the project using the terminal, enter the following command.
    ```
    python3 manage.py createsuperuser

    ```

10. The app can now be ran locally using the following command.

    ```
    python3 manage.py runserver

    ```

11. To access the **admin panel**, you can add the /admin path at the end of the url link and login using your superuser credentials.













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
To create a Blog Model i followed [Django Project - Simple Blog App] (https://www.youtube.com/watch?v=AF4ji8bb1M8&ab_channel=veryacademy)




# Disclaimer
**This websit is for educational purposes only.**

