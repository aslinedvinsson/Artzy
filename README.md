***Must haves to include except everything i PP4***

# Artzy
![](docs/responsive.png)////


Artzy is a distinctive e-commerce platform developed as a part of Portfolio Project 5 for the Code Institute's Full Stack Software Developer Course. Utilizing Django, HTML, CSS, JavaScript, and Python, Artzy dismantles the barriers to art appreciation, offering an extensive array of paintings and prints accessible to everyone, irrespective of their art knowledge.

With a focus on emotional resonance rather than academic credentials, Artzy curates art that speaks directly to the heart. It is founded on the belief that art should be a source of joy and inspiration for all, fostering a connection between the viewer and the artwork without necessitating expertise.

The vision behind Artzy extends beyond merely selling art; it's about encouraging mindful engagement with art, supporting a lifestyle where beauty, creativity, and personal expression are paramount. This approach is in line with modern values of meaningful consumption and the growing desire for experiences that truly enrich lives.

In essence, Artzy is not just a platform; it's a movement toward making art accessible and enjoyable for everyone, promoting a deeper, more personal interaction with the world of art.

The site was deployed via Heroku - the live site can be found here -
[Artzy](https://artzy-f5e67145006a.herokuapp.com/)

# Table of Contents

- **[Project Rationale - Bridging the Art Appreciation Gap](#project-rationale---bridging-the-art-appreciation-gap)**
  - [Purpose and Goal: Mission to Simplify Art Discovery and Ownership](#purpose-and-goal-mission-to-simplify-art-discovery-and-ownership)
  - [Target Audience: Who Artzy Serves - Connecting with Our Audience](#target-audience-who-artzy-serves---connecting-with-our-audience)
  - [Addressing Target Audience Needs: A Tailored Approach to Meeting Our Audience's Needs](#addressing-target-audience-needs-a-tailored-approach-to-meeting-our-audiences-needs)
  - [Business Model and Customer Goals: Accessibility at Scale and Enhancing Customer Experience through Art](#business-model-and-customer-goals-accessibility-at-scale-and-enhancing-customer-experience-through-art)

- **[Marketing and SEO Strategies](#marketing-and-seo-strategies)**
  - [SEO Strategies](#seo-strategies)
  - [Sitemap.xml](#sitemapxml)
  - [Robots.txt](#robotstxt)
  - [Marketing Strategies](#marketing-strategies)
    - [Content Marketing](#content-marketing)
    - [Social Media Engagement](#social-media-engagement)
    - [Email Marketing](#email-marketing)

- **[UI/UX Design](#uiux-design)**
  - [Wireframes](#wireframes)
  - [Colors](#colors)
  - [Fonts](#fonts)
  - [Images and Icons](#images-and-icons)

- **[Features Overview](#features-overview)**
  - [Navigation Bar](#navigation-bar)
  - [Home Page](#home-page)
  - [Account Registration and Management Pages](#account-registration-and-management-pages)
    - [Registration](#registration)
    - [Login](#login)
    - [Logout](#logout)
    - [User Profile](#user-profile)
    - [Update Profile](#update-profile)
  - [Product Exploration Pages](#product-exploration-pages)
    - [Listing](#listing)
    - [Detail](#detail)
    - [Wishlist](#wishlist)
  - [About and Contact Pages](#about-and-contact-pages)
  - [Newsletter and Communication Pages](#newsletter-and-communication-pages)
  - [Shopping Cart and Checkout Process](#shopping-cart-and-checkout-process)
  - [Checkout Page](#checkout-page)
  - [Checkout Success Page](#checkout-success-page)

- **[Security Features and Defensive Design](#security-features-and-defensive-design)**
  - [User Authentication](#user-authentication)
  - [Form Validation](#form-validation)
  - [Database Security](#database-security)
  - [Error Pages](#error-pages)

- **[Database Design](#database-design)**
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Custom Models](#custom-models)

- **[Technologies Used](#technologies-used)**
  - [Languages](#languages)
  - [Frameworks and Libraries](#frameworks-and-libraries)
  - [Programs and Services](#programs-and-services)

- **[Testing](#testing)**
  - [Responsive Testing](#responsive-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Bugs and Resolutions](#bugs-and-resolutions)
  - [Code Validation](#code-validation)
  - [User Stories Testing](#user-stories-testing)
  - [Feature Testing](#feature-testing)

- **[Deployment](#deployment)**
  - [Heroku](#heroku)
  - [Stripe](#stripe)
  - [AWS](#aws)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Cloning the Repository](#cloning-the-repository)

- **[References and Credits](#references-and-credits)**
  - [Content and Media](#content-and-media)
  - [Acknowledgements](#acknowledgements)

- **[Disclaimer](#disclaimer)**




# Project Rationale - Bridging the Art Appreciation Gap with Artzy
Artzy is a pioneering e-commerce platform designed to bridge the gap between the vibrant art community and those who may feel daunted by the world of art due to their limited knowledge. With a focus on simplifying art appreciation and making the acquisition of art pieces like paintings and prints more accessible, Artzy aims to connect a diverse audience to the art world. By utilizing strategic keywords such as "accessible art", "online art platform", and "art for beginners", we enhance our visibility and appeal to a wide range of art enthusiasts searching for easy entry points into art collection and appreciation.

## Purpose and Goal: Simplifying Art Discovery and Ownership for Everyone
Artzy’s mission is deeply rooted in demystifying the art discovery and purchase process. By offering a curated selection of "affordable paintings", "limited edition prints", and "digital art", we cater to a broad audience ranging from art novices to seasoned collectors. Keywords like "simplifying art discovery" and "online art buying" are integral to our content strategy, ensuring Artzy is easily found by those seeking to enrich their lives with art without the intimidation often associated with traditional art galleries.

## Target Audience: Artzy's Commitment to Art Enthusiasts and Beyond
Artzy is dedicated to serving a diverse group including "art enthusiasts", "gift shoppers", and "home decorators" looking for "unique art gifts" and "wall art" to personalize their spaces. Our platform targets individuals embarking on their "art discovery journey", leveraging keywords to resonate with users seeking "easy art buying experiences" and "art for personal spaces", ensuring a wide reach and relevance in search queries.

## Addressing Audience Needs: Tailoring the Artzy Experience
We understand the unique needs of our audience, from those making their first art purchase to seasoned collectors. Artzy's intuitive platform offers "emotion-based art", employing keywords that highlight our unique selling points like "informative art descriptions" and "user-friendly art selection". This strategic use of language not only aids in SEO but ensures our platform meets the varied needs of our users, making art selection an informative and enjoyable process.

## Business Model and Customer Goals: Promoting Art Accessibility and Engagement
As a B2C e-commerce platform, Artzy champions "democratizing art access" and enhancing the art purchasing experience. Our diverse collection, ensuring there's something for every taste and preference. By integrating keywords related to "art e-commerce" and "digital art marketplace" into our digital marketing strategies, we aim to attract a broad audience and foster a culture of art appreciation, making art accessible to all.


## SEO Strategies: Enhancing Artzy's Digital Footprint
To maximize Artzy’s visibility online, we meticulously research and integrate specific keywords like "buy art online", and "start an art collection". Utilizing tools like Google Trends and Keyword Planner allows us to identify and incorporate terms that potential customers frequently use. Our content, from website metadata to newsletters, is carefully crafted to include these keywords, ensuring Artzy ranks highly in art-related searches. This strategic approach not only improves our search engine rankings but also makes art more accessible to those seeking it.

### Note on SEO and Keyword Strategy
In our mission to make art more accessible and to enhance Artzy's visibility online, we've employed a strategic approach to SEO (Search Engine Optimization). You'll notice terms within quotation marks, such as "buy art online" and "digital art marketplace," throughout this document. These aren't random; they're strategic keywords identified to enhance Artzy's search engine visibility. The quotation marks highlight these carefully chosen keywords, underscoring our targeted SEO efforts to connect with our audience more effectively. This transparent approach is part of our ongoing strategy to make Artzy easily discoverable and accessible to all art enthusiasts and newcomers alike.

## Sitemap.xml
Adding a sitemap.xml to Artzy aids search engines in quickly finding and indexing the pages, thereby improving the site's visibility and SEO, leading to increased traffic. The sitemap.xml acts as a roadmap of the website, listing all important pages and content. This facilitates easier discovery, indexing, and understanding of the site’s structure and content hierarchy by search engine crawlers, enhancing SEO by ensuring all art collections and related content are found and ranked appropriately, ultimately driving more organic traffic to Artzy.

## Robots.txt
Utilizing a robots.txt file for Artzy directs search engine bots on which pages to crawl and index, improving site navigation and SEO efficiency. The file serves as a directive for search engine bots, specifying which areas of the site should be crawled and which should be ignored. By managing bot traffic, I ensure the indexing of key pages and prevent server overload from unnecessary crawling. This not only improves Artzy’s SEO by ensuring relevant content is quickly found and indexed but also enhances the overall user experience by highlighting the most important content.


## Agile
This project followes agile methods. I identified Epics and broke them down to user stories to map out what needs the customer and seller have. For every user story there are Acceptance criteria that needs to be met and in some cases more concrete tasks. The userstories are sorted with the use of the MoSCoW method, giving the userstories labels like "Must Have", "Should Have", "Could Have" and "Wount have". Git Hub projects is used to document it and track the progress of the deveoplment. The Epics and User stories are divided into to Milestone. The first one is Requirements Specification and Analysis, Technical set up and Design and the second one is Interface and user experience including CRUD functionality, search and sort.

The Epics and User stories are documented on a Kanban board on Git Hub and can be viewed [here](https://github.com/users/aslinedvinsson/projects/8/views/1)

## Work approaach
This project originated from a template provided by a Code Institute project called Boutique Ado. After implementing all the features from Boutique Ado, I transitioned the project into a unique creation of my own. I modified aspects of the front end and introduced new features to the back end. For much of the design work, I utilized Bootstrap.

## Marketing strategies
To effectively market Artzy, the art e-commerce platform, I will employ a multi-faceted strategy designed to engage our target audience and enhance our online presence.

### Content Marketing
We will develop newsletters and social media content that educates and inspires our audience about art. By focusing on storytelling, we aim to highlight artists and their work, making art more relatable and accessible to everyone.

### SEO
We will optimize the website with relevant keywords identified through research. This will improve our visibility in search engine results and attract organic traffic from individuals interested in purchasing art.

### Social Media Engagement
We will utilize platforms like Instagram and Facebook, where visual content thrives, to showcase our art pieces. Creating engaging posts and connecting with our audience through comments and stories will be key.

#### Facebook
![](docs/fb.png)

Facebook posts
![](docs/fbpost.png)
![](docs/fbpost2.png)

### Email Marketing
We will launch an email newsletter to keep subscribers informed about new arrivals, exclusive offers, and upcoming sales. This strategy is intended to encourage repeat visits and foster a community around the brand.


# UI/UX Design
Artzy e-commerce platform is a vibrant gateway to creativity, featuring an inspiring homepage alive with color, designed to captivate and draw art lovers into a world of visual delight. With a minimalist approach, I’ve chosen a white background for browsing art, ensuring each piece stands out with its true colors and details, offering a clean and focused viewing experience akin to an exclusive gallery.

Navigation on my site is intentionally streamlined and intuitive, allowing you to explore curated collections effortlessly. The visual design emphasizes a user-friendly interface, highlighting simplicity and ease, making the discovery and acquisition of art an enjoyable and straightforward journey for every visitor.

By focusing on a clean, engaging, and easy-to-navigate experience, I aim to enrich the art buying process, turning it into a journey of discovery and inspiration for all who visit.

## Wireframes

<details open>
    <summary>Desktop home page</summary>
    <img src="docs/wireframes/home_dt.png">
</details>

<details>
    <summary>Mobile home page</summary>
    <img src="docs/wireframes/home.png">
</details>

<details>
    <summary>Desktop products page</summary>
    <img src="docs/wireframes/products_dt.png">
</details>

<details>
    <summary>Mobile products, products_detail and product_management page</summary>
    <img src="docs/wireframes/products.png">
</details>

<details>
    <summary>Desktop product detail page</summary>
    <img src="docs/wireframes/product_detail_dt.png">
</details>
<details>
    <summary>Desktop newsletter page</summary>
    <img src="docs/wireframes/newsletter_dt.png">
</details>

<details>
    <summary>Mobile newsletter page </summary>
    <img src="docs/wireframes/newsletter.png">
</details>

<details>
    <summary>Desktop shopping cart page</summary>
    <img src="docs/wireframes/shopping_cart_dt.png">
</details>

<details>
    <summary>Mobile shopping cart page////</summary>
    <img src="docs/wireframes/shopping_cart.png">
</details>

<details>
    <summary>Desktop about page</summary>
    <img src="docs/wireframes/about_dt.png">
</details>

<details>
    <summary>Mobile about page with contact section</summary>
    <img src="docs/wireframes/about_contact.png">
</details>

<details>
    <summary>Desktop contact page</summary>
    <img src="docs/wireframes/contact_dt.png">
</details>
<details>
    <summary>Desktop profile page</summary>
    <img src="docs/wireframes/profile_dt.png">
</details>

<details>
    <summary>Mobile profile page////</summary>
    <img src="docs/wireframes/profile.png">
</details>

<details>
    <summary>Desktop checkout page</summary>
    <img src="docs/wireframes/checkout_dt.png">
</details>

<details>
    <summary>Mobile shopping cart and checkout page</summary>
    <img src="docs/wireframes/shoppingcart_checkout.png">
</details>

<details>
    <summary>Desktop product management page</summary>
    <img src="docs/wireframes/product_management_dt.png">
</details>

<details>
    <summary>Mobile product management page/// </summary>
    <img src="docs/wireframes/product_management.png">
</details>

<details>
    <summary>Desktop wishlist page</summary>
    <img src="docs/wireframes/wishlist_dt.png">
</details>

<details>
    <summary>Mobile wishlist page/// </summary>
    <img src="docs/wireframes/wishlist.png">
</details>

<details>
    <summary>Desktop sign up for newsletter</summary>
    <img src="docs/wireframes/signup_newsletter_dt.png">
</details>
<details>
    <summary>Mobile newsletter and sign up for newsletter</summary>
    <img src="docs/wireframes/newsletter.png">
</details>


## Colors
Choosing a vibrant and colorful image for the homepage against a white background with black text is a strategic move designed to instantly grab the visitor's attention. This pop of color makes a bold statement, ensuring the artwork and, by extension, the products, are the stars of the show.

The contrasting white header and black footer enhance readability and frame the homepage art beautifully, without overshadowing the main attraction. On subsequent pages, the white background with black text continues this theme of simplicity and focus, ensuring that the colorful homepage art remains the visual highlight of the website.

This color scheme is not just about aesthetics; it's a deliberate choice to make the shopping experience more engaging and memorable. By keeping the design elements minimal and focused, the website directs visitors' attention exactly where it needs to be: on the products and the vibrant imagery that represents them. This approach not only improves user engagement but also strengthens the site's branding.

## Fonts
PT Sans from [Google Fonts](https://fonts.google.com/?query=pt+sans) is a versatile, open-source font that's free and easy to use across all digital platforms. Its wide language support and variety of styles make it suitable for global projects and diverse design needs, ensuring the content is both accessible and visually appealing.

## Images
The site uses images from [Unsplash]( https://unsplash.com/).

## Icons
The site uses icons from [Font AIsome]( https://fontaIsome.com/ ).

Favicon comes from A by H Alberto Gongora from <a href="https://thenounproject.com/browse/icons/term/a/" target="_blank" title="A Icons">Noun Project</a> (CC BY 3.0)

## Text content
Text content, such as the names of artworks, artists, descriptions of the art, newsletter text is generated by ChatGPT.

## User stories
<details>
<summary><b>Epic: About page</b></summary>
<ul>
  <li><b>As a user, I want to read a concise overview of the art e-commerce site on the About page.</b>
    <ul>
      <li>The About page should contain a brief history of the company.</li>
      <li>The page should have contact information available.</li>
      <li>The About page should be easy to navigate.</li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><b>Epic: Newsletter Subscription</b></summary>
<ul>
  <li><b>As a website visitor, I want to fill out the newsletter subscription form, so that I can receive updates through a newsletter.</b>
    <ul>
      <li>The subscription form is easy to find on the website.</li>
      <li>The form requires minimal information (e.g., name and email address).</li>
      <li>Users receive a confirmation email upon subscription.</li>
    </ul>
  </li>
  <li><b>As a subscriber, I want to easily unsubscribe from the newsletter.</b>
    <ul>
      <li>Subscribers can unsubscribe via a link in the newsletter.</li>
      <li>Changes to subscription preferences are processed immediately.</li>
    </ul>
  </li>
  <li><b>As a seller, I want to create and send newsletters to subscribers.</b>
    <ul>
      <li>There is an interface for creating newsletter content.</li>
      <li>Newsletters can be sent to all subscribers.</li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><b>Epic: Message Notification to Users</b></summary>
<ul>
  <li><b>As a user, I receive notifications for important updates or messages.</b>
    <ul>
      <li>User receives notifications for account-related activities like registration, login/logout, and password changes.</li>
      <li>User receives notifications for shopping cart-related activities like changes the user does in the shopping cart before submitting the order.</li>
      <li>User receives notifications for order-related activities like order confirmation, delivery.</li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><b>Epic: Wishlist</b></summary>
<ul>
  <li><b>As a customer, I want to add products to my wishlist so that I can return to them later.</b>
    <ul>
      <li>The customer can add a product to the wishlist from the product page.</li>
      <li>The customer can see the number of products in their wishlist on the main menu.</li>
      <li>The customer can view their wishlist by clicking on the wishlist in the main menu.</li>
    </ul>
  </li>
  <li><b>As a customer, I want to see my saved products in my wishlist so that I can plan my purchases.</b>
    <ul>
      <li>The wishlist shows all products that the customer has added.</li>
      <li>The customer can see product images, names, prices for each product in the wishlist.</li>
    </ul>
  </li>
  <li><b>As a customer, I want to remove products from my wishlist so that I can manage my desires.</b>
    <ul>
      <li>The customer can remove a product from the wishlist from the wishlist page.</li>
      <li>When a product is removed from the wishlist, the wishlist is immediately updated.</li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><b>Epic: Checkout management</b></summary>
<ul>
  <li><b>As a user, I can proceed to checkout and complete the purchase.</b>
    <ul>
      <li>User can navigate to the checkout page from the shopping cart.</li>
      <li>User can view the summary of items in the cart.</li>
      <li>User can input delivery and payment details.</li>
      <li>User receives confirmation upon successful payment completion.</li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><b>Epic: Shopping cart management</b></summary>
<ul>
  <li><b>As a user, I can add items to my shopping cart for purchase.</b>
    <ul>
      <li>User can click on the "Add to Cart" button on the item details page.</li>
      <li>Item is added to the user's shopping cart.</

li>
      <li>User can view the updated cart with the added item.</li>
      <li>User can add multiple items to the cart.</li>
    </ul>
  </li>
  <li><b>As a user, I can update items in my shopping cart to change their quantities or remove them altogether before finalizing my purchase.</b>
    <ul>
      <li>Next to each item in the cart, there are options to adjust the quantity of the item or remove it from the cart.</li>
      <li>When the user adjusts the quantity, the cart updates to reflect the new quantity of the item.</li>
      <li>User can remove multiple items from the cart in one session.</li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><b>Epic: System setup</b></summary>
<ul>
  <li><b>User story: As a developer, I set up a new Django project to develop a web application.</b>
    <ul>
      <li>Start Django project.</li>
      <li>Create .gitignore file.</li>
      <li>Add allowed hosts in settings.py.</li>
      <li>Create superuser account.</li>
      <li>Install Django allauth.</li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><b>Epic: Product Management</b></summary>
<ul>
  <li><b>As a user, I can view the list of items and details of an item listed on the e-commerce site.</b>
    <ul>
      <li>User can view a list of items and select some to purchase.</li>
      <li>User can view a specific category of items without having to search through all items.</li>
      <li>User can navigate to the item details page.</li>
      <li>User can view item name, description, price, and images.</li>
      <li>User can see seller information.</li>
      <li>User can see reviews and ratings if available.</li>
    </ul>
  </li>
</ul>
</details>

Git Hub Kanban board can be viewed [here](https://github.com/users/aslinedvinsson/projects/8/views/1)


## Features Overview/// Korrekturläs

### Navigation Bar
- Unregistered User: Displays navigation links, brand logo (redirects to the home page), search bar, Login/Sign Up link, and shopping bag icon
- Registered User: Displays navigation links, brand logo (redirects to the home page), search bar, user's account name, and shopping cart icon

### Home Page
Visible elements vary based on user registration status

### Account Registration Page
Displays a registration form and a link to the login page

### Login Page
Features a login form, "Remember Me" option, links to the home page and password recovery

### Logout Page
Shows a logout button

### Product Listing Page
Lists products with an image, name, artist, category, and price Includes a "Back to Top" button

### Product Detail Page
Details product name, artist, category, price, description, quantity selector, "Keep Shopping" and "Add to Bag" buttons, and an "Add to Wishlist" option

### Wishlist Page
Specific contents undisclosed

### About Page
Showcases an image and text about Artzy

### Contact Page
Contains a user contact form

### Newsletter Page
Displays an image and the latest newsletter, which is also distributed to subscribers

### User Experience Differentiation
Describes the difference in site visibility and access between logged-in and logged-out users

### Shopping Cart Page
Lists order information, including price, quantity, subtotal, item management options, cart total, delivery charges, free delivery threshold, and navigation buttons

### Checkout Page
Presents an order summary, delivery information, payment options, and completion steps

### Checkout Success Page
Confirms the order and informs about the confirmation email sent

### User Profile Page
Displays the user's default picture, delivery details, order history, with links to detailed order confirmation, and profile management options

### Update Profile Page
Offers a form for updating the user profile, including image selection, order history review, and navigation options

### Super User - Product Management
Includes options for adding, updating, and deleting products

### Footer
Visible on all pages, featuring a free delivery banner


## Security Features and Defensive Design

### User Authentication
User authentication is applied to protect user data and prevent unauthorized access. During registration, users create a unique username and a strong password, following stringent security requirements. The login process securely verifies these credentials.

### Form Validation
Should a form be submitted with incorrect or missing information, it will not proceed, and the user will receive a notification identifying the field that triggered the error.

### Database Security
The env.py file securely stores the database URL and secret key to safeguard against unauthorized database access, a setup established prior to the initial push to GitHub.

To enhance site security, Cross-Site Request Forgery (CSRF) tokens have been implemented across all forms.

### Error Page
404 - Page Not Found error page was created to guide them back to the site.

![404-Error](docs/web/404.png)


## Database Design
### Entity Relationship Diagram
 ![](docs/erd.png)


### Custom Models
#### Wishlist & WishlistItem Models

In this Django application, I have developed two custom models designed to manage user wishlists and the items within them. These models are integral to a system that includes user profiles and product catalogs, aiming to provide a seamless e-commerce or retail experience.

**Wishlist Model**

The Wishlist model serves as a container for a user's desired products, enabling them to save items they are interested in purchasing at a later time. Each wishlist is linked to a user's profile and can be named for easy identification. The key features of the Wishlist model include:

User Association: Each wishlist is connected to a specific user profile, ensuring personalized wishlists for each user.
Name: Users can give their wishlist a name, making it easier to manage and access.

**WishlistItem Model**
The WishlistItem model represents individual items saved within a wishlist. This model allows users to add products from the product catalog to their wishlists. The key attributes include:

Wishlist Association: Each item belongs to a specific wishlist, which aids in the organized management of wishlist items.
Product Reference: Items within a wishlist are directly linked to products from the product catalog, making it easy for users to access product details and purchase options.
These models are crucial for creating a user-friendly e-commerce platform, enhancing the shopping experience by allowing users to curate and manage lists of items they wish to purchase.

#### Newsletter and Subscriber Models
**Newsletter model**

The Newsletter model is designed to create and manage newsletters within the application. Each newsletter includes a title, content, and an optional image. The created_on field automatically records the time when a newsletter is created. This model is essential for distributing information, updates, or promotional content to subscribers.

Attributes:

title: The title of the newsletter, allowing up to 200 characters.
content: The main body of the newsletter, stored as text.
created_on: The date and time when the newsletter was created, automatically set upon creation.
newsletter_image: An optional image for the newsletter, enhancing its visual appeal.

**Subscriber Model**

The Subscriber model keeps track of individuals who subscribe to receive newsletters. It includes the subscriber's email, name, and a unique identifier. The email field is unique for each subscriber, ensuring that each email address is only registered once.

Attributes:

email: The email address of the subscriber, used as a unique identifier.
name: The name of the subscriber.
identifier: A unique UUID for each subscriber, generated automatically and not editable, serving as the primary key.
These models together facilitate a straightforward yet effective system for managing newsletter subscriptions and distributing content to a list of subscribers.


#### Other models
The code used for the following models are taken from CodeInstitute Walkthroughs "I think, therefore I blog" and "Boutique Ado Walktrhough" and are slightly modified.

**Product Model**

The Product model was taken from Code Insistute Boutique Ado Walktrhough, and slightly altered. The model now includes artist and is_print attributes, providing a distinction between original artworks and prints. This adjustment allows users to filter products based on whether they are original paintings or prints. Furthermore, for prints, users can select the type of print paper from options such as Japanese Washi, Cotton Rag, Bristol Paper, and Photo Paper, enhancing customization and user choice.


**About Model**

The About model is crafted for the "About Us" section, providing a space to share details like the section's title, content, and an associated image. The updated_on field captures the last update timestamp, ensuring the section remains current. A default image can be used if none is specified.

**ContactRequest Model**

The ContactRequest model manages incoming messages through a contact form, recording the sender's name, email, and message. A boolean field, read, indicates whether the message has been reviewed. This setup streamlines communication, allowing for efficient tracking and response to inquiries.
Additionally, there are minor alterations to some of the other models.

## Technologies

### Language
* HTML5 - Provides the content and structure for the website.
* CSS - Provides the styling for the website.
* Python - Provides the functionality for the site.
* Django - Used as the Python framework for the website.
* Javascript - Used to add card payment, country field, sorting products, back to top click function, update the item quantity, and remove the item from the shopping cart


### Systems
- **Git**: A version control system for tracking changes in computer files and coordinating work on those files among multiple people. [Git](https://git-scm.com/)

- **AWS S3 and IAM**: Amazon Ib Services (AWS) provides cloud computing services. S3 (Simple Storage Service) is for storage, and IAM (Identity and Access Management) is for managing access to AWS services securely. [AWS S3 and IAM](https://aws.amazon.com/)

### Frameworks
- **Django**: A high-level Python Ib framework that enctheages rapid development and clean, pragmatic design. [Django](https://www.djangoproject.com/)
- **Bootstrap**: A front-end framework for developing responsive and mobile-first websites. [Bootstrap](https://getbootstrap.com/)

### Libraries
- **Psycopg2**: A PostgreSQL adapter for Python. [Psycopg2](https://pypi.org/project/psycopg2/)
- **Gunicorn**: A Python WSGI HTTP Server for UNIX, used to run Python Ib applications. [Gunicorn](https://gunicorn.org/)

### Programs and Services
- **GitHub**: An online platform for hosting and sharing code repositories. [GitHub](https://github.com/)
- **GitPod**: A cloud-based Integrated Development Environment (IDE) that provides a complete dev environment for GitHub projects. [GitPod](https://www.gitpod.io/)
- **ElephantSQL**: A cloud-based PostgreSQL database service. [ElephantSQL](https://customer.elephantsql.com/login)
- **Prycopg2**:Used as a postgres database adapter. [Psycopg2](https://pypi.org/project/psycopg2/)
- **Gunnicorn**: Used as a website server provider. [Gunicorn](https://gunicorn.org/)
- **Heroku**: A cloud platform service that enables developers to build, run, and operate applications entirely in the cloud. [Heroku](https://id.heroku.com/)
- **Stripe**: A payment processing platform for handling secure payments. [Stripe](https://stripe.com/ie)
- **XML-Sitemaps**: A tool for generating website sitemaps. [XML-Sitemaps](https://www.xml-sitemaps.com/)
- **Privacy Policy Generator**: An online tool to generate privacy policies for websites. [Privacy Policy Generator](https://www.privacypolicygenerator.info/)

### Additional Tools
- **Balsamiq**: A wireframing tool for designing user interfaces. [Balsamiq](https://balsamiq.com/)
- **LucidChart**:diagramming tool used for creating ERDs (Entity-Relationship Diagrams). [Lucidchart](https://lucidchart.com)
- **AmIresponsive**: A tool to check how responsive a website is on different devices. [AmIresponsive](https://ui.dev/amiresponsive)
- **Favicon**: A tool for creating favicons (the small icons that appear in the tab of a Ib browser). [Favicon](https://favicon.io/)
- **Google Chrome DevTools**: A set of Ib developer tools built directly into the Google Chrome browser. [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- **HTML Validation Service**: A tool to check the markup validity of Ib documents in HTML. [HTML Validation](https://validator.w3.org/)
- **CSS Validation Service**: A service to check the validity of Cascading Style Sheets (CSS). [CSS Validation](https://jigsaw.w3.org/css-validator/)

- **CI Python Linter**: A Code Insitute tool to validate Python. [CI Python Linter](https://pep8ci.herokuapp.com/)
- **JSHint**: A tool to validate JavaScript. [JSHint](https://jshint.com)

- **Lighthouse**: An open-sthece, automated tool for improving the quality of Ib pages. [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)


## Testing
Full testing can be seen in [TESTING.md](https://github.com/TESTING.md) file.
/////
responsive testing
browser compatability
bugs resolved and unresolved
lighthouse tesing
code validation
user stories testing
feature testing
### Bugs

## Deployment

### Heroku
- Create an account or log in to **Heroku**.
  - On the dashboard, click on **"New"** and select **"Create new app"**.
  - Give the app a unique name and select the region closest to you. Then click **"Create app"** to confirm.
- To create a new database accessible by Heroku, create an account or log in to **ElephantSQL**.
  - Click **"Create New Instance"**.
  - Set up ythe plan by giving it a name and choosing the **"Tiny Turtle (free)"** plan.
  - Select the Region and data center closer to you, then click **"Review"** and confirm by clicking on **"Create instance"**.
  - Return to the ElephantSQL dashboard and click on the database instance name for this project.
  - In the URL section, click the copy icon to copy the database URL.
- Install the plugins `dj-database-url` and `psycopg2-binary` in the terminal.
  - Run `pip3 freeze > requirements.txt` so both are added to the `requirements.txt` file.
- Create a **Procfile** in the root directory, adding `Ib: gunicorn ytheapp.wsgi:application`.
- Run the migration command in ythe terminal to migrate ythe database structure to the newly-connected ElephantSQL database: `python manage.py migrate`.
- Run `python3 manage.py createsuperuser` to create a superuser.
- Load the `.json` files for categories and products.
- Install `gunicorn` (`pip install gunicorn`) and add it to the `requirements.txt` file using the command `pip3 freeze > requirements.txt`.
- In `ALLOID_HOSTS`, add the Heroku app and localhost to the list: `ALLOID_HOSTS = ['HEROKU_APP_NAME.herokuapp.com', 'localhost']`.
- Add a config variable by typing `DISABLE_COLLECTSTATIC = 1`.
- Connect Heroku to the GitHub repository and enable automatic deploys.
- Deploy the app and access the website.

### Stripe
- Sign up for a Stripe account.
- Navigate to the **Developers** tab, then to the **API** area and retrieve ythe publishable and secret keys.
- Incorporate `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` into `settings.py` and into ythe Heroku configuration, using the information from the API section.
- Proceed to the **webhooks** area to establish a new webhook.
- Select the option to display all events and specify ythe endpoint.
- Incorporate `STRIPE_WH_SECRET` into both ythe environment variables and Heroku setup.

### AWS
- Sign up for an account on the **AWS Management Console**.
- Navigate to **S3** and initiate a new bucket creation.
- Configure the bucket settings, including static hosting, CORS configuration, and bucket policy for access and permissions.
- Proceed to **IAM** to establish a new group.
- Develop a Policy tailored for this group's permissions.
- Generate a User and associate it with the group and policy created earlier.
- Upon creating the User, download the CSV file from the User's profile, which includes the user's access key ID and secret access key.
- Implement `boto3` and `django-storages` in ythe project, then update the `requirements.txt` file with these dependencies.
- Integrate AWS service variables into `settings.py` to link ythe application's static storage with AWS.
- Create a dedicated media folder within ythe project structure to organize all media files for storage on AWS.

### Forking repository
- Forking enables you to create a personal copy of an existing repository on a remote server. To do so with the specified repository:

- Navigate to the **[repository](https://github.com/aslinedvinsson/Artzy.git)**  on GitHub.
- Click on the **"Fork"** button located at the top right corner of the page.
- This action will generate a copy of the repository under ythe own GitHub account.

### Cloning repository
- Cloning creates a local version of a repository, maintaining a connection to the original sthece. To contribute modifications to a repository you have access to, begin with cloning before applying changes and pushing them:

- Navigate to the **[repository](https://github.com/aslinedvinsson/Artzy.git)** on GitHub.
- Click on the **"Code"** dropdown menu and choose ythe cloning method: **HTTPS**, **SSH**, or **GitHub CLI**, then copy the URL provided.
- Open a **Terminal** window.
- Change to the directory where you wish the cloned repository to be located.
- Type `git clone`, folloId by the URL you copied in the previous step.
- Hit enter to execute the cloning command, creating a local copy of the repository.


## References and Credits ////
//////boutique Ado boilerploate

    <!-- Footer Inspired by https://mdbootstrap.com/docs/standard/navigation/footer/-->↩
additional tutorials
media and content used for educational purpose

### Disclaimer
The content available on this site is solely for educational purposes and should not be interpreted as professional advice.
