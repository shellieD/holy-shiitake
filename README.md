# Holy Shiitake!!! 

Holy Shiitake is a website dedicated to sharing, creating and interacting with vegan recipes.  Whether you are vegan, a vegetarian looking to reduce your dairy intake, or are looking for something different to add to your recipe repertoire, Holy Shiitake is the place to be!

Browse through the recipes already added to the site for a bit of inspiration, or if you are a seasoned vegan, share your recipes with others to help get them on the 'band-wagon'!

(Am I Responsive screenshots here)

Visit the live site here:

Holy Shiitake has been built using the Django framework in Python.

## User Experience (UX)

### User Stories

### Design

#### Color Scheme

#### Typography

#### Imagery

#### Wireframes 

#### Database Schema

likes - many to many



![Database Schema](docs/images/databaseschema.png)

#### Features

##### Navigation Bar

##### Footer

##### Add more features here...

#### Future Features

## Testing

### Bugs

When adding functionality to allow users to add comments to recipes, the user was able to post one comment, however if they were to comment on another post an error would display saying the user already existed.  Through debugging I noticed that when setting up the comments model, I had used unique=True in the name field.  This meant that the user could only ever comment on one recipe.  To fix this, I simply removed unique=True and migrated the changes to the database.  This fixed the error and users can now comment multiple times on multiple recipes.  

## Technologies 

### Languages

### Libraries/Frameworks

## Deployment

## Credits

Image by <a href="https://pixabay.com/users/pasja1000-6355831/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4581877">pasja1000</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4581877">Pixabay</a>