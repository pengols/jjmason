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

## **Features**

### **Current Features**

- Developed with a 'mobile-first' ethos, the site is responsive on all device sizes.  Visitors to the site should experience no difference in functionality of the site regardless of screen viewing size. 
- Using the 3rd party package [Allauth](https://django-allauth.readthedocs.io/en/latest/) users are able to securely register, verify their account with a link provided by email and subsequently login to the site to be able to record their purchase history and peronalise their delivery details for future purchases.  Registered users are also able to perform a forgotton password request form the sign in page.

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

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts are used to import the 'Kumbh Sans' font into the style.css file which is used on all pages throughout the project.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Materialize to make the navbar responsive.
1. [Git](https://git-scm.com/)
    - Git is used for version control by utilising the Gitpod terminal to commit to Git and push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Gitpod:](https://gitpod.io/)
    - Gitpod was used as the IDE for creating the project.
1. [Heroku:](https://www.heroku.com/)
    - Heroku is used to host the website.

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

## **Credits**

#### Content


#### Media


#### Acknowledgments

