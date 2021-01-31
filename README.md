<div align="center">
  <img src="https://github.com/pengols/jjmason/blob/master/documentation/images/screens.png">
<hr>

**A site where users can view, purchase and follow the inspiration and artistic work of JJ Mason.**

[View the live site](https://jjmason.herokuapp.com/)

</div>

---

## <u>Table of contents</u>

**<details><summary> User Experience (UX)</summary>**
  - [Purpose](#purpose)
  - [Design](#design)
  - [User stories](#user-stories)
  - [Wireframes](#wireframes)
</details>

**<details><summary> Features</summary>**
  - [Current Features](#current-features)
  - [Future Features](#future-features)
</details>

**<details><summary> Technologies</summary>**
  - [Languages](#languages)
  - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
</details>

**<details><summary> Deployment</summary>**
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
  - [Deploying to Heroku](#deploying-to-heroku)
</details>

**<details><summary> Testing</summary>**
  - [Tools](#tools)
  - [Testing User Stories](#testing-user-stories)
  - [Further Testing](#further-testing)
  - [Known Bugs and Resolutions if Applicable](#known-bugs-and-resolutions-if-applicable)
</details>

**<details><summary> Credits</summary>**
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
</details>

<hr>

# **User Experience (UX)**

### **<u>Purpose</u>**

Using HTML, CSS, JavaScript, Python & Django, the site is designed to provide a platform to both showcase and make available to purchase, the various types of artwork by Jeremy J Mason. Non-registered users are able to browse products and make purchases using Stripe.  Registered users are able to store delivery information and also browse and make purchases.  Site owners/Administrators are able to manage orders, users, products and blog posts.

To make a test purchase, please use credit card number 4242 4242 4242 4242.

### **<u>Design</u>**

**Colour scheme**

<div align="center">
  <img src="https://github.com/pengols/jjmason/blob/master/documentation/images/color.PNG"></div>

  The site is purposefully designed with a predominantly black and white theme.  This is due to the nature of the content, which is artwork and I wanted that to be the primary focus for the reader. There are minimal flashes of color to help a user navigate the site.  Primary action buttons are a deep purple (#731CED), secondary buttons are a lighter purple (#FF5CD1).

  The home page adds a third variant of purple for the action boxes (#CB6CEC).

  Form borders are higlighted in grey (#7c7c7c) rather than black to make them softer, and delete buttons are red (#fab3b) to ensure they stand out and the user can quickly understand their function.

**Typography**

The site uses two fonts, both available from [Google Fonts](https://fonts.google.com/).  Headings and titles use IM Fell English.  Much of Jeremy's art is inspired by the work of Oscar Wilde and this font evokes the feeling of printed works from the 19th Century.  For larger pieces of text such as product descriptions Opens Sans is used for it's legibility.  Sans Serif is used as a fallback font, in case for any reason the fonts aren't being imported into the site correctly.

### **<u>User Stories</u>**

Non-registered and registered users:
- view products so I can select items to purchase
- sort products by category, price (ascending and descending) and sort products alphabetically (ascending and descending)
- search for specific product using keywords
- view individual product details to easily see price, description and image, product rating, and availability
- view site owners blog
- register for an account or login 
- view current items in my shopping cart
- complete a purchase and receive a confirmation email


Registered users 
- ability to login/logout
- ability to reset a forgotten password
- view previous purchase history

Site owner/Administrator
- login to administration panel
- within the administration panel be able to manage site users, products orders and blog posts
- add, edit and remove existing products for sale
- add, edit and remove blog posts


### **<u>Wireframes</u>**

- [Desktop home and product view](https://github.com/pengols/jjmason/blob/master/documentation/wireframes/dt.jpg)
- [Mobile home & blog & tablet product view](https://github.com/pengols/jjmason/blob/master/documentation/wireframes/tabmob.jpg)

## **Features**

### **Current Features**

- Developed with a 'mobile-first' ethos, the site is responsive on all device sizes.  Visitors to the site should experience no difference in functionality of the site regardless of screen viewing size. 
- Using the 3rd party package [Allauth](https://django-allauth.readthedocs.io/en/latest/) users are able to securely register, verify their account with a link provided by email and subsequently login to the site to be able to record their purchase history and peronalise their delivery details for future purchases.  Registered users are also able to perform a forgotton password request form the sign in page.
- The site hosts a blog that can be updated by site Admins. 

### **Future Features**

- Forum so vistors and members can discuss artwork, blog posts, upcoming events and the subjects of Jeremy's inspiration.
- Product rating for logged in users who have made a purchase.
- The ability to add a personalised message from Jeremy on any purchases made.

## **Technologies Used**

#### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

#### Frameworks Libraries and Programs Used


- [Google Fonts:](https://fonts.google.com/)
    - Google fonts are used to import the 'IM Fell English' and 'Open Sans' fonts into the style.css file which is used on all pages throughout the project.
- [jQuery:](https://jquery.com/)
    - jQuery is used to perform a number of actions within the site.
- [Git](https://git-scm.com/)
    - Git is used for version control by utilising the Gitpod terminal to commit to Git and push to GitHub.
- [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
- [Gitpod:](https://gitpod.io/)
    - Gitpod was used as the IDE for creating the project.
- [Heroku:](https://www.heroku.com/)
    - Heroku is used to host the website.
- [Bootstrap:](https://www.getbootstrap.com/)
    - Bootstrap is used as the framework to ensure a responsive mobile-first website.
- [Django:](https://www.djangoproject.com/)
    - Django is a high-level Python Web framework.
- [Stripe:](https://www.stripe.com/)
    - Stripe is used to handle Credit Card transactions.

## Schema

## **Deployment**

### Forking the GitHub Repository

Forking the GitHub Repository allows a copy of the original repository in GitHub to be created.  The forked repository can be viewed or be changed without affecting the original repository, by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/pengols/#)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/pengols/#)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `pengols`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

### Deploying to Heroku

An Amazon [S3 bucket](https://aws.amazon.com/s3/) account is required as a repository for STATIC and MEDIA files for this project.

1.  Browse to [Heroku](https://www.heroku.com/).
2.  Login or create an account.
3.  Click on the **New** button.
4.  Click - **Create New App**.
5.  Create a unique app name.
6.  Choose closest server location.
7.  Once created, navigate to the resources button and select the Heroku Postgres to attach a Postgres database.
8.  Install the following libraries using your IDE terminal:
    [Gunicorn](https://gunicorn.org/) a (WSGI HTTP Server), [dj-database-url](https://pypi.org/project/dj-database-url/) PostgreSQL connector and [Psycopg](https://www.psycopg.org/) PostgreSQL adapter

        ```
        $ pip install Gunicorn, dj-database, Psycopg
        ```

9.  To migrate to the postgres db. Add `import dj-database-url` in `settings.py`.
10. Then comment out the default database configuration and add:

    ```
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('< Put your DATABASE_URL here >'))
    }
    ```

    > In Heroku, Click into the settings tab and navigate to **'reveal config vars'**.
    > Here you will find the _'DATABASE_URL'_.

11. Make the required database migrations:
    ```
    $ python manage.py migrate
    ``` 
12. Create a superuser using your IDE terminal:
    ```
    $ python manage.py createsuperuser
    ```

12. After migrations are complete, change database configuration in settings.py to:

    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```

    > This change will ensure SQLite3 is used in development and Postgres is used in production.

13. Enter in all your AWS variables as well as all your `.env` variables into Heroku's Config Vars.

    | Key                   |      Value      |
    | --------------------- | :-------------: |
    | AWS_SECRET_ACCESS_KEY | < Your Values > |
    | AWS_ACCESS_KEY_ID     | < Your Values > |
    | USE_AWS               |      True       |

    > These variables are retrieved from your AWS S3 account.

14. In your IDE terminal. Navigate to your directory.
    Login to Heroku using the Terminal

    ```
    $ heroku login -i
    ```

15. Create a `Procfile`.

    ```
    $ echo web: gunicorn jjmason.wsgi:application > Procfile
    ```

16. Freeze your requirements

    ```
    $ pip freeze > requirements.txt
    ```

17. Add all files to GitHub staging

    ```
    $ git add .
    ```

18. Commit changes to GitHub

    ```
    $ git commit -m "Your message"
    ```

19. In `settings.py` configure AWS storage settings

     ```
     if 'USE_AWS' in os.environ:
         AWS_STORAGE_BUCKET_NAME = < Your Bucket Name >
         AWS_S3_REGION_NAME = < Your server location >
         AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
         AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
         AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
         AWS_DEFAULT_ACL = None

       # Static and media files

         STATICFILES_STORAGE = 'custom_storages.StaticStorage'
         STATICFILES_LOCATION = 'static'
         DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
         MEDIAFILES_LOCATION = 'media'
         STATIC_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
         MEDIA_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
      ```

    >Specifies the hosts that the app can run on

      ```
        ALLOWED_HOSTS = ['127.0.0.1', 'jjmason.herokuapp.com']
      ```

20. Push all changes to Heroku

    ```
    $ git push heroku master
    ```

21. This should deploy the app to Heroku successfully.  To view the app, within Heroku, click the Open App button.

## **Testing**

### Tools

The W3C Markup Validator and W3C CSS Validator Services were used to validate the HTML and CSS of the project. 

- [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

- Errors were found with HTML checker

    - Bad value 200px for attribute width on element img: Expected a digit but saw p instead. This is ignored as the images in question need the width defined and no issues were detected.
    - End tag for body seen, but there were unclosed elements.  This is ignored as I believe this to be a false positive.  No errors were highlighted in GitPod and the page renders as intended.  This is possibly caused by the fixed footer div that was implemented.  A manual search of the fully rendered home page revealed no issues.
    - Unclosed element div. Again, the same result as above.  The pages render correctly and is possibly related to the fix applied for fixed footer.

- Errors were found with CSS checker

    - Same color for background-color and border-right-color.  This is not fixed as this is a deliberate choice for button design.
    - 	-webkit-radial-gradient(circle at 30% 107%,#fdf497 0%,#fdf497 5%,#fd5949 45%,#d6249f 60%,#285AEB 90%) is an unknown vendor extension.  This is not fixed as the colored Instagram logo renders as desired.
    - -webkit-background-clip is an unknown vendor extension.  The same as bove.  The logo renders correctly so no fix implemented.

The Esprima JavaScript Syntax Validator & JSHint were used to validate the JavaScript of the project. No errors were found.

- [Esprima JavaScript Syntax Validator](https://esprima.org/demo/validate.html)
- [JSHint](https://jshint.com/)

The PEP8 Online & ExtendsClass Python Syntax Checker were used to validate the Python of the project. No errors were found.

- [ExtendsClass Python Syntax Checker](https://extendsclass.com/python-tester.html)
- [PEP8 online](http://pep8online.com/)

Lighthouse in Chrome Devtools was used to test website performance, bestpractices, accessibility and SEO

- [Lighthouse](https://developers.google.com/web/tools/lighthouse)

### Testing User Stories

- #### Non-registered and registered users

    1. View products so i can select items to purchase:

        - Upon entering the site, the users are presented with three ways to navigate to the products page - a large button in the site banner, through the navbar and another button further down the homepage.

    2. Sort products by category, price (ascending and descending) and sort products alphabetically (ascending and descending):

        - Once a user has navigated to the products page, positioned at the top of the list of available products is a dropdown box to enable sorting.  This box remains at the top of the products page at all times and on all screen sizes.  The navbar has a dropdown option to show particular categories or all items.  Users are also able to click a category in a product's details to also view all other items in that category.

    3. Search for specific product using keywords:

        - The searchbox is situated in a dropdown in the sticky navbar meaning it is always accessible no matter where the user is situated in the site.

    4. View individual product details to easily see price, description and image:

        - Clicking on a product in the main product view will take the user to a detailed page for that product which includes description, larger image, and more detailed information of the product.

    5. View site owners blog:

        - The blog is available form the navbar and from another button on the home page.

    6. Register for an account or login:

        - Account functions are available from the navbar Account dropdown and there is also a button on the homepage to take a user to the signup/signin pages.

    7. View current items in my shopping cart:

        - The shopping cart is situated to the right of the fixed navbar and as such is always available to a visitor regardless of where they are located in the site.

- #### Registered users

    1. Ability to login/logout:

        - Through the account dropdown in the navbar users are able to login or logout depending on their current signed in status.

    2. Ability to reset a forgotten password:

        - The signin page has a forgotten password link.  This is handled by Allauth and the user recieves an email on forgotten password request.

    3. View previous purchase history:

        - Upon login, the user is presented with an option in the account navbar dropdown to view "my profile.  This page contains default delivery information and previous purchase history.

- #### Site owner/Administrator

    1. Login to administration panel:

        - By appending /admin to the homepage URL the user is presented with the Django administration login page.

    2. Within the administration panel be able to manage site users, products orders and blog posts:

        - The Django admin panel contains full functionality to be able to add, edit and & delete, users, products, categories, orders and blog posts.

    3. add, edit and remove existing products for sale & add, edit and remove blog posts:

        - When an admin user is logged in, they are presented with additional controls on the product pages and blog page.  There is an additional item in the accout dropdown menu in the navbar for 'Product management' whicj allows the user to add a new product.  There are edit and delete buttons visible on each item both in the all products views and in the individual products view. Within the blog page there is an add post button in the page banner and each individual blog post has its own edit and delete buttons.

### Further Testing

- The website was tested on Google Chrome, Internet Explorer, old Microsoft Edge, new Microsoft Edge and Mozilla Firefox browsers for desktop. In each of the browsers, the following were tested to ensure functionality:

    - Login & logout
    - View all pages
    - Register
    - Purchase a product through to completion

- The website was tested on Google Chrome, Safari, Samsung Internet and Amazon Silk on mobile devices. In each of the browsers, the following were tested to ensure functionality:

    - Login & logout
    - View all pages
    - Register
    - Purchase a product through to completion

- The website was viewed on a variety of devices such as Windows Desktop, Windows Laptop, Samsung S8, Samsung S20, Samsung S3 tablet, Motorola G4, Amazon Fire, iPhone7, iPhone 8.
- All text input fields were tested with no text, quantities of text that did not meet minimum length requirements and quantities of text exceeding the maximum length requirements. For fields labelled as required, the correct response was returned by the browser. For minimum and maximum requirements the expected tooltip response was returned by the browser.
- For login, an incorrect username and incorrect password were supplied to the login form. The expected 'invalid credential' flash message was shown on each incorrect attempt.
- The search function located in the navigation bar was tested with single characters, special characters and paragraphs of text.  The expected response was returned each time.  If results were available they would be returned, if there were no results the correct warning would be presented to the user.
- Frequent tests were undertaken after major code changes to ensure cross-browser and cross-device compatibility.
- Friends and family members of ages ranging from 15 to 73, were asked to review the site and documentation to point out any bugs and/or user experience issues.
- Google Lighthouse developer tool in Google Chrome dev tools was used to ensure pages meet best practice.

### Known Bugs and Resolutions if Applicable

- The product page was rendered using Django template logic.  This caused difficulty is setting images and buttons at equal height.  Default width was supplied to images to attempt to overcome this, but at the moment, the best method is to ensure the image is supplied with equal height and width to make sure it doesn't overrun it's allotted space.  Long term this is probably an unsustainable resolution and requires rebuilding the products page.
- Clicking add to cart from the products page redirects the user back to the products page, but if they have sorted results the sorting is forgotten and the user is presented back with the default sorting method.  This remains unfixed.
- W3 HTML checker reports unclosed div.  I am unable to find the div in question and believe it to be a false result.  The all pages render as expected.

## **Credits**

#### Content

All content is reproduced with express permission of JJ Mason.

#### Media

All media is supplied by site creator.

#### Acknowledgments

My wife for looking after the kids all those nights I couldn't.  I am in bedtime debit.. Jeremy Mason for letting me use his artwork. Jo Mason for assisting with the course.  My mentor Antonio for having positive words.