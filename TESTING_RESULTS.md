# Testing

_Frame for Testing Results adapted from ChatGPT.<br>
All tests, notes, observations, and screenshots created by the developer_

**Disclaimer:**
Due to late changes to website design before submission, <br>
testing results are more compact than previous testing file (TESTING.md).

## Pages & Core Features

- [V] Favicon displays correctly
- [V] 'Back to Shop' buttons works on all pages where displayed

### Navbar & Logo

- [V] Logo displays correctly and links to Home
- [V] All Navbar NavLinks and Icons visible, clickable, and responsive as appropriate to screen size
    - [V] Collapsed Navbar/Burger Menu displayed on smaller screens
    - [V] Navbar with all NavLinks and Icons displayed on larger screens
- [V] Collapsed Navbar menu works on smaller screens
    - [V] Items are highlighted on hover
- [V] Search Icon displayed on all screens
- [V] Search Bar opens correctly via Search Icon
- [V] Search Bar: placeholder visible, disappears on typing
- [V] Search Bar: returns correct results for valid input (except **Known Bugs** referred to in README)
- [V] Search Bar: error message for empty/invalid input

### Home (Products) / Art / Photos Pages

- [V] Products display with image, name, price, author, category badge

    ![Products Grid](docs/readme_images/home_page_products_opt_50.png)

- [V] Clicking product opens product detail page

    ![Product Detail page on iphone SE](docs/readme_images/product_detail_size_iphoneSE_opt_50.png)

- [V] Filtering products by sorting, badges, categories works

    ![Sorted by Category A to Z](docs/readme_images/sort_by_category_a_to_z_opt_50.png)

- [V] Responsive layout on all screen sizes

### How To...? Page

- [V] All links open the correct video
- [V] Video opens in a new tab
- [V] Layout and links responsive

### Newsletter

- [V] Email field visible and required
- [V] Confirmation message appears after submitting
- [V] Error message for invalid email
- [V] Confirmation email received
- [V] Subscribers saved on Django, and are only accessible by Admin

### Contact Us Page

- [V] Form fields display (Full Name, Email, Subject, Message)
- [V] Required validation works for all fields
- [V] Confirmation message appears after submission
- [V] Message is saved on Django, and only accessible by Admin

## User Icon

- [V] Accessible from Navbar
- [V] Dropdown menu with options to **Sign In** / **Sign Up**

### Sign In / Sign Out

- **Sign In**

- [V] Accessible via **User Icon**
- [V] Link **Sign Up** page opens up **Sign Up**
- [V] Required fields validation
- [V] Incorrect credentials handled
- [V] **Remember Me** option works
- [V] Username displayed in Navbar when Signed In

![Username displayed when Signed In](docs/readme_images/username_signed_in.png)

- [V] **My Account** and **Sign Out** available when Signed In
- [V] **Forgot Your Password** works

- **Sign Out**

- [V] Available only when Signed In
- [V] Sign Out works
- [V] Username no longer displayed
- [V] **My Account** and **Sign Out** no longer available


### Sign Up

- [V] Accessible via **User Icon** and link on **Sign In** page
- [V] Required fields validation
- [V] Confirmation appears after **Sign Up**
- [V] **Verify Your E-mail Address** is displayed
    - [V] Working **Contact Us** link on verification page
    - [V] **Contact Us** page opens


### My Profile

- [V] Editable **Default Postage Information** fields
- [V] Update notification appears

    ![Profile updated notification](docs/readme_images/profile_updated.png)

- [V] Fields are not mandatory
- [V] Order history accessible
- [V] **You have no orders to date** displayed when no orders

## Cart & Checkout

### Cart

- [V] Add to Cart works
- [V] Toast notification re added to cart works correctly
- [V] Update Quantity works and updates total
- [V] Remove item works
- [V] Free postage message appears correctly


### Checkout

- [V] All required fields validated
- [V] Payment & order submission works
- [V] Confirmation page displays order summary
- [V] Buttons **Adjust Cart**, **Complete Order** work as expected

### 404 Page

- [V] Custom error page displayed
- [V] Link **Back to Shop** works


## Admin / Product Management

- [V] Admin Sign In works
- [V] Product Management: add, edit, delete products, works as expected
- [V] Product images display correctly
- [V] Orders & users viewable via Django Admin
- [V] Links and navigation work as expected

## UI / Responsiveness / Visuals

- [V] Branding colors consistent
- [V] Fonts readable
- [V] Layout responsive in general on desktop, tablet, mobile (with some **Known Bugs** mentioned in README)
- [V] Buttons hover states consistent for most buttons
- [V] Navbar items lifted on hover
- [V] Forms styled consistently and following similar theme
- [V] Toasts / notifications readable, usually displayed for a few seconds
- [V] Images display correctly in galleries, products, toasts

## Automatic Testing/Validation

- [V] ESLint set up for JS testing (all steps and code learned from ChatGPT):
    ### Set up JS automatic testing:
    ![eslint.json from ChatGPT](docs/readme_images/eslint.json_from_chatGPT.png)

    ### Check all JS files - Run ESLint:
    npx eslint .

    ### Auto-fix minor JS issues:
    npx eslint . --fix

## Extra Notes/Screenshots

### Dropdown Menus

- On smaller screens: **Burger Menu**

![Burger Menu](docs/readme_images/burger_menu_dropdown.png)

- On larger screens: **Art Menu** and **Photos Menu**

![Art Dropdown menu](docs/readme_images/art_dropdown_menu.png)


![Photos Dropdown menu](docs/readme_images/photos_dropdown_menu.png)

- On all screens: **User Menu**

![Signed In User menu](docs/readme_images/user_menu_signed_in.png)

![Hover effect, Signed In User menu](docs/readme_images/hover_effect_signed_in_user_menu.png)


### Checkout

- [V] Screenshot demonstrating **Free Postage** working based on **Cart Total**
- [V] Longer pages, like **Checkout**, scroll behind the Navbar as expected, and can be seen beyond Navbar,
    for added effect

![Checkout page with free postage](docs/readme_images/checkout_free_postage_op_50.png)