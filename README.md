<h1 align="center">
  <a href="http://reuse-gang.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/vYK0KB8/Screenshot-2020-03-10-at-1-14-15-AM.png" target="_blank" alt="Multi Device Mockup"/></a>
</h1>

<div align="center">
<a href="http://reuse-gang.herokuapp.com/" target="_blank"><img src="https://i.ibb.co/4ZfmYSJ/logo-2.png" width='200' height='150'target="_blank" alt="Reuse Gang logo"></a>
</div>

## Table of Contents

* [Introduction](#introduction)
* [How?](#how)
* [UX](#ux)
    * [Strategy: Why and what?](#why-and-what)
        * [1. Primary target audience](#1-primary-target-audience)
        * [2. Who is the project for?](#2-who-is-the-project-for)
        * [3. What are the main goals?](#3-what-are-the-main-goals)
        * [4. What are the goals and needs of the user?](#4-what-are-the-goals-and-needs-of-the-user)
        * [5. What are the goals and needs of the business?](#5-what-are-the-goals-and-needs-of-the-business)
        * [6. Research](#6-research)
        * [7. Planning](#7-planning)
        * [8. User Stories](#8-user-stories)
    * [Scope plane: How?](#scope-plane-how)
    * [Structure plane: Organisation and functionality](#structure-plane-organisation-and-functionality)
        * [1.Existing Features](#1-existing-features)
        * [2.Features Left to Implement](#2-features-left-to-implement)
    * [Skeleton plane: Presentation and navigation](#skeleton-plane-presentation-and-navigation)
        * [1. Wireframes](#1-wireframes)
    * [Surface: Design](#surface-design)
        * [1. Color Scheme](#1-color-scheme)
        * [2. Font](#2-font)
        * [3. Logo](#3-logo)
* [Testing](#testing)
* [Technology Used](#technology-used)    
* [Deployment](#deployment)
* [Credits](#credits)
    * [Special Thanks & Acknowledgements](#special-thanks--acknowledgements)

# Presentation of the project
I am very engaged with a local zero waste group and have been part of a freecycle network. So I felt drawn to build a platform where people want to give for free, an unwanted item. A platform where the free item can be taken by another person that needs it. A free and user-friendly platform where exchange happens.

[Back to Top](#table-of-contents) 

# UX
## Strategy plane: Why and what?

### 1. Primary target audience

General people, probably more from a local community. People who are already concerned about planet and environment and want to be part of a community of exchange

### 2. Who is the project for?

A local town or community where people can exchange easily their items. The project can be promoted and managed by a local zero waste association run by volunteers.
  
### 3. What are the main goals?

- A platform where people want to give for free, an unwanted item 
- A platform where the free item can be taken by another person that needs it
- A very simple and user-friendly platform where exchange happens effectively and that does not turn away people

[Back to Top](#table-of-contents) 

### 4. What are the goals and needs of the user?

- A user wants to either give away a used but now unwanted item
- A user needs an item and would be interested to have one already used before
- Both users want to be able to do the exchange without much stress and complexity
- Need for an efficient and quick exchange while having the beautiful opportunity to have human contact
- Users might also want to get more information about the organisation or network so they might engage

### 5. What are the goals and needs of the business?

- To use the online platform to promote and help reuse and recycle within its members
- To have an online easy platform to use with a unique and beautiful design to attract REusers...
- To raise awareness among the larger community that giving away and REuse is fun, cool and trendy!
- To encourage community exchange which is started online but often continue within the community by more engagement
- To have local charities and charity shops participating by either giving away or taking used items
- To have less items being thrown away and less consumption
- To follow up with community events related to freeREuse like Clothes Swap for adults or kids, repair cafes
- While the platform being promoted locally, the goal of organisation would be to expand its geographical engagement

[Back to Top](#table-of-contents) 

### 6. Research

#### Who else is building this?
- [Information page about Freecycle concept](https://freecycle.net/)
- [Global and main website where free exchange happens](https://www.freecycle.org/)
- [Local free exchange website](https://www.freetradeireland.ie/)
- [FreeUse website](http://www.freeuse.org/)
- Any Facebook page that offer this type of free items exchange: people who want to give away send a Facebook post on the page. Since no record of available items anywhere, other users would need to scroll down on Facebook page to find old posted items

#### How are they doing it?
- An information page about Freecycle network and concept of reuse, recycle for free, explaining the best practices of being a local network member
- Global network has hundreds of smaller groups where you become a member before you can view posts
- To add item, member has to send post to offer item and send another post to want item
- Post is sent to server via a form with dropdown options of offering or searching, group location, brief description, more precise location of member, text area for more description. Image can be attached to post
- Once published, the member can manage his posts to edit, cancel and delete it or mark it as gone and delete it
- Post is then published to the group by order of latest published
- User login system 
- All items showing as card
- Search option by user type (household, business, school) and then refined search by item category. 
- User can also search by item name and location. 
- Map added to show user location 
- Item owner contact details only showing to user if logged in.
- Can view all items posted by same user.

[Back to Top](#table-of-contents) 

#### What are the pros of what they are doing?
- User login system
- I like the idea of only showing contact details of item owner when other users are logged in, for privacy reasons.
- Responding to a post about a given item directly send email to item owner and all further contacts are done privately. Not sure if I can do it using my acquired knowledge so far.
- Having an extra page where users can find more information about the concept and history of the free reuse movement.
- An interactive map showing the location of the user as shown on the item being given away
- Search option by categories and location
- Rules for using the network and offering or wanting items
- Having a moderator
- Non-liability disclaimer of the network advising its members that  they use groups at their own risk and to watch their personal information and security when exchanging an item

#### What could they do better?
- On one website, to make sure items are removed once taken away
- Improve responsive design of one website
- Add search option with different categories on one website
- Decluttering the heavy content which is not useful to the users
- Moderator on one website, no moderator or rules on other website

[Back to Top](#table-of-contents) 

### 7. Planning

#### What relevant content should we deliver that fits our demographic?
- Quick description of the idea/concept
- About/information page about organisation/network and idea/concept behind website
- List of items being given away and available for taking: including image
- A search option with 4 drop down menu of different categories
- A button to sign up/log in
- A button to add item to be given away
- A button to want used item
- A button where to find user’s existing posts and where it can be edited or deleted
- Form to add item with 5 fields: To offer or to want, Item name, Item description, is or not urgent
- Form to edit or delete a post with used item

#### How can we make the content easily tracked and catalogued in an intuitive way?
Using database with clear collections and categories

#### Is the technology known and used appropriate? 
- JS will be used for all interactive movements and click of users
- Python will be used as syntax to fetch and send information between front-end and database
- Flask will be used to add information on html using templating language 
- the data will be recorded and rendered using MongoDB, noSQL database.

[Back to Top](#table-of-contents) 

#### Why are we so special? What additional value will it add to what is existing?
- Belongs to a specific local community vs global
- Run by a local organisation already engaged in the community
- Fun and trendy way of exchanging items compared to charity shops
- Clear and brief information about concept with links to other websites if needed
- Quick and easy to search and view available items before signing up
- Quick and easy to log in, add an item, edit it, delete it
- Nice and clear UX design

[Back to Top](#table-of-contents) 

#### Importance and feasibility table:
| Goals and features wanted                                        | Importance | Feasibility |
|------------------------------------------------------------------|------------|-------------|
| Page about concept behind website                                | 4          | 5           |
| User login allows all CRUD                                       | 5          | 3           |
| List of items showing as cards                                   | 5          | 5           |
| Search option with categories                                    | 5          | 4           |
| Non-Liability disclaimer, Rules                                  | 4          | 2           |
| Map showing item’s location (once network grows)                 | 3          | 3           |
| Links to organisation website and Facebook page for more contact | 3          | 5           |

### 8. User stories

#### As a user, I am expecting:
* A welcome or about section so I can understand what the website is about
* A logo on top left corner where I can click and go back to home page
* All items available displayed on the home page when I first land
* A special page where I can find my own items
* A search bar to filter specific items depending of a category or other common factors (user, location)
* A quick view about the item with an image
* The location of the item so I know if close enough to where I am located
* An option to see more details with only one click
* To email item owner if I need item
* Add button to offer an item on the home page
* If not logged in, expecting to be sent to log in form when I want to add an item
* An edit button to update any details
* A place where I can delete the item to show it has been taken
* A register button if I am not a member
* An error message if my username or email address is already in database
* A message to confirm I am successfully logged in or if password is wrong
* A button to log out
* A footer where I can find links to the associated organisation and to the developer's professional pages

#### As a developer, I want:
* Design and develop a webiste to show my knowledge of Flask, Python and MongoDB
* Match up my interest of environment-friendly, zero waste with my coding skills
* Make contact with local organisations to offer my skills and maybe get more practice with other projects, free at the beginning, then paid

[Back to Top](#table-of-contents) 

## Scope plane: How?

### 1. Existing Features:
* Feature 1 - List of items showing as cards
* Feature 2 - Search option with categories
* Feature 3 - Simple register/login feature for users
* Feature 4 - User can add an item to give away by filling a form (CREATE) with name, description, image, location, category of items
(Kids, clothes, home, books, others)
* Feature 5 - User can edit an item card by updating its details (UPDATE)
* Feature 6 - User can remove an item by marking it as taken (DELETE)
* Feature 7 - Logo on the top left linking to home container at any moment which would reload the whole page
* Feature 8 - Minimalist navigation in the shape of spinner instead of burger, minimalist, which gives 4 options: home, about, member page and login/logout
* Feature 9 - About section with gang statement above footer which can be accessed via the navigation

### 2. Features Left to Implement:
* Using Javascript to handle register, log in and log out
* A full 'about' page to have more information about a registered charity or organisation which would be managing the gang locally
* A form modal to send email to item owner directly from the website and store messages in the database
Although the website was actually live tested by a person not knowing about educative aspect of project and I receive emails from her regarding the items. So mailto implementation was tested and work well.
* For the purpose of milestone project, I have functionality of deleting item but for user experience, it would be better to have taken items saved in an archive section of the website so that members can re-use them later if needed
* Adding a date generator when item is created and store as key of object
* A switch button which member can choose to use in order to confirm if item still available after a certain time
* Adding a filter by location and maybe by date added
* Non-Liability disclaimer, Rules
* Network page to offer partnership with schools, charities when they need used items
* Business page for businesses who also would like to donate items or fund the page to reduce their waste and increase their local visibility
* A page on upcycling tips which members can share or any upcoming workshops organised locally

[Back to Top](#table-of-contents) 

## Structure plane: Organisation and functionality?

### 1. Organisation of functionality and content
a) One main page: find quick and useful information, log in and contact others
- From main page, user can view list of available items where necessary information is showing
- From main page, user can log in on modal and be re-directed again to main page with available items
- From main page, user can view each item, toggle down separate sections (image, description, contact…)
- From main page, user can click on contacting item owner which throws a modal to write and send email
- From main page, user can click to view his profile or his latest posts

b) User page: separated to avoid too much information on the same page and mixing different information
- User does not need to visit his user page at each visit, might only be for updating details or items given
- User can update or remove given items

[Back to Top](#table-of-contents) 

### 2. Data structure
Data model with two collections where User Name creates relationship between collections

#### Users
| Title         | Form Identifier key | Type     | Form collection   |
|---------------|---------------------|----------|-------------------|
| User ID       | _id                 | ObjectId | automatic         |
| User Name     | user_name           | string   | input             |
| User Email    | user_email          | string   | input             |
| User Password | user_pwd            | string   | input and hashing |

#### items

| Title            | Form Identifier key | Type     | Form collection |
|------------------|---------------------|----------|-----------------|
| Item ID          | _id                 | ObjectId | automatic       |
| Username         | username            | string   | input           |
| Item Name        | item_name           | string   | input           |
| Item Description | item_description    | string   | input           |
| Item Image       | item_img            | string   | input           |
| Item Category    | item_category       | string   | input           |

[Back to Top](#table-of-contents) 
	
## Skeleton plane: Presentation and navigation? 
### 1. Wireframes

I used Balsamiq tool for the wireframes and attached them to the directory in assets. 

- [Home page on desktop](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/Home-desktop.png)
- [Home page on mobile](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/Home-mobile.png)
- [Home page on tablet](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/Home-tablet.png)
- [Login modal on desktop](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/Home-login-desktop.png)
- [Login modal on tablet](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/Home-login-tablet.png)
- [Login modal on mobile](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/Home-login-mobile.png)
- [User page on desktop](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/User-desktop.png)
- [User page on tablet](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/User-tablet.png)
- [User page on mobile](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/User-mobile.png)
- [Edit post on desktop](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/User-editpost-desktop.png)
- [Edit post on tablet](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/User-editpost-tablet.png)
- [Edit post on mobile](https://raw.githubusercontent.com/mkuti/reuse_gang_project/master/wireframes/User-editpost-mobile.png)

[Back to Top](#table-of-contents) 

## Surface plane: How does it look like?
### 1. Color scheme
As the platform is about less waste. recycle, planet-friendly, it was natural for me to have the main color represented by green. From there, I use Color Scheme to find complementary colors which are different shades of green to a very light one for the text and the body background color. Also used a dark grey for text in other parts in order to contrast with the darker green color.

### 2. Font
#### Cabin Sketch
- I have decided to use Cabin sketch font as it represented the opposite of permanent, which could mean the writing could be rubbed and written again. This thematic of non-permanent, flowing, ephemere, to me fitted particularly well with the website thematic of re-use. It also gives a look of chalk written which is planet-friendly material.
- Cabin sketch became my primary font as it is used for the logo and for the attention text of the home page so it gives an atmosphere of the website to the user on first visit.

#### Indie Flower
- I chose Indie Flower font as I am very attracted to cursive writing and again, it represents the simple gesture of hand-writing, which is the opposite of permanent. It is easy to read and gives a friendly atmosphere of exchange. Is also consistent and complimentary of the other font chosen.
- It is used as main font for the body.

### 3. Logo
I wanted the logo to be simple and effective, showing the thematic and atmosphere of the website to the user. Used my primary font of chalk style and removed background so it falls nicely on the home image.

### 4. Image
It took me a long time to find the perfect image which compliment the logo, the colors and the fonts and does not take too much from the rest of the website content. It matches perfecly the colors thematic and gives a friendly welcome to the website users.

[Back to Top](#table-of-contents) 

# Testing

I created a separate document for Testing writeup which can be found [here](https://github.com/mkuti/reuse_gang_project/blob/master/test.md)

[Back to Top](#table-of-contents) 

# Programming languages and technologies Used
- [GitPod](gitpod.io) - I used __GitPod__ as my IDE for the development of this website.
- __HTML__ language is used to create the structure of the website and game.
- __CSS__ language is used to add styling on the structure of the website.
- [BootstrapCDN](https://www.bootstrapcdn.com/) - The website is using __Bootstrap4__ as the basic structure and grid of the website and to increase the responsiveness of the website.
- [jQuery](https://jquery.com/) and [Popper.js](https://popper.js.org/) - The website uses __jQuery__ and __Popper.js__ to bring in Javascript which makes the navbar responsive
- __Javascript__ functioning language is used to fetch external data and add interactivity on the website so the game functions based on user's actions
- [jQuery](https://jquery.com/) - I used jQuery to avoid repeating same actions on the DOM when buttons were clicked
- __Python__ Object-oriented programming and structured programming language which allows smooth communication between the backend and frontend. 
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - I used Flask framework, Jinja templates and Werkzeug to 
Python werkzeug.check_password_hash()
- [FontAwesome](https://kit.fontawesome.com/f7e192f540.js) - The website is using __Font Awesome__ to display the social media icons in my footer
- [Google Fonts](https://fonts.google.com/)- The website uses __1 Google font__- Url imported in CSS
- [AutoPrefixer](https://autoprefixer.github.io/) - I have used __AutoPrefixer__ to make sure the css code worked on all browsers
- [Tiny.jpg](https://tinyjpg.com) - I have used __Tinyjpg__ to compress logo image of the website to increase the website loading on browser
- [ColorSpace](https://mycolor.space) - I have used __ColorSpace__ to find matching colors for the website
- [Balsamiq](https://balsamiq.cloud) - I have used __Balsamic__ to build the wireframes which I then exported to the IDE
- [Favicon converter](https://favicon.io/favicon-converter/) - I used Favicon converter to convert the logo into a favicon which I was able to insert in the asset folder and I tested it to be working
- [Sweetalert2](https://sweetalert2.github.io/)
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) Chrome extension to show content structure, margin and paddings and fix any offset
- [Lunapic](https://www2.lunapic.com/editor/) - to make the logo transparent
- [Spinkit](https://tobiasahlin.com/spinkit/) - for the loader css and html
- [Techsini Multi-Mockup](https://techsini.com/multi-mockup/index.php) - to create multi-device photo of README
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables#) for generating Markdown tables for README


[Back to Top](#table-of-contents) 

# Media and Content origin
1. Taglines: [BrandonGaille](https://brandongaille.com/list-45-catchy-recycling-slogans-and-great-taglines/)
2. [Home background by Min An from Pexels](https://www.pexels.com/photo/green-leafed-plants-1650035/)
3. Photos used for test items
- [Photo of printer by Fernando Arcos from Pexels](https://www.pexels.com/photo/black-sd-card-adapter-on-white-device-193057/)
- [Photo of garden tools by Nastya Kvokka on Unsplash](https://unsplash.com/photos/vdD1rcsdL3E)
- [Image of pink bike by Isa KARAKUS from Pixabay](https://pixabay.com/photos/bicycle-child-baby-kids-bike-1713165/)
- [Photo of baby clothes by Chloe Amaya from Pexels](https://www.pexels.com/photo/white-and-blue-textiles-2252000/)
- [Image of slide by nlachmund from Pixabay](https://pixabay.com/photos/slide-play-kids-playground-1016832/)
- [Image of glass jar by Devanath from Pixabay ](https://pixabay.com/photos/glass-containers-glass-empty-clean-1205611/)
- [Image by Susanne Jutzeler, suju-foto from Pixabay](https://pixabay.com/photos/bike-child-children-cycling-wheel-2895424/) 
- [Image by Attraction Magazine from Pixabay](https://pixabay.com/photos/beads-lilac-fashion-design-jewels-809385/)

[Back to Top](#table-of-contents) 

# Deployment
I have been using the Integrated development environment (IDE) [GitPod](gitpod.io) to develop this milestone project.
As I used it for the first time and Code Institute changed the preferred IDE for the whole course, I was lucky to avail of the full template prepared by Code Institute at the time.

I went to Code Institute [full template repository](https://github.com/Code-Institute-Org/gitpod-full-template), cloned it and created my own repository with the template ready. From there, I opened GitPod which started a workspace.

From that point, I could add, commit any update of my code and push it to the remote repository so it could be regularly backed up and accessed by others.

### GitHub
All versions and branches of the code are stored in github:
https://github.com/mkuti/reuse_gang_project

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [GitPod](https://gitpod.io/)

The following **must be installed** on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
- If you use Code Institute template, all the above will be already installed
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine. 
    - How to set up your Mongo Atlas account [here](https://docs.atlas.mongodb.com/).

### Instructions
1. Install all required modules with the command 
```pip3 freeze -r requirements.txt```

2. In your local IDE create a file called `env.py`

3. Inside the env.py file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `reuse gang`, with 2 collections called `users` and `items`.

4. Make sure to add env.py to a .gitignore file so it's not pushed to the repository

4. You can now run the application with the command
```python app.py```

9. You can visit the website at `https://8080-fbbe19f1-c9cd-4b0b-9a9e-2d36c0dd3c88.ws-eu01.gitpod.io/`

## Heroku Deployment

To deploy Reuse Gang to heroku, you would need to follow the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.

[Back to Top](#table-of-contents) 

# Credits
* Code for the 404 error handling was taken from [Geeks for Geeks](https://www.geeksforgeeks.org/python-404-error-handling-in-flask/)
* Code provided by Simen Dehlin for the logo disappearing on window scrolling from my first milestone, via [Codepen](https://codepen.io/Eventyret/pen/RXBNaJ)
* Switch statement for JS function of filtering items so I would avoid adding if statement inside template literals kindly suggested by my mentor [Simen Dehlin](https://github.com/Eventyret)
* Idea of appending filtered html template from JS to existing component was inspired by [Anna Greaves](https://github.com/AJGreaves) from her milestone 3
* The solution to send json object from MongoDB to JS via Ajax was suggested by my mentor [Simen Dehlin](https://github.com/Eventyret) who also found the solution to json.dumps not working
* Code for the trick ```if (used_email or used_name) is None``` found on [Stack Overflow](https://stackoverflow.com/questions/19400115/python-difference-between-x-is-not-none-and-y-is-not-none-and-x-and-y-is-n)
* Code for adding attribute active to a page being rendered in Python was followed from [Anna Greaves](https://github.com/AJGreaves) Milestone 3

# Special thanks

To my mentor, [Simen Dehlin](https://github.com/Eventyret), for never being tired of my questions or despair when unsure or lost. For his amazing mentoring throughout the building of this project, encouraging, suggesting and pointing me to the right direction, by explaining the Javascript and Python logic but also explaining the professional expectations of a Python and Javascript developer. He encourages but always challenge for extra development which is great. Thank you!

To [Malia Havlicek](https://github.com/maliahavlicek) for testing extensively the website, its functionalities and for providing a very detailed feedback on the website but also the readme and code. It was very helpful to tackle some very important bugs.

To all in the #peer-code-review channel of Slack who were kind enough to provide their feedback and find bugs or provide solution.

To my two sons Léon and Seyi whose time with me is being sacrificed currently, for being patient with me when I am tired after sleepless nights.

##### Disclaimer:
The content of the website is for educational purposes only.

[Back to Top](#table-of-contents) 