
<img width="50%"  alt="Project Logo" src="https://raw.githubusercontent.com/Devihem/Fruitipedia_Django_Project/master/assets/images/logo.png" />

## Django Project - Workshop from SoftUni

**This repository provides a Django project for a workshop on Python ORM at Software University. The project, named "fruitipedia" includes preset HTML pages and CSS files. The workshop tasks are detailed in this document, covering project setup, database models, routes, views, and template inheritance.**

- [x] Skeleton: 
  - All required HTML pages and CSS files for the project are provided.
- [x] Setup:
  -  Create a new Django project called "fruitipedia"
  -  Create an app within the project named "fruits."
  -  Configure project settings, add templates and static files.

- [x] Database: Define two models: Category and Fruit.
  -  Category model with a unique character field "name."
  -  Fruit model with character fields "name," "image_url," "description," and optional "nutrition."
- [x] Routes:
  - Define URLs for various pages, including index, dashboard, create-fruit, details-fruit, edit-fruit, delete-fruit, and create-category.
- [x] Views:
  - Implement views for handling HTTP requests, including index, dashboard, create-fruit, details-fruit, edit-fruit, delete-fruit, and create-category.
- [x] Fruits App URLs:
  - Create an urls.py file in the "fruits" app directory to define URL patterns for the app.
- [x] Template Inheritance:
  - Implement a base.html template in the common directory, containing common elements like header, navigation, and footer.
  -  Extend this base template in other templates using {% extends 'common/base.html' %} and define specific content blocks.
- [x] Pages Edit:
  - Add specific futures to the pages: Index, Dashboard, Create Category, Create Fruit, Details Fruit, Edit Fruit, Delete Fruit.


**Custom futures that may be added:**

- [ ] Add a ready to use database for at least 100 fruits
- [ ] Dynamic wallpaper to the main page
- [ ] Change the color scheme of the project
- [ ] Search bar for fruits by name
- [ ] Add small game based on fruits
- [ ] Change the logic of "Category" it makes no sense as it is.
- [ ] Background music if possible
