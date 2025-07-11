# Project 5 - Kelly's Art & Photo Boutique

[Kelly's Art & Photo Boutique](https://kellys-art-and-photo-boutique-913058c0223e.herokuapp.com/) was created as part of Code Institute's project,
for Diploma in Full Stack Software Development (E-commerce Applications) course.

Developer mainly based her project on Code Institute's Walk-through:
[Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode).
 
Aim of Kelly's Art & Photo Boutique:
- built for educational purposes only
- to create a Site where selection of Art and Photos are displayed,
- sharing Art made by Developer's kids, and Photos taken by the Developer
- option for Site users to browse products, search and choose products, 
- test out purchasing products (without real transactions),
- option to Sign up and Sign in,
- check out 'How To...?" videos with art lessons by various YouTubers
- sign up for a Newsletter
- fill in a Contact form

This website has no real-time commercial intention.
No real orders, payments or deliveries.

Deployed site: [Kelly's Art & Photo Boutique](https://kellys-art-and-photo-boutique-913058c0223e.herokuapp.com/)

Github: [link to github](https://github.com/BarbyKelly/project-5)

Responsiveness test with [am i responsive](https://ui.dev/amiresponsive)

![Am I Responsive image](docs/readme_images/am_i_responsive_opt_350.png)


# Contents

[User Experience](#user-experience)
- [User Stories](#user-stories)

[Wireframes](#wireframes)

[ERD, SEO and Marketing](#erd-seo-and-marketing)
- [ERD](#erd-seo-and-marketing)
- [SEO](#seo)
- [Marketing](#marketing)

[Design](#design)
- [Images](#images)
- [Color](#color)
- [Font](#font)

[Features](#features)
- [Existing Features](#existing-features)
- [Future Features](#future-features)

[Languages Used](#languages-used)

[Sites, Apps Used](#sites-apps-used)

[Validation](#validation)
- [Lighthouse](#lighthouse)
- [HTML](#html)
- [CSS](#css)
- [Python](#python)

[Testing](#testing)
- [Favicon Test](#favicon-test)
- [Logo Test](#logo-test)
- [Search Bar Test](#search-bar-test)
- [Sign In Test](#sign-in-test)
- [404 Error Page](#404-error-page)

[Bugs](#bugs)
- [Fixed Bugs](#fixed-bugs)
- [Known Bugs](#known-bugs)

[Deployment](#deployment)

[Forking Repository](#forking-repository)

[Creating Repository](#creating-repository)

[Cloning Repository](#cloning-repository)

[Credits](#credits)

[Acknowledgements](#acknowledgements)


# User Experience

## User Stories

### Users may:

- Click on Logo (to bring them back to Home Page or refresh Home Page)
- Use Search Bar on larger screens to find Art and Photos 

- Click on 'Sign In' to access 'Sign In' form:
  - Click on link: 'Sign Up first' (steps for 'Sign Up' described below)
  - Fill in Username or Email, and a password:
    - Even if they don't have an account. Only User with an account will be signed in
    - Users without invalid/not existing Username or Email address, will be reminded: "Please fill in this field"
  - Tick 'Remember Me' box:
    - Even if they don't have an account. Only User with an account will be Remembered (depending on their cookie settings)
    - Users will be reminded to 'Please fill in this field', if they have not filled either of the 'Sign In' boxes correctly, 
      or if they do not have an account
  - Click on 'Home' button to get back to Home page
  - Click on 'Sign In' button to sign in:
    - Even if they don't have an account or have not entered correct details. Only User with an account and valid Username/e-mail and Password,
      will be signed in
    - User without an account or user who has not entered correct details, will be reminded to "Please fill in this field"
  - Click on 'Forgot Your Password?':
    - Even if they don't have an account.
      - Fill in 'Password Reset' form:
        - Click on 'Reset My Password'
        - Only User with an account and valid email address, will receive an email to reset their password
        - Click on 'Back to Sign In' button

- Click on 'Sign Up' to access 'Sign Up' form:
  - Click on: 'Sign In here' (which opens up 'Sign In' form, and steps for 'Sign In' form were described above)
  - Fill in E-mail address,E-mail address confirmation, Username, Password and Password(again)
    - Users are reminded: 'Please fill in this field' if they leave a required field blank
  - Click on 'Back to Sign In' button to return to 'Sign In' form
  - Click on 'Sign Up' button to Sign Up

- Click on Cart to open Shopping Cart page
  - Click on 'Back to Shopping' if no items in the cart

- Click on "Proceed to Secure Checkout" in the pop-up, after adding an item into the cart:

  ![Added to cart pop up](docs/readme_images/proceed_to_checkout_opt_50.png)

  - Click on 'Continue Shopping'
  - Click on 'Secure Checkout'

  ![Shopping Cart](docs/readme_images/shopping_cart_opt_50.png)

- Click on Nav Bar Menu Items, and dropdown Menus to choose which Items to display
- Choose to have products displayed by Category, by Price, by Author, or All Items
- Select Art by: Animal Art, Name Art, Winter Art, Variety of Art, or All Art
- Choose photos displayed by: Beach, Rainbows, Animals, Sky, Variety of Photos, or All Photos

### User who is not an Admin of Kelly's Art & Photo Boutique, may not:

- Add, edit or delete products
- Access Product Management

[Back to Contents](#contents)
 
### Users once signed in may:
- Notice a pop up: "Success! Successfully signed in as ..." displayed on top right
- Access 'My Profile' via 'My Account'
- Under their profile Update their Default postage information
- See their Order History
- Sign Out by clicking on 'Sign Out' under 'Sign In' tab

### Extra permissions for An Admin. Admin may:
- Access 'Product Management' once signed in
- Add, edit and delete products via django, or directly on website when logged in as Admin (via Product Management)
- Follow SKU system already in place: 
  dr33(add a unique number in the end) for art,
  ph88(add a unique number in the end) for photos

- Admin may change the SKU system if needed
- Admin may click on Shopping cart and see if admin has any products in the cart (for testing)
- Admin can create test purchases and delete them after
- Admin may click on all items on the website like other users

[Back to Contents](#contents)


# Wireframes

Wireframes created with [Balsamiq](https://balsamiq.com/wireframes/)

## Home Page

![Wireframe, Homepage](docs/readme_images/home_page_wireframe_boutique_opt_50.png)

## All Items Menu

![Wireframe, All Items Menu](docs/readme_images/all_items_menu_wireframe_boutique_opt_50.png)

## Art Menu

![Wireframe, Art Menu](docs/readme_images/art_menu_wireframe_boutique_opt_50.png)

## Photos Menu

![Wireframe, Photos Menu](docs/readme_images/photos_menu_wireframe_boutique_opt_50.png)


[Back to Contents](#contents)

# ERD, SEO and Marketing

## ERD

Not completed to date

[Back to Contents](#contents)

## SEO

SEO tests helped Developer to see robots.txt file was not ok.
With tutors help, developer fixed robots.txt and sitemap.xml 

[Back to Contents](#contents)

## Marketing

### Facebook Mockup

- Developer set up Facebook Mockup to show how her site would look in Facebook:

![Facebook Mockup](docs/readme_images/facebook_page_post_opt_500.jpg)

### Facebook Reel

- Developer created a [Facebook Reel](https://youtu.be/F123AhI8RGA), with Stone Art, to show one of the options how she would advertise the arrival of a new collection:

  All of the displayed stone Art in the Reel, was created by Developer's daughter Aoife, age 10

[Back to Contents](#contents)

[Back to ERD, SEO and Marketing](#erd-seo-and-marketing)

### Keyword Research

Developer used keywords suitable for the project eg photo, art, boutique, shop, cart

[Back to ERD, SEO and Marketing](#erd-seo-and-marketing)

[Back to Contents](#contents)


### Similar Businesses

Developer found the following businesses relevant and interesting:

[Gallerix.ie](  https://gallerix.ie/)

[JamArtFactory.com](https://jamartfactory.com/)

[Kids and Art](https://kidsandart.org/store-artwork/)

To date Developer did not come across a website with same combination as hers: parent's photos and their kids' art in one online shop.

[Back to ERD, SEO and Marketing](#erd-seo-and-marketing)

[Back to Contents](#contents)


# Design

## Images

- Background image by the Developer

- Logo image created together with Developers kids, using Wireframe and our own photos/art

## Color

- Base color (cornflower) for the website from: [Create.vista.com](https://create.vista.com/colors/color-names/cornflower/)

## Font

- Code for "Cormorant Garamond" font from [Google Fonts](https://fonts.google.com/selection/embed):

  ![Google Fonts](docs/readme_images/font_embed_opt_50.png)

[Back to Contents](#contents)

# Features

## Existing Features

### Home Page

  ![Home Page](docs/readme_images/home_page_boutique_opt_500.png)

### Favicon

Favicon displayed in the browser tab for Kelly's Art & Photo Boutique:

  ![Favicon](docs/readme_images/favicon.png)

### Logo

- Logo displayed on all pages of the website, and on all screen sizes
- Click on Logo brings user back to Home page

  ![Logo](docs/readme_images/logo.png)

[Back to Features](#features)

[Back to Contents](#contents)

### Search Bar

- Search bar displayed on larger screen sizes:

  ![Search Bar](docs/readme_images/search_bar_centered.png)

- Button to activate search
- User can search for Products: Art & Photos
- User can search for eg 'rainbow', and products from both Art and Photos are displayed:

  ![Rainbow Search](docs/readme_images/two_rainbows_found_opt_50.png)

- If user enters nothing in Search box, error message pops up:

  ![Search criteria error](docs/readme_images/error_search_criteria.png)


[Back to Features](#features)

[Back to Contents](#contents)


### Navigation Menu

#### Nav bar

- All Navigation Menu items are clickable and displayed below Logo on a larger screens, beside each other:

  ![Nav bar](docs/readme_images/nav_bar.png)

- Collapsed/burger-menu is displayed on smaller screens:

  ![All Items Dropdown Menu](docs/readme_images/burger_menu.png)

- When User clicks on 'All Items', dropdown opens:
  - All Items
    - By Category
    - By Price
    - By Author
    - All Items

- Previously opened dropdown menu closes, if another Button is clicked 

### Art

- When User clicks on 'Art', dropdown opens:

![Art Dropdown Menu](docs/readme_images/art_menu_dropdown.png)

- Art
  - Animal Art
  - Name Art
  - Winter Art
  - Variety of Art
  - All Ar

### Photos

- When User clicks on 'Art', dropdown opens:

![Photos Dropdown Menu](docs/readme_images/photos_dropdown.png)

- Photos
  - Beach
  - Rainbows
  - Animals
  - Sky
  - Variety of Photos
  - All Photos

### How To...?

- 'How To...?' page displays links to various YouTube channels, showing different styles of doing art

![How To...? page](docs/readme_images/how_to_page_opt_50.png)

### Sign In

![Sign In page](docs/readme_images/sign_in_form.png)

- Displaying 'Sign In' form
- And an option to 'Sign Up'
- To click on 'Home' button
- Or 'Sign In' button
- And to choose 'Forgot Your Password?", which opens up:
  - 'Password Reset' page:
    - User can enter email address,
    - Click on 'Back to Sign In', 
    - Or click on 'Reset My Password'

### Sign Up

![Sign Up](docs/readme_images/sign_up_form.png)

- Displaying 'Sign Up' form
- And an option to 'Sign In' if User already has an account
- Option to click on 'Back to Sign In' button
- Or 'Sign Up' button

### Cart

![Cart page](docs/readme_images/cart_page.png)

- Displaying 'Shopping Cart' page:
  - If cart is empty:
    - Message: 'Your cart is empty'
    - with a button below: 'Back to shopping'
  - If items placed in the cart by User:
    - list of products in the cart with image, title, size, and SKU
    - price of each item
    - quantity of each item
    - option to update quantity or remove product
    - cost of subtotal of each type of item
    - cart total
    - postage cost
    - grand total
    - buttons below: 'Continue shopping' and 'Secure Checkout'

### Contact Us

![Contact Us](docs/readme_images/contact_us.png)

- User can click on Contact Us
- Fill in Contact Form
- Click on 'Back to Shopping'
- Or click on 'Submit Contact Form'

### Newsletter

![Newsletter](docs/readme_images/newsletter.png)

- Newsletter page has an option to fill in Subscription form
- User can enter their email address
- Click on 'Back to Shopping'
- Or click on 'Subscribe'

### 'Click here to shop' button

- Clickable button to start to shop
- All of the products are displayed on scrollable page after clicking on 'Click here to shop'

### Footer
  - Copyright with year of the project
  - Developer's name
  - Stating it is an E-commerce Project
  - Disclaimer: NOt for real transactions
  - Privacy policy:
    - User can click on 'Privacy Policy' to access it
  - Social Media links:
    - Clickable
    - General Facebook, Twitter and YouTube pages open after click/tap
    - Mock Facebook page has been set up for the site. Developer understand Facebook can require deletion of the Mock up page,
    therefor Developer kept the general Facebook link

[Back to Features](#features)

[Back to Contents](#contents)


## Future Features

- Active/chosen Menu Item is underlined or otherwise highlighted
- Registered Site User may save items for later, or as their favorites, to access these under their account
- Registered User is notified of saved items in their cart when they return to the website

- Improved Descriptions for all products, to improve search for Users, and add more keywords
- Add an option to search Art and Photos by special celebrations: Easter, Christmas, Halloween, Birthday, Anniversary, Valentine's Day etc.
  (with improved Descriptions, this option will work, like now when looking for Winter, rainbow)
- Filter to search products with multiple options eg Stone Art - Birthday - Age 5
- Option to choose art based on what tools were used eg pencil, paint, water-color, marker, paper, stone, canvas

- Username is displayed when signed in

- Live classes with Site Visitors, creating Art, discussing techniques, sharing ideas

- Users can use search box to search all parts of the website, not just products

- Password Reset form would notify User if their email is not registered for an Account. Presently any email address is accepted on Password Reset form 

- Clickable Contact details below 'Password Reset' form, instead of just text as it is at the moment: 

  ![No 'contact us' details](docs/readme_images/password_reset_form.png)

- Clickable Contact details below 'Password Reset' email notice, instead of just text as it is at the moment:

  ![alt text](docs/readme_images/password_reset_email_sent.png)

- For Admin: System would suggest a new unique SKU, based on existing products, when Admin is adding a new product

- All required fields marked with asterisk

- On smaller screens, Search Icon was displayed before:

  ![Search Icon](docs/readme_images/search_icon.png)

  Due to Developer changing Nav bar items around, Search Icon is no longer displayed on smaller screens. Developer is aware this needs to be fixed.

- When User has added an item into Cart, at the moment 'Proceed to Secure Checkout' is displayed below the cart content. 'Back to shopping' button needs to be added beside it.

- Sign In menu to close after person has signed in. At the moment dropdown stays open even when other nav links are clicked on.

!['Sign In' dropdown remains open](docs/readme_images/sign_in_menu_remains_open.png)

[Back to Features](#features)

[Back to Contents](#contents)


# Languages Used

![Languages Used](docs/readme_images/languages_used.png)

- HTML
- Python
- CSS
- JavaScript
- Dockerfile

[Back to Contents](#contents)

# Sites, Apps Used

Developer used the following Sites/Apps to create Kelly's Art & Photo Boutique:

- [Code Institute](https://codeinstitute.net/)
- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [VS Code](https://code.visualstudio.com/)
- [Django](https://www.djangoproject.com/)
- [Heroku](https://www.heroku.com/)
- [Balsamiq Wireframes](https://balsamiq.com/wireframes/)
- [AWS](aws.amazon.com)
- [Stripe](https://stripe.com/)
- [YouTube](https://www.youtube.com/)
- [Simple Image Resizer](https://www.simpleimageresizer.com/)
- [Diffchecker](https://www.diffchecker.com/)
- [Favicon](https://favicon.io/favicon-converter/)
- [Font Awesome](https://fontawesome.com/icons)
- [Chat GPT](https://chatgpt.com/)

  Chat GPT only used near the end of the project, to:
  - fix Newsletter app error. It was not used to generate the code itself
  - understand why responsiveness test would not work

  ![Chat GPT](docs/readme_images/chat_gpt_check.png)


[Back to Contents](#contents)


# Validation

* For testing, in many places developer used "Kelly's Boutique" instead of "Kelly's Art & Photo Boutique", to reduce the number of characters, and make it easier read.

## Lighthouse

Lighthouse tests with Google developer tools:

- Kelly's Art & Photo Boutique 'Home' Page lighthouse test:

  ![Lighthouse test, Home](docs/readme_images/lighthouse_home.png)

- Kelly's Art & Photo Boutique 'All Products' Page lighthouse test:

  ![Lighthouse test, All Products](docs/readme_images/lighthouse_all_products.png)

- Kelly's Art & Photo Boutique 'Art' Page lighthouse test:

  ![Lighthouse test, Art](docs/readme_images/lighthouse_art.png)

- Kelly's Art & Photo Boutique 'Photos' Page lighthouse test:

  ![Lighthouse test, Photos](docs/readme_images/lighthouse_photos.png)

- Kelly's Art & Photo Boutique 'How To...?' Page lighthouse test:

  ![Lighthouse test, How To...?](docs/readme_images/lighthouse_how_to.png)

- Kelly's Art & Photo Boutique 'Sign In' Page lighthouse test:

  ![Lighthouse test, Sign In](docs/readme_images/lighthouse_sign_in.png)

- Kelly's Art & Photo Boutique 'Sign Up' Page lighthouse test:

  ![Lighthouse test, Sign Up](docs/readme_images/lighthouse_sign_up.png)

- Kelly's Art & Photo Boutique 'Cart' Page lighthouse test:

  ![Lighthouse test, Cart](docs/readme_images/lighthouse_cart.png)

- Kelly's Art & Photo Boutique 'Contact Us' Page lighthouse test:

  ![Lighthouse test, Contact Us](docs/readme_images/lighthouse_contact.png)

- Kelly's Art & Photo Boutique 'Newsletter' Page lighthouse test:

  ![Lighthouse test, Newsletter](docs/readme_images/lighthouse_newsletter.png)


[Back to Validation](#validation)

[Back to Contents](#contents)

## HTML

- HTML validator test with [W3C Markup Validation](https://validator.w3.org/) failed

## CSS

- CSS validator validation with [W3C Markup Validation](https://validator.w3.org/) failed

## Python

- Developer checked some of Python files with [CI Python Linter Test](https://pep8ci.herokuapp.com/)

![CI Python Linter test](docs/readme_images/ci_python_linter.png)

[Back to Validation](#validation)

[Back to Contents](#contents)

# Testing

## Favicon Test

![Favicon](docs/readme_images/favicon.png)

| Tested Item | Expected Outcome                                      | Outcome     |
| ----------- | ----------------------------------------------------- | ----------- |
| Favicon     | Reduced image of the Logo                             | as expected |
|             | Displayed in browser tab for all pages of the website | as expected |

[Back to Testing](#testing)

[Back to Contents](#contents)

## Logo Test

![Logo example on a smaller screen](docs/readme_images/logo_center_smaller_screen.png)

| Tested Item | Expected Outcome                               | Outcome     |
| ----------- | ---------------------------------------------- | ----------- |
| Logo        | Displayed top left for larger screens          | as expected |
|             | Displayed top center for smaller screens       | as expected |
|             | Displayed on all pages of the website          | as expected |
|             | Text 'Kelly's Art & Photos Boutique' is        |             |
|             | displayed big enough on all screen sizes       | as expected |
|             | Art and Photos on the Logo are                 |             |
|             | displayed big enough on all screen sizes       | as expected |
|             | Logo matches the theme of the website          | as expected |
|             | Clicking on Logo brings user back to Home page | as expected |  

[Back to Testing](#testing)

[Back to Contents](#contents)

## Search Bar Test

![Search Bar Test](docs/readme_images/search_bar.png)

Color changes when Hovering over Search Button:

![Color Changes when Hovering](docs/readme_images/color_change_when_hovered_over_search_button.png)

| Tested Item | Expected Outcome                                                                   | Outcome     |
| ----------- | ---------------------------------------------------------------------------------- | ----------- |
| Search Bar  | Displayed top center for larger screens                                            | as expected |
|             | Placeholder is faded in Search box                                                 | as expected |
|             | Personalized Placeholder                                                           | as expected |
|             | Placeholder text 'Search our Boutique for Art & Photos'                            | as expected |
|             | User can type in the Search box                                                    | as expected |
|             | Placeholder is no longer displayed, when first character is entered in Search Box  | as expected |
|             | Search button is clickable                                                         | as expected |
|             | Hovering over 'Search Icon' that is placed on the right of 'Search Bar' button,    | as expected |
|             | changes color of the button                                                        | as expected |
|             | User can click on Search button to activate Search                                 | as expected |
|             | If user enters a valid Search term, those products are displayed                   | as expected |
|             | When user enters eg number 9, all products made by 9 year old, are displayed       | as expected |         
|             | If user clicks on Search button without entering any value in Search Box,          |             |
|             | An error message "Search criteria not entered!" pops up                            | as expected |
|             | When user searches for eg 'rainbow', photo and art with rainbow are displayed      | as expected |
|             | When user types in random characters eg 'jjjj',                                    |             |
|             | '0' Products found for 'jjjj' is displayed                                         | as expected |
|             |                                                                                    |             |
|             | Search option is displayed on all pages of the website                             | as expected |
|             | User can search Products only: Art & Photos, not rest of the website               | as expected |


[Back to Testing](#testing)

[Back to Contents](#contents)

## Sign In Test

!['Sign In' form](docs/readme_images/sign_in_form.png)

| Tested Item | Expected Outcome                                                                    | Outcome     |
| ----------- | ----------------------------------------------------------------------------------- | ----------- |
|             |                                                                                     |             |
| Sign In     | 'Sign In' is clickable                                                              | as expected |
|             | Click on 'Sign In' opens 'Sign In' form                                             | as expected |
|             | 'Sign Up first' option is displayed below the heading                               | as expected |
|             | Placeholder 'Username or e-mail' is displayed in top box                            | as expected |
|             | Placeholder 'Password' is displayed in a Password box                               | as expected |
|             | User can type in 'Username or e-mail' and 'Password' box                            | as expected |
|             | Placeholder is no longer displayed, when User enters one character                  | as expected |
|             | 'Username or e-mail' and 'Password' are required fields                             | as expected |
|             | If either of the required fields have no character typed in,                        | as expected |
|             | Pop-up "Please fill in this field" is displayed                                     | as expected |
|             |                                                                                     |             |
|             | 'Remember Me' checkbox is optional                                                  | as expected |
|             | Checkbox is displayed below required fields                                         | as expected |
|             | Click on Checkbox ticks the box                                                     | as expected |
|             | Checkbox can be ticked multiple times                                               | as expected |
|             | User may remove tick before submitting the form                                     | as expected |
|             |                                                                                     |             |       
|             | 'Sign In' button is clickable                                                       | as expected |  
|             | Hovering over 'Sign In' button, changes color of the button                         | as expected |
|             | Click on 'Sign In' button Signs User in, if entered details are correct             | as expected |
|             | If either of the required fields is left empty, "Please fill in this field" pops up | as expected |
|             | If entered details are incorrect, pop up is displayed:                              | as expected |
|             | "The username and/or password you specified are not correct"                        | as expected |
|             | User may enter details again, and try to 'Sign In' again                            | as expected |   
|             |                                                       |             |
|             | 'Home' button is displayed on the left of 'Sign In' button                          | as expected |         
|             | 'Home' button is clickable                                                          | as expected |
|             | Hovering over 'Home' button, changes color of the button                            | as expected |
|             | Click on 'Home' button opens Home Page                                              | as expected |
|             |                                                                                     |             |
|             | 'Forgot Your Password?' is displayed below 'Home' and 'Sign In' buttons             | as expected |
|             | 'Forgot Your Password?' is clickable                                                | as expected |
|             | Click on 'Forgot Your Password?' opens up 'Password Reset' form                     | as expected |
|             | Placeholder is displayed in 'E-mail' address box                                    | as expected |
|             | Placeholder is no longer displayed, when first character is entered in e-mail box   | as expected |
|             | E-mail box is a required field                                                      | as expected |
|             |                                                                                     |             |
|             | If User omits '@' from the email address, pop up is displayed:                      |             |  
|             | "Please include an '@' in the email address. 'x' is missing an '@' "                | as expected |  
|             |                                                                                     |             |
|             | "Please fill in this field" is displayed if User clicks on 'Reset My Password' and  |             |
|             | has not typed any characters in e-mail box                                          | as expected |
|             |                                                                                     |             |
|             | If User omits any characters after '@' in the email address, pop up is displayed:   |             |  
|             | "Please enter a part following '@'. 'x@' is incomplete."                            | as expected |  
|             |                                                                                     |             |
|             | If User type in one character before '@', and one after in the e-mail box,          |             |  
|             | "Enter a valid email address" is displayed below the e-mail box                     | as expected |  
|             |                                                                                     |             |
|             | User can fill the 'Password Reset' form even if they don't have an account          | as expected |
|             | Only User with an account and valid email address,                                  |             |
|             | will receive an email to reset their password                                       | as expected |
|             | 'Reset My Password' button is clickable                                             | as expected |
|             | Hovering on the 'Reset My Password' button, changes the color of the button         | as expected |
|             |                                                                                     |             |
|             | If entered email address meets the requirements,                                    |             |
|             | and User has clicked on 'Reset My Password' button, message appears:                |             |
|             | "We have sent you an e-mail. If you have not received your Password Reset email,    | as expected |  
|             | please check your spam folder. Otherwise contact us"                                |             |  
|             |                                                                                     |             |
|             | 'Back to Sign In' button is displayed beside 'Reset My Password' button             | as expected |
|             | 'Back to Sign In' button is clickable                                               | as expected |
|             | Hovering on the 'Back to Sign In' button, changes the color of the button           | as expected |
|             | Click on 'Back to Sign In' button opens up 'Sign In' form                           | as expected |
|             |                                                                                     |             |
|             | Second click on 'My Account' closes dropdown menu                                   | as expected |  
       

[Back to Testing](#testing)

[Back to Contents](#contents)


## 404 Error Page

| Tested Item | Expected Outcome                                       | Outcome     |
| ----------- | ------------------------------------------------------ | ----------- |
| Error Page  | Personalized Error page 404 is displayed               | as expected |
|             | Tips how to fix this error are displayed               | as expected |
|             | Background image of the KAP Boutique is displayed      | as expected |
|             | Link to get back to KAP Boutique page    | as expected |
|             | KAP Boutique page opens when user clicks on the link   | as expected |         

[Back to Testing](#testing)

[Back to Contents](#contents)

# Bugs

## Fixed Bugs

- When developer clicked on any of Art or Photos nav-links, 0 items were displayed on all occasions, and NavLinks did not change color, 
  therefore it was hard to know which tab was open. Screenshot of when Developer expected to see 'All Art' displayed, 
  instead displayed were '0 products, with a heading 'All items':

    ![0 products displayed](docs/readme_images/0_products_displayed.png)

  Developer took these steps to fix main-nav links:

  1. Developer realised, in templates/main-nav.html, she had set up different categories for Art and Photos, than categories in categories.json or Django categories:

    ![main-nav categories](docs/readme_images/main-nav categories for art and photos.png)

    ![Django categories](docs/readme_images/django categories.png)

  therefore, Art and Photos categories couldn't display, under Art and Photos NavLinks

  2. Developer matched categories in main-nav with Django categories and categories.json

  3. Art and Photos displayed now correctly, except for Beach Photos.
  None of the 'Beach Photos' were displayed. Developer noticed 'beach-photos' instead of expected: 'beach_photos' in Django Categories:

    ![beach-photo instead of beach_photo](docs/readme_images/beach-photo instead of beach_photo.png)

  Developer fixed the category name from 'beach-photo' to 'beach_photo', then Beach Photos were displayed on the website as expected:

    ![beach photos displayed ok](docs/readme_images/beach_photos_displayed_ok_opt_50.png)

  4. Developer removed 'photo' from selection of photo titles to make wording look better on the screen (previously: 'Beach photo' title displayed for one photo, and 'Beach photo' displayed for more than one photo, instead of 'Beach Photos')

  5. Developer updated all of the new names/titles for Art and Photos in main-nav.html, categories.json, and Django Categories. 

  6. 'Sky' photos didn't display under 'All Photos'. Developer checked main-nav.html, and noticed sky_photos and animal_photos were still displayed in category, for 'All Photos'. Developer changed sky_photos for sky, and animal_photos for animal, and 'Sky' photos were displayed under 'All Photos' then.

[Back to Contents](#contents)

[Back to Bugs](#bugs)

### Fixed "django.core.serializers.base.DeserializationError: Problem installing fixture"

- Developer ran command: 'python manage.py loaddata categories' and "django.core.serializers.base.DeserializationError: Problem installing fixture..." appeared in the terminal.

- Earlier that day, tutor Oisin guided developer how to fix 'keyword: title' error, relating to json files

- Developer was able to follow similar steps to figure out the error:

- Developer broke down terminal error messages into 3 main (puzzle) pieces, to understand where was the error located:

#### Keyerror: author:

  ![keyerror: author](docs/readme_images/keyerror author.png)

#### No field_name author:

  ![no field_name author](docs/readme_images/no field_name author.png)

#### Fixtures categories.json:

  ![fixtures categories.json](docs/readme_images/fixtures categories.json.png)

- Developer had been focusing on field 'author' in categories.json file. Seeing 'author' is in categories.json file, so why would it come up as an error, 'no field_name author'

- After looking at these 3 parts of terminal messages, and checking out fields in Django for Adding 'Categories':

#### Django Add Categories:

  ![Django Add Categories](docs/readme_images/django admin categories.png)

developer realised issue was that categories.json had a field 'author', while in admin.py/Django categories there was no 'author' field set up

- Developer removed 'author' field from categories.json and 'python manage.py loaddata categories' command worked then ok:

  ![load categories command worked](docs/readme_images/load categories command worked.png)

- Fixing this bug/error was a great lesson for the developer, she learned how to better understand Terminal messages, and saw more value in them

- This error/bug also helped Developer to realize, she had added products to Django and hadn't updated categories.json accordingly, to reflect
changes made via Django Products.

- Product amounts were not updating in the basket: 
developer adjusted <div class="input-group-prepend"> and <div class="input-group-append"> in cart.html. 

Developer was able to update the amount of certain products in the cart, yet couldn't increase or decrease products when putting it into cart:

  ![Increase/decrease buttons not working](docs/readme_images/buttons_clicking_but_quantity_remains_the_same_opt.png)

Button still didn't work, after adusting cart.html, or quantity_input_script.html:

  ![Fixed var plusDisabled](docs/readme_images/fix var plusDisabled.png)

Arrows up and down in Quantity box, worked ok, and increased or decreased Quantity as needed, and Subtotal accordingly.

 
- nothing in the cart when clicking on add to cart

- cart shows €0.00 on the website, but when you click to open the cart, it has items in

- Plus and minus buttons would not work, when developer tried to adjust item quantities in the cart. 
  Developer could only increase the item quantities with arrows:

  ![Plus and minus buttons not working](docs/readme_images/bug_plus_minus_opt_50.png)

  Developer thought issue is in base.html, scripts must be not correct. As plus and minus buttons had worked when she followed Boutique Ado walk-through for her walk-through project.
  Developer used [Diffchecker](https://www.diffchecker.com/) to compare her project 5's code vs Boutique Ado walk-through lesson,
  and then compared the script codes vs the Boutique Ado version that had worked for the developer:

  ![Comparing codes with Diffchecker](docs/readme_images/bug_fix_plus_minus.png)

  Developer went back to lesson "Base Template Part 1":

  ![Base template changes](docs/readme_images/walk_through_instructions.png)

  to see where she may have made an error. Developer found that she had used the updated code when she created her walk-through project, but had used different version of code for project 5.

  Developer adjusted block corejs code in her project 5, to match the one that worked for her walk-through project. This fixed the error. Plus and minus buttons were fixed, developer was able to increase or decrease the number of particular item in the cart with plus and minus buttons:

  ![Plus and minus buttons work](docs/readme_images/plus_minus_work_opt_50.png)

  - Developer noticed how "All Photos" and "All Art", showed 0 items, while "All Items" displayed all items. She couldn't find 
    what was causing the error. Developer's coursemate Patrick Hladun found an error: two of the product categories had the same "pk":9 
  ![pk error](docs/readme_images/pk_error.png)

    Developer fixed conflict between pk numbers, and used ![jsonformatter.com](https://jsonformatter.org/) to help her to fix rest of categories.json, as "author": "author" was missing under pk:1, and pk:6 "author": "author" was missing one of these: '}':
    
    ![error line 1](docs/readme_images/error_line1.png)
    
    After fixing these errors, json file validation worked as expected:

  ![JSON working ok](docs/readme_images/fixed_pk.png)

- Developer noticed Logo had 'Art', while NavLinks had 'Drawings'. Developer replaced 'Drawing' with 'Art' in fixtures: categories.json, in django categories, and in index.html (Home page), and in main.nav html (templates), and then 'Art' was displayed instead of 'Drawings':

  ![Before: NavLink 'Drawings' instead of Art](<docs/readme_images/bug, art vs drawings.png>)


  ![After: NavLink 'Art'](<docs/readme_images/word drawings replaced with art.png>)

[Back to Bugs](#bugs)

[Back to Contents](#contents)

## Known Bugs

- Username not showing up when logged in

- Sign In menu closes after person has signed in. At the moment dropdown stays open even when other nav links are clicked on:

!['Sign In' dropdown remains open](docs/readme_images/sign_in_menu_remains_open.png)

- Search icon not displayed for smaller screens

[Back to Bugs](#bugs)

[Back to Contents](#contents)

# Deployment

- Ensure env.py is set up properly
- Check gitignore
- Set "DEBUG = 'DEVELOPMENT' in os.environ" in settings.py
- Login to Heroku
- Click on settings in the Menu
- Click on Reveal Config Vars
- Check if these look ok
- Click on Deploy in the main menu
- Scroll down to the end and click on Deploy Branch
- Once Heroku has finished deploying your app, "View app" appears at the bottom of the page
- Click on "View app"

[Back to Contents](#contents)

# Forking Repository

- Go to [Github](https://github.com/)
- Search Github or Google for the repo that you would like to fork
  - If it's your own repo, check out steps below for [cloning](#cloning-repository) instead
- Open the repo you want to fork
- On the same line as the Repo's name, on the right, click on the arrow beside the Fork
- Click on: + Create a new fork

- Choose a name for the repo
- Add description if you desire
- Choose if you want to Copy the main branch only
- Click on: "Create fork"

[Back to Contents](#contents)

# Creating Repository

- Code Institute's [template](https://github.com/Code-Institute-Org/ci-full-template) was used to set up this project.
- After clicking on the above template link, click on the green button: "Use this template"
- From there choose: "Create a new repository"
- Fill in "Repository name" with your desired name for the project
- Leave the project Public like the default setting (for Code Institute projects)
- Click on the green button "Create repository"

[Back to Contents](#contents)


# Cloning Repository

- Go to GitHub repo that you want to clone
- You may clone any public Repo of others, or your own private and public repos
- Click on the green button 'Code'
- Click beside the url to copy url of the repo
- Go to VS code
- Click on 'Source control' on the left side
- Click on 'Clone Repository'
- Paste the url and press Enter
- Select the location/folder where you want to store clone of this repo
- Ensure name of the folder is different to your previous repo, if you had a folder with that repo already
- Click on 'Select Repository Location'
- Click 'Open' if you wish to open cloned repo

  Developer found this [How to clone a repo](https://www.youtube.com/watch?v=ILJ4dfOL7zs) video clear, and helpful, and described steps 
  of cloning mainly based on this video.

# Credits

- CODE

  - Code for Kelly's Art & Photo Boutique is mainly based on Code Institute's Walk-through project ["Boutique Ado"] (https://github.com/Code-Institute-Solutions/boutique_ado_v1) 
  The developer has credited Walk-through mainly on top of html files, 
  due to enormous number of files.

  - Other projects, that Developer found helpful to make this project, have been credited in some files and below:

  ["Seaside Sewing by Kera Cudmore](https://github.com/kera-cudmore/seaside-sewing)

  ["Vegan Sneaker Store by Denis Klopotan](https://github.com/denisklopotan/vegan-sneaker-store/)

  [Chirpy Chooks by Kay Welfare](https://chirpy-chooks.herokuapp.com/)

[Back to Credits](#credits)

[Back to Contents](#contents)

- README

  - General README template derived from developer's Project 4 [BookBlog](https://github.com/BarbyKelly/blog). README for BookBlog was based on: [findMEreadME](https://github.com/brodsa/findMEreadME/blob/main/README.md#content)

  - Final README based on Developer's Project 2 ["Estonia Quiz" README](https://raw.githubusercontent.com/BarbyKelly/Estonia-Quiz/refs/heads/main/README.md)

[Back to Credits](#credits)

[Back to Contents](#contents)

- ICONS

  - Free Icons for Search and Social Media, from: [fontawesome.com](https://fontawesome.com/search?ic=free)

[Back to Credits](#credits)

[Back to Contents](#contents)

- LOGO

  - As Kelly's Photo & Art Boutique displays Art made by the developer's kids, the developer asked her kids to come up with a logo. 
  Website's Logo was designed by developer's 10 year old daughter Aoife. With developer's guidance, Aoife used Balsamiq Wireframes to create the Logo. Aoife chose colors based on Developer's wish for 'cornflower blue'.
  Developer used ![Color contrast check](https://coolors.co/contrast-checker/9fc5f8-134f5c) to check and slightly adjust contrast of colors. And together, developer and Aoife chose icons for Logo. Developer adjusted the layout of the Title on the Logo. Developer's 6 year old daughter Ciara watched every step, and gave her approval.
  Logo has Aoife's art work, Ciara's art work, and photo by the developer. 
  Website's finalised logo:

  ![Logo for Kelly's Art and Photo Boutique](docs/readme_images/logo_wireframe_by_aoife_ten_opt_50.png)

[Back to Credits](#credits)

[Back to Contents](#contents)

- FONT

  - Developer read [this article](https://webflow.com/blog/professional-fonts?utm_source=google&utm_medium=search&  utm_campaign=SS-GoogleSearch-Nonbrand-DynamicSearchAds-Tier4&utm_term=dsa-1480385100845___703207072761__&gad_source=1&gclid=Cj0KCQjwzva1BhD3ARIsADQuPnUfvRW_kuHUD-8GkB-9fEIf5ugmRlHpgHIsqWgaPlIm8EvOsCXomWIaAtElEALw_wcB) to figure out which font to use

  - Code for "Cormorant Garamond" font from [Google Fonts](https://fonts.google.com/selection/embed):

  ![Google Fonts](docs/readme_images/font_embed_opt_50.png)

[Back to Credits](#credits)

[Back to Contents](#contents)


- WIREFRAMES

  - Wireframes created with [Balsamiq](https://balsamiq.com/wireframes/)

[Back to Credits](#credits)

[Back to Contents](#contents)

- PRIVACY POLICY

  - Privacy Policy created based on lessons for Code Institute's walk-through [Boutique Ado](https://github.com/Code-Institute-Solutions/) 

  [Privacy Policy Generator ](https://www.privacypolicygenerator.info/) was used to create Privacy Policy.

[Back to Credits](#credits)

[Back to Contents](#contents)

- 'HOW TO...?' LINKS

  - Disclaimer: Boutique's admin shared selection of YouTube video links that she or her kids found helpful for creating art. No personal benefit from those or any other youtube channels shared on this website

[Back to Credits](#credits)

[Back to Contents](#contents)

- PRODUCTS AND IMAGES

  - All of the photos used for the website, were taken by the developer

  - All of the Art was made by developer's kids, at school, preschool, in art class, or at home

  - Images optimized with [Simple Image Resizer](https://www.simpleimageresizer.com/resize-image-to-50-kb)
    All converted images have 'opt' in the name to show they were optimized

[Back to Credits](#credits)

[Back to Contents](#contents)

# Acknowledgements

- Developer is grateful for any guidance and support provided by her family and friends; mentor Lauren-Nicole Popich; Student Care, especially Kim, facilitator Kay Welfare, tutors, Slack members, and online content creators.

- Special thank you to developer's daughters Aoife and Ciara, for allowing their beautiful art to be part of this e-commerce project, for creating a unique Logo based on Developer's ideas for the project, and Aoife's vision for the logo. Great team effort. And for asking Developer to increase prices for their Art. 

- Developer understands the importance of hiding Secret Keys. Mentor Lauren-Nicole Popich suggested to mention in README, that the secret key was visible at the start of the project, as the developer was following the steps from Boutique Ado walk-through, where Secret key was hidden at a later stage.
Developer changed the key asap and hid it, as advised by her mentor.

[Back to Contents](#contents)