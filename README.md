# FSDI 112 - Blog
This project presents a page based off a local newspaper. It has a home page, an about page, it presents posts in a list page and you're able to create new posts as well.

## Heroku
https://aqueous-taiga-52238.herokuapp.com/
https://git.heroku.com/aqueous-taiga-52238.git

## Mini Challenge 1 (class 4)

## Blog project

Using what we've learned in class 1, 2 and 3, let's create and configure a new project:

1. The project directory should be `blog`.
2. There should be a configuration folder within it named `config`.
3. Apps for `pages` and `posts` should exist.
4. All apps should be installed.
5. A home page.
6. An about page.
7. Using the model provided below, add support for:
    7.1. Creating new posts.
    7.2. Listing all posts.
    7.3. Viewing a detail view of a post by specifying their ID.
8. Add bootstrap and a navbar.
9. Add static files.

### Note: Your project must be based on a real or fictional newspaper.

#### Model:

```
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('YOUR_DETAIL_URLPATTERN_NAME', args=[self.id])

```