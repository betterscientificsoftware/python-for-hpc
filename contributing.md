## How to Contribute Content to the Python in HPC community website

We are interested in any contributions that may be useful to other members of the community, including, blogs, tutorials, example notebooks, and useful links to content or software.

Blogs, tutorials and notebooks can be found under the _posts, tutorials and notebooks directories respectively.

To contribute, you have the following options.


### 1. Send me the content at shudson@anl.gov

If you send me content, we can iterate as necessary and I can add to the site. Feel free to ask questions if you are not sure whether it's a good fit.

Most of our articles are in markdown format, but I am happy to take plain text and format it. 

If you have suggested links, it is helpful to provide brief descriptions (sentence or two or three) on what it is, and in the case of software links, the unqiue feature/benefit.


### 2. Fork repository and make pull request.

I am happy to take pull requests.

*Example: Adding a blog.*

Take an article from the _posts directory to use as a template.

The file should be in markdown format and named with the same YYYY-MM-DD-<ARTICLE_NAME> format.

Modify the front matter (at the top between the ---). We can help with this as required. Note that by default author_profile is set to True. We can [add an author profile for you](#author-profiles), with optional picture. Otherwise "author_profile: False" can be added to the front matter. Tags can be anything and will help with searches. The excerpt field should also help google to directly find your article in searches.

### Author Profiles

If would like an author profile, please provide details as in the following example (you can email me the photo if you want one - shudson@anl.gov). All but name is optional. We can also add fields (eg. twitter). Note, this goes into _data/authors.yml.

  name             : "Joe Blogs"  
  avatar           : "images/my_photo.jpg"  
  bio              : "Software Developer at Argonne"  
  location         : "Illinois, USA"  
  email            : "whatever@gmail.com"  
  github           : "myusername"  
  linkedin         : stephen-hudson-787844145  

