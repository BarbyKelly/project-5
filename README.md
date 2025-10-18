# Project 5 - Kelly's Art & Photo Boutique

[Kelly's Art & Photo Boutique](https://kellys-art-and-photo-boutique-913058c0223e.herokuapp.com/) was created as part of Code Institute's project,
for Diploma in Full Stack Software Development (E-commerce Applications) course.

Developer mainly based her project on Code Institute's Walk-through:
[Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode).
 
Aim of Kelly's Art & Photo Boutique:
- built for educational purposes only
- to create a Site where selection of Art and Photos are displayed
- sharing Art made by Developer's kids, and Photos taken by the Developer
- option for Site users to browse products, search and choose products
- test out purchasing products (without real transactions)
- option to Sign up and Sign in
- check out 'How To...?" videos with art lessons by selected YouTubers
- sign up for a Newsletter
- fill in a Contact form

This website has no real-time commercial intention.
No real orders, payments or deliveries.

Deployed site: [Kelly's Art & Photo Boutique](https://kellys-art-and-photo-boutique-913058c0223e.herokuapp.com/)

Github: [https://github.com/BarbyKelly/project-5](https://github.com/BarbyKelly/project-5)

Responsiveness test...

Am I Responsive image... update



# Contents

[Business Model for Kelly's Art & Photo Boutique](#business-model-for-kellys-art--photo-boutique)
- [Direct Audience](#direct-audience)
- [Indirect Audience](#indirect-audience)

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

[Bugs](#bugs)
- [Fixed Bugs](#fixed-bugs)
- [Known Bugs](#known-bugs)

[Deployment](#deployment)

[Forking Repository](#forking-repository)

[Creating Repository](#creating-repository)

[Credits](#credits)

[Acknowledgements](#acknowledgements)

# Business Model for Kelly's Art & Photo Boutique

## Direct Audience

The following groups are considered Direct Audience, as they are most likely to purchase, commission or order products from Kelly's Art & Photo Boutique:
  
  - Online Users searching for:
    - Original Art (e.g., Name Art, Seasonal Art such as winter, Animal Art etc.) 
    - Children's Art
    - Handmade Art
    - Photos (e.g., Sky, Beach, Animals, Rainbows, Variety etc.)

  - Educational Institutions: 
    - Schools and higher education providers seeking examples of art/photos or decorations for their institutions
    - Crèches and preschools incorporating childrens' art into projects

  - Healthcare and Care Homes:
    - Nursing homes and healthcare Practices searching for artwork or photos for waiting rooms, wards,
      and community spaces
    - Clinics and treatment areas where children and adults are tested or treated, to create a brighter more welcoming, 
      more homely/relatable atmosphere, and maybe inspire patients

  - Treatment Centers, Therapists:
    - Looking for artwork or photos to enhance the ambiance of the waiting rooms, therapy areas or playrooms, sensory sections

  - Hospitality and Accommodation Providers:
    - Restaurants, cafes, hotels, B&B's, Airbnb's, searching art or photos for specific ambiance
  
  - Individuals, couples, families, friends:
    - People seeking handmade and original gifts for variety of occasions eg graduation, first school day, birthday, anniversary, just to say 'Thank you'

  - Beauty and Spa businesses:
    - Salons, spas, wellness centers, looking for certain type of Art/Photos to complement their relaxing atmosphere


## Indirect Audience

Groups that are influenced by the display or recommendation of the products made by Kelly's Art & Photo Boutique:

- Business owners and interior designers:
  - Seeing products of Kelly's Art & Photo Boutique displayed in someone's living space, business,
    accommodation, Healthcare Provider, in Educational institution
  
- Visitors, friends, guests:
  - Individuals or groups exposed to art and photos in homes, schools, hospitality and accommodation places,
    hospitals, nursing homes, businesses, may be interested in requiring art from Kelly's Art & Photo Boutique

- Influencers and Promoters:
  - Influencers or Promoters, who share or recommend products from the boutique, on social media, blogs, 
    local networks, sharing boutique's reels/page

[Back to Business Model](#business-model-for-kellys-art--photo-boutique)

[Back to Contents](#contents)

# User Experience

## User Stories

Users may opt to tap, click, hover, open, fill various items listed below:

### Navbar

- **Logo**
  - Click **Logo** (to bring them back to Home Page or refresh Home Page)

- **Home**
  - Click **Home** NavLink to get back to Home page or to refresh Home page.
  - Click **Click Here To Shop** button on Home page

- **Art**
  - Hover on Art NavLink (on larger screens) for Art dropdown menu to be displayed
  - Click Art NavLink which opens up Art page with all of the Art available in the Boutique
  - Choose to click any item in dropdown menu, to select Art by specific category
  - Hover on badges (for all screen sizes) to highlight any badge that pointer is on
  - Click badges to choose an Art category
  - Choose to sort Art by Price, Name, Author, or Category
  - Select Art by: Animal, Name, Winter, or Variety

- **Photos**
  - Hover on Photos NavLink (on larger screens) for Photos dropdown menu to be displayed
  - Click Photos NavLink, which opens up Photos page with all of the Photos available in the Boutique
  - Choose to click any item in dropdown menu to select Photos by specific category
  - Hover on badges (for all screen sizes) to highlight any badge that pointer is on
  - Click badges to choose particular Photos category
  - Choose to sort products by Price, Name, Author, or Category
  - Select Art by: Animal, Name, Winter, or Variety
  - Choose photos by: Beach, Rainbow, Animal, Sky, or Variety

- **How To...?**
  - Click **How To...?** NavLink, to access 'How To...?' page
  - Select any of the YouTube links to watch by clicking on them
  - YouTube videos opening up in the new tab, leaving Kelly's Art & Photo Boutique's open in a previous tab

- **Newsletter**
  - Click **Newsletter** NavLink to open up Newsletter page with form
  - Fill in the form (email only) to sign up for Boutique's Newsletter
  - Click **Back to Boutique**
  - Click **Subscribe** to subscribe to the Newsletter

- **Contact Us**
  - Click **Contact Us** NavLink to open up 'Contact Us' page
  - Fill in form to contact Boutique
  - Click **Back to Boutique**
  - Click **Submit Contact Form**

- **User Icon**
  - Click **User Icon**, to access **Sign In** or **Sign Up**

    - **Sign In**

    ![Sign In page](docs/readme_images/sign_in_page.png)

      - Click **Sign In** to access 'Sign In' page with a Sign In Form
      - Click link: **Sign Up**
        - Where Users can create an account
        > Detailed **Sign Up** form features and testing available in [testing.md#sign-up-page-testing](testing.md#sign-up-page-testing) 
      - Fill the 'Sign In' form

      - **Sign In form**
        - Fill in **Username or Email**, and **Password**:
        - Tick **Remember Me** box:
        - Click **Home** button to return to Home page
        - Click **Sign In** button to sign in:
        - Click **Forgot Your Password?**:
            - Fill in **Password Reset** form:
              - Click **Reset My Password**
              - Click **Back to Sign In** button
              > Detailed **Sign In** form features and testing available in [testing.md#sign-in-page-testing](testing.md#sign-in-page-testing)

    - **Sign Up**

      ![Sign Up](docs/readme_images/sign_up.png)

      - Click **Sign Up** to access 'Sign Up' page and 'Sign Up' form:
      - Click **Sign In here**
        > Detailed **Sign In** form features and testing available in [testing.md#sign-in-page-testing](testing.md#sign-in-page-testing)
      - Fill the 'Sign Up' form
        - **Sign Up** form
          - Fill in E-mail address, E-mail address confirmation, Username, Password and Password (again)
          - Opt to click 'Back to Sign In' button to return to 'Sign In' form
          - Click 'Sign Up' button to Sign Up
          > Detailed **Sign Up** form features and testing available in [testing.md#sign-up-page-testing](testing.md#sign-up-page-testing) 

- **Cart**
  - Click **Cart** NavLink to open Shopping Cart page
    - Click **Back to Shopping** if no items in the cart
    - Click **Proceed to Secure Checkout** in the pop-up, after adding an item into the cart:

    ![Added to cart pop up](docs/readme_images/proceed_to_checkout_opt_50.png)

    - Click **Continue Shopping**
    - Click **Secure Checkout**

    ![Shopping Cart](docs/readme_images/shopping_cart_opt_50.png)


- **Search Icon/Search Form**
  - Click **Search Icon** to open up Search Form
  - Type in Search Form
  - Click Blue Search Icon (part of the form) or press Enter, to start search
  - Search Art and Photos in the Boutique with keywords eg 'rainbow':

    ![Search results for 'Rainbow'](docs/readme_images/search_results_rainbow_opt_50.png)

  - Click Blue Search Icon (part of the form) or press Enter, without typing in Search Form
    - Use 'x' in top right corner to close Error alert, when Search Form was left empty
  - Click Search Icon in the Navbar to close Search Form

- **Burger Icon/Menu** (on smaller screens)

  - Click Burger Icon to open dropdown menu
  - Choose any of the items from the dropdown menu and click them

- **User** who is not an Admin of Kelly's Art & Photo Boutique, **may not**:
  - Add, edit or delete products
  - Access Product Management
 
- **Users once signed in** may:
  - Notice a pop up: "Success! Successfully signed in as ..." displayed on top right
  - Access 'My Profile' via 'My Account'
  - Under their profile Update their Default postage information
  - See their Order History
  - Sign Out by clicking on 'Sign Out' under 'Sign In' tab

- **Extra permissions for An Admin**
  Admin may:
  - Access 'Product Management' once signed in
  - Add, edit and delete products via django, or directly on website when logged in as Admin (via Product Management)
  - Follow SKU system already in place: 
    dr33(add a unique number in the end) for Art,
    ph88(add a unique number in the end) for Photos

  - Admin may change the SKU system if needed
  - Admin may click Shopping cart and see if admin has any products in the cart (for testing)
  - Admin can create test purchases and delete them after
  - Admin may click all items on the website like other users

- **Footer**
  - User may click **Privacy Policy** to open it up
  - May click **Social Media** icons to open up their home pages

[Back to User Experience](#user-experience)

[Back to Contents](#contents)


# Wireframes

Wireframes created with [Balsamiq](https://balsamiq.com/wireframes/)

Disclaimer: There may be variations between Wireframes and the finished project.

## Home Page

![Wireframe, Homepage](docs/readme_images/home_page_wireframe_boutique_opt_50.png)

## All Items Menu

![Wireframe, All Items Menu](docs/readme_images/all_items_menu_wireframe_boutique_opt_50.png)

## Art Menu

![Wireframe, Art Menu](docs/readme_images/art_menu_wireframe_boutique_opt_50.png)

## Photos Menu

![Wireframe, Photos Menu](docs/readme_images/photos_menu_wireframe_boutique_opt_50.png)

[Back to Wireframes](#wireframes)

[Back to Contents](#contents)

# ERD, SEO and Marketing

## ERD

ERD is created as a visualization of the Kelly's Art & Photo Boutique's database structure.

- ERD steps learned from: [LucidChart Tutorial: How to Create an ERD](https://youtu.be/RBZtPhZkUZM?feature=shared)

- [LucidCharts](https://www.lucidchart.com/pages) used to create ERD

- Disclaimer: There may be variations between ERD and the finished database structure of the project.

  ![ERD](docs/readme_images/kelly's_art_and_photo_boutique_erd.png)

[Back to Contents](#contents)

## SEO

- SEO tests helped Developer to see robots.txt file was not ok.
  With tutors help, developer fixed robots.txt and sitemap.xml

- Google Lighthouse tests helped Developer to improve SEO score.

[Back to Contents](#contents)

## Marketing

### Facebook Mockup

- Developer set up Facebook Mockup to show how the website would look on Facebook:

  ![Facebook Mockup](docs/readme_images/facebook_page_post_opt_500.jpg)

### Facebook Reel

- Developer created a [Facebook Reel](https://youtu.be/F123AhI8RGA), with Stone Art,
  to show one of the options how she would advertise the arrival of a new  collection:

  All of the displayed stone Art in the Reel, was created by Developer's daughter Aoife, age 10

  Disclaimer: Reel is demonstrated via YouTube, in case sample business page for Facebook is taken down by Facebook 

[Back to ERD, SEO and Marketing](#erd-seo-and-marketing)

[Back to Contents](#contents)

### Keyword Research

- Developer used keywords suitable for the project eg photo, art, boutique, shop, handmade, original, Kelly's Art & Photo Boutique, gifts, décor

[Back to ERD, SEO and Marketing](#erd-seo-and-marketing)

[Back to Contents](#contents)


### Similar Businesses

- Developer found the following businesses relevant to her sample business:

  [Gallerix.ie](  https://gallerix.ie/)

  [JamArtFactory.com](https://jamartfactory.com/)

  [Kids and Art](https://kidsandart.org/store-artwork/)

  >To date Developer did not come across a website with same combination as hers: parent's photos and their kids' art in one online shop.

[Back to ERD, SEO and Marketing](#erd-seo-and-marketing)

[Back to Contents](#contents)


# Design

## Images

- **Background** image by the Developer

- **Logo** created together with Developers kids, by using Wireframe and Developer's photo and her kids art:

  ![Logo](docs/readme_images/logo.png)

## Color

- Base color **cornflower** for the website from: [Create.vista.com](https://create.vista.com/colors/color-names/cornflower/)

## Font

- From [Google Fonts](https://fonts.google.com/)

  - Main font: **Cormorant Garamond**

  ![Google Fonts](docs/readme_images/font_embed_opt_50.png)


[Back to Contents](#contents)

# Features

## Existing Features (mobile-first approach)

- **Favicon**

  - Favicon displayed in the browser tab for Kelly's Art & Photo Boutique:

    ![Favicon](docs/readme_images/favicon.png)

- **Navigation Menu**
  - **Navbar**
    - Global navigation appearing on all pages, consisting of:
      - **Logo**:
        - Clicking **Logo** returns user to the **Home** page or refreshes it if already on it
      - **User Icon**:
        - With **Sign In** and **Sign Up** options
      - **Cart**
      - **Search**:
        - Allows Users to search for Products
        - Search Icon displayed on all screen sizes
  
          ![Search Icon](<docs/readme_images/search_icon.png>)

        - Clicking the Search Icon opens the Search Form below the Navbar:

          ![Search Form](docs/readme_images/search__form.png)

        - Keyword search supported     
        - Empty search results display:
          - All Products
          - Error message near Search Icon: "Search criteria not entered!"
      
      - **Burger Menu**:
        - Dropdown menu of NavLinks
        - On larger screens, NavLinks are displayed instead of the Burger Menu
      - Hovering effect for all Navbar items and dropdowns

- **Footer**:
  - Copyright (year of the project)
  - Developer's name
  - Project type
  - Disclaimer: No real transactions
  - Clickable **Privacy Policy**, opens Privacy Policy in a new tab
  - Social Media links:
    - Clickable **Facebook**, **Twitter** and **YouTube** links: open respective pages in a new tab
      (general pages, not personalised for website)

### Home Page

  ![Home Page - mobile first](docs/readme_images/home_page_pixel7_opt_50.png)

  - Features only on Home page:
    - Background image
    - **Click here to shop** button:
      - All of the products are displayed on scrollable page after clicking on **Click here to shop**
      - Button is displayed near bottom left
 
[Back to Features](#features)

[Back to Contents](#contents)

### Art

- **Page Navigation**
  - Hovering effect for Art NavLink (on larger screens) displays dropdown menu of Art categories:
    - Animal Art, Name Art, Winter Art, Variety of Art
  - Clicking Art opens page with all Art

- **Badges**
  - Displayed below Navbar for all Art or selected category
  - Clickable to filter products by category

- **Sorting**
  - 'Sort by' option displayed on the right below badge(s):

    ![Options for sorting](docs/readme_images/sort_by_options_opt_100.png)

  - Sorting options: Price, Name, Author, Category

- **Product Cards**
  - On hover, pointer appears and product is raised up to highlight which product is hovered 
  - Card includes: Image, Name, Price, Author, Badge
  - Click on card opens product page

- **Product Page**
  - Displays image, name, price in €, badge, author, description
  - Quantity input (1-50) with arrows and manual entry
  - Buttons:
      - **Continue Shopping**: returns User to all Products (Art and Photos)
      - **Add to Cart**: adds product to cart with selected quantity

[Back to Features](#features)

[Back to Contents](#contents)


### Photos

- All features and functionality are identical to [Art](#art), except for categories:

  ![Photos Dropdown Menu](docs/readme_images/photos_dropdown.png)

  - Beach, Rainbows, Animals, Sky, Variety of Photos


### How To...?

- 'How To...?' page displays links to various YouTube channels, showing different styles of doing art

  ![How To...? page](docs/readme_images/how_to_page_opt_50.png)

### Newsletter

  ![Newsletter](docs/readme_images/newsletter.png)

- Subscription form
- Email address field
- Click **Back to Shopping**
- Or click **Subscribe**

### Contact Us

![Contact Us](docs/readme_images/contact_us.png)

- Clickable **Contact Us**
- Contact Form
- Buttons:
  - **Back to Shopping**
  - **Submit Contact Form**

### User Menu
- **Sign In**

  ![Sign In page](docs/readme_images/sign_in_form.png)

  - Displays **Sign In** form
  - Option to **Sign Up**
  - Buttons:
    - **Home**: returns User to Home page
    - **Sign In**: signs User in (if credentials are correct)
  - Option **Forgot Your Password?**, which opens:
    - **Password Reset** page:
      - Email address field
      - Buttons:
        - **Back to Sign In**: returns User to Sign In page 
        - **Reset My Password**: submits password reset request
  - **Username** displayed for signed in Users, with options:
    - **My Profile**: opens up User's Profile page
      - View and update default postage information
      - View order history
      - Button: **Update Information**
    - **Sign Out**: signs User out

  - **Admin Only** (additional permissions):
    - **Product Management**: add, edit and delete products

- **Sign Up**

  ![Sign Up](docs/readme_images/sign_up_form.png)

  - Displays **Sign Up** form
  - Option to **Sign In** if User account exist
  - Buttons:
    - **Back to Sign In**: returns User to Sign In page
    - **Sign Up**: register new account

### Cart

![Cart page](docs/readme_images/cart_page.png)

- Displays **Shopping Cart** page
- If cart is empty:
  - Message: **Your cart is empty**
  - Button **Back to shopping** brings User to all Products (Art and Photos)
- If item(s) in cart:
  - List of products with image, title, SKU, price, quantity, subtotal
  - Cart total, postage, and grand total
  - Buttons:
    - **Continue shopping**: returns User to all products
    - **Secure Checkout**: opens up Checkout page

  - **Checkout**
    - Accessible via Cart
    - Users can complete purchase (disclaimer: no real transactions, website for study purposes only)
    - Payment handled via Stripe integration
    - **Order Confirmation**
      - Accessible after completing checkout
      - Displaying order number, summary of purchased items, totals, and postage cost

[Back to Features](#features)

[Back to Contents](#contents)


## Future Features

- Active/chosen Menu Item is highlighted as active
- Registered Site User may save items for later, or as their favorites, to access these under their account
- Registered User is notified of saved items in their cart when they return to the website

- 'How To...?' page to include videos related to Photos, Photography
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

- Asterisks to mark all mandatory fields on all forms.

- 'Sign In' form: if incorrect details entered, pop up to display: 'The Username/email and/or password entered are incorrect. Please try again.'
At the moment default message mentions only username and/or password being incorrect.

!['Sign In' dropdown remains open](docs/readme_images/sign_in_menu_remains_open.png)

- Links in 'How To ...?' to include lessons how to take better photos

- Users can Sign Up and Sign In via social media links, Google account and similar

- Admin has an option to update prices in bulk for similar products

### About Creators

- App added to share details about the people who created Art & Photos for the Boutique. Maybe painted images of each creator.

### 'My Profile'

- to include email field

- fields to have a label above them or on the left

- alert set up to notify User that they are about to change their 'Default Postage Information'

- 'Phone Number' field to accept numbers only

- Set up restrictions, so User can not delete all 'Default Postage Information' and click on 'Update Information' when fields are left blank

- Instead of displaying 'Thank You for shopping' when User clicks on previous Order, in Order History, would be nice to display: "Your Order nr ..."

### Size options

- Limited to Landscape style or Portrait style, instead of both options available like now
- Image to reflect the size option that User has chosen, before they add the product into cart 

### Quantity

- Message to pop up for User: "Minimum quantity 1", when User tries to reduce minimum quantity below 1
- Alert to pop up: "Maximum quantity 50 per product", when User has quantity of 50 in insert box, and tries to click on upward arrow to quantity beyond 50 

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

Due to large volume of Tests done, Testing is reported in a separate [Testing.md](TESTING.md) file.

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

  7. When logged in as an admin, Sign In was still showing in the Navbar, and all of the options for admin were displayed at all times:

   ![Sign In not ok in Navbar](docs/readme_images/sign_in_not_ok.png)
  
  Click on other NavLinks, opened those links, yet Sign In menu remained open, and blocked top of other pages:

  ![Sign In menu blocking top part](docs/readme_images/sign_in_menu_blocking_top.png)

  When Developer clicked on Sign In NavLink to see if that would close the Sign In menu, Homepage opened instead.

  Solving:

  Issue located in main_nav.html with Chat GPT's help:

  ![Issue in main_nav.html](docs/readme_images/main_nav_sign_in_issue.png)

  ChatGPT guided Developer to see she was always rendering 'Sign In', signed in or not. 
  Which meant after being signed in, extra links were added as inside the same <li>.

  Developer fixed the styling for Navbar/NavLinks, to see if all would work together after Sign In fix, and ChatGPT guided Developer to reduce repetition of styling in main-nav.html.

  Sign In before and after fix, including updated styling:

  ![Sign In after fix](sign_in_fix.png)

  As a result of the fix, when Admin was signed in:
  - 'Sign In' NavLink was no longer displayed,
  - Username replaced 'Sign In' NavLink,
  - Options for Signed In Admin were available via dropdown menu
  - 'Sign Up' was no longer displayed for Signed In user/admin

  ChatGPT was a great help for fixing this error, and improving styling to match Django and Bootstrap.

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

- **Order Number**
  - The numeric part of the Order Number (eg '1') appears smaller font than the letters (eg 'ABC') on:
    - Order Details page, and on
    - 'Success!' pop up: 

    ![Order Number digit](docs/readme_images/order_number_digit.png)

- **Country**
  - Country name stopped displaying on Order Form, after Order Form was edited. Country at least shows up on Order confirmation.

- **Size checkout/models.py**
  Developer removed Size from most of the website, except from checkout/models.py, due to time constraint, in case migrations affect project too much, and Developer would not be able to fix it before the deadline. 
  Developer sees the need to add some form of Size to each product. As the products are all different sizes, it would be time consuming to add their unique sizes at this stage.

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
- If you want to fork one of your own repos, then DO NOT login under your own name, as fork option is not available

  ![How fork looks when logged in](docs/readmeimages/notpossibletofork.png)

- Search Github or Google for the repo that you would like to fork
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

  - Developer used [Canvas](https://www.canva.com/mockups) to create Mockups of the website. ChatGPT guided to Canvas.

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

- ChatGPT

  - Closer to the end of the project 5, Developer found out it is ok to check code and get guidance from ChatGPT.
  Developer had no previous coding experience with ChatGPT, as she thought students were supposed to avoid it.
  Learning to use ChatGPT was an interesting experience.
  ChatGPT helped to understand the updated guidelines for Django, Bootstrap, styling, and even helped to solve git commit issue, when
  security changes started to see vs code as a threat, and commits wouldn't go through.
  Changing permissions, and path with ChatGPT's guidance, git commit error got fixed.
  Something similar, would have usually been fixed with tutor's help.
  
  Developer found ChatGPT helpful in general.
  Even with all of the knowledge packed into ChatGPT, it was very important to check if suggestions matched Developer's vision,
  and trying to solve the issues first herself.
  Treating ChatGPT like a tutor, was useful.
  Before ChatGPT, Developer couldn't imagine getting so many errors fixed without tutor's help.
  It was lovely to be able to ask guidance at any time.

  - Performance improvement (after Lighthouse test)

    - Starting Performance score: 71

      ![Lighthouse score before performance fixes](docs/readme_images/lh_score_before_performance_fixes.png)

    - Developer shared initial Lighthouse score results with ChatGPT
    - Steps the Developer implemented based on ChatGPT's guidance:
      - Added 'defer' to the Stripe JS script in base.html
      - Updated {% for product in products %} loops in products.html, to improve loading time for images
      - Optimized background image file size (472KB to 190KB)
      - Uploaded optimized image to AWS S3
      - Deleted previous background image from both local media and AWS
      - In base.css, replaced the original local background image:

        background-image: url('/media/website_background.jpg');

        with the optimized AWS-hosted image:

        background-image: url('https://kellys-art-and-photo-boutique.s3.eu-north-1.amazonaws.com/media/website_background_opt_200.jpg');

      - Result: Lighthouse Performance score improved to 93

        ![Lighthouse score after performance fixes with ChatGPT's guidance](docs/readme_images/lh_score_after_performance_fixes.png)

  - Best Practices Score improved with ChatGPT's guidance

    - Starting Lighthouse score: 79

      ![LH report for Best Practices](docs/readme_images/lh_bp_starting_score.png)
    
    - Steps suggested by ChatGPT to improve Content Security Policy(CSP):

      ![Steps for CSP fix, by ChatGPT](docs/readme_images/lh_bp_csp_steps.png)

      ![Security and CSP fix](docs/readme_images/security_and_csp_from_chatgpt.png)

  - README styling:
    - ChatGPT guided Developer how to reduce nesting, and to use **bold** instead of headings, where many subcategories
    - Developer wished to link exact parts of Testing.md to README. ChatGPT showed how that could be done eg (testing.md#sign-up-page-testing)


- Business Model

  - Developer learned from [Sensical.ie project by David Calikes](https://github.com/davidcalikes/sensical.ie#prior-business-model) how to write Business Model for Kelly's Art & Photo Boutique. Mentor Lauren-Nicole Popich guided developer to this project, as an example for Business model.
   

# Acknowledgements

- Developer is grateful for any guidance and support provided by her family and friends; mentor Lauren-Nicole Popich; Student Care, especially Kim, facilitator Kay Welfare, tutors, Slack members, chatGPT, and online content creators.

- Special thank you to developer's daughters Aoife and Ciara, for allowing their beautiful art to be part of this e-commerce project, for creating a unique Logo based on Developer's ideas for the project, and Aoife's vision for the logo. Great team effort. And for asking Developer to increase prices for their Art. 

- Developer understands the importance of hiding Secret Keys. Mentor Lauren-Nicole Popich suggested to mention in README, that the secret key was visible at the start of the project, as the developer was following the steps from Boutique Ado walk-through, where Secret key was hidden at a later stage.
Developer changed the key asap and hid it, as advised by her mentor.

[Back to Contents](#contents)