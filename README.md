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
  - [Features used](#features-used)
  - [Future Features](#to-do-list)
</details>

**<details><summary> Technologies</summary>**
  - [Languages](#languages)
  - [Frameworks, Libraries & Programs](#frameworks-libraries-programs)
</details>

**<details><summary> Deployment</summary>**
  - [Deploy to Heroku](#deploy-to-heroku)
</details>

**<details><summary> Testing</summary>**
  - [Testing Documentation](https://#)
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

### **<u>Design</u>**

**Structure**


**Colour scheme**


**Typography**

The site uses two fonts, both available from [Google Fonts](https://fonts.google.com/).  Headings and titles use IM Fell English.  Much of Jeremy's art is inspired by the work of Oscar Wilde and this font evokes the feeling of printed works from the 19th Century.  For larger pieces of text such as product descriptions Opens Sans is used for it's legibility.  Sans Serif is used as a fallback font, in case for any reason the fonts aren't being imported into the site correctly.

### **<u>User Stories</u>**

Non-registered and registered users:
- view products so i can select items to purchase
- sort products by category, price (ascending and descending) and sort products alphabetically (ascending and descending)
- search for specific product using keywords
- view individual product details to easily see price, description and image, product rating, and availability
- view site owners blog
- register for an account or login 
- view current items in my shopping cart
- complete a purchase and recieve a confirmation email


Registered users 
- ability to login/logout
- ability to reset a forgotten password
- view previous purchase history
- recover account
- reset password
- personalised user profile

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
- blog

### **Future Features**

- Forum
- product rating
- personalised message

## **Technologies Used**

-   allauth

#### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

#### Frameworks, Libraries & Programs


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

### Heroku Deployment

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

## **Credits**

#### Content


#### Media


#### Acknowledgments

