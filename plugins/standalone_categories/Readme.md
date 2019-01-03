# Standalone Categories

A [Pelican](http://blog.getpelican.com/) plugin that will remove specified categories out of the "normal" blog workflow. These categories will not appear in your regular blog's _Categories_ page, and the articles in them will not be created during normal article processing. For each of these special categories, a separate list page will be created using a template you choose, and every article in that category will be created with a specified template. This allows you to have a different look and feel for one or more categories.

I wrote this plugin because I wanted a couple categories that had thumbnails on the article list page and that were separate from the main blog posts. You can see the results on my site [eskimospy.com](http://www.eskimospy.com): the _Work_ and _Projects_ pages and the articles in them were handled by this plugin. 

## How To Use

In your `pelicanconf.py` create a `STANDALONE_CATEGORY_PAGES` setting that is a list of categories you want special treatment for. Each item in the list is a dict that defines the category name via the `category_name` key, what template to use for the category list page via the `page_template` key, and a template to use for the articles in that category with the `article_template` key. See the example!

Each of the custom category pages, and each custom article page has access to all the same properties as your normal `article` and `category` templates. Each of the custom template files you use will need to exist in your theme's `templates` directory alongside all the standard ones.

## Example

In `pelicanconf.py`:

    PLUGIN_PATH = "plugins"
    PLUGINS = ['standalone_categories',]

    STANDALONE_CATEGORY_PAGES = [

        {
            'category_name': 'Work', 
            'page_template': 'project_list_page',
            'article_template': 'project_article'
        },

        {
            'category_name': 'Painting', 
            'page_template': 'artwork_list_page',
            'article_template': 'artwork_article'
        },
    ]

In your theme folder:

    your_theme/
        templates/
            artwork_article.html
            artwork_list_page.html
            project_article.html
            project_list_page.html

This will pull any articles in the __Work__ and __Painting__ categories from the blog proper and create two category pages, `work.html` and `painting.html`, that use the templates `project_list_page.html` and `artwork_list_page.html` respectively. All the articles in the __Work__ category will then be created with the `project_article.html` template, and all __Painting__ posts will be created with the `artwork_article.html` template.
