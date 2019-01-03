"""
Standalone Categories
=====================

A Pelican plugin that will generate a special page for individual post
categories using a specified template, and remove articles from those
categories from the 'normal' blog workflow, and render them with a specified
template as well.

See the Readme.md file for a lot more information
"""
import time

from collections import defaultdict
from logging import warning
from functools import partial
from itertools import chain

from pelican import signals
from pelican.generators import Generator
from pelican.utils import slugify, process_translations


class StandaloneCategoryGenerator(Generator):
    """
    Creates a category page and article pages for each standalone category
    the user has defined in the STANDALONE_CATEGORY_PAGES settings.
    """
    def __init__(self, *args, **kwargs):
        super(StandaloneCategoryGenerator, self).__init__(*args, **kwargs)
        self.config = self.settings.get('STANDALONE_CATEGORY_PAGES', None)
        if not self.config:
            warning(
                "Missing STANDALONE_CATEGORY_PAGES configuration in settings."
            )

    def generate_output(self, writer):
        start_time = time.time()
        page_count = 0
        article_count = 0
        write = partial(writer.write_file,
                        relative_urls=self.settings.get('RELATIVE_URLS'))
        for cat in self.config:
            category_name = cat.get('category_name')
            if not category_name:
                warning("Improperly configured Standalone Category: "
                        "missing required `category_name` parameter.")
                continue
            category_name_lc = category_name.lower()
            cat_page_name = "{}.html".format(
                slugify(category_name_lc, self.settings.get(
                    'SLUG_SUBSTITUTIONS', ()
                ))
            )
            articles = self.context['standalone_articles'][category_name_lc]
            write(
                cat_page_name,
                self.get_template(cat['page_template']),
                self.context,
                articles=articles,
                category=cat['category_name']
            )
            page_count += 1
            the_articles, translations = process_translations(articles)
            for article in chain(the_articles, translations):
                write(
                    article.save_as,
                    self.get_template(cat['article_template']),
                    self.context,
                    article=article,
                    category=article.category,
                    override_output=hasattr(article, 'override_save_as')
                )
                article_count += 1
        print(
            "Standalone categories done: Processed {} articles and {}"
            " pages in {:.2f} seconds.".format(
                article_count, page_count,
                time.time() - start_time
            )
        )


def get_generators(generators):
    """ Adds our generator to the things Pelican will use to make stuff"""
    return StandaloneCategoryGenerator


def remove_category_articles(article_gen):
    """
    Removes articles and categories defined in the STANDALONE_CATEGORY_PAGES
    settings file from the regular Pelican article / category context and
    places them in a second context our generator will use.
    """
    config = article_gen.settings.get('STANDALONE_CATEGORY_PAGES')
    categories_to_watch = [cat['category_name'].lower() for cat in config]
    standalone_articles = defaultdict(list)
    non_standalone_articles = []
    non_standalone_categories = []
    for article in article_gen.articles:
        the_category = article.category.name.lower()
        if the_category in categories_to_watch:
            standalone_articles[the_category].append(article)
        else:
            non_standalone_articles.append(article)
    for category, articles in article_gen.categories:
        if category.name.lower() not in categories_to_watch:
            non_standalone_categories.append((category, articles))
    """
    This removes the articles from being created on the index page
    and from being generated along with the rest of the articles. You have to
    do it in both places (articles *and* context) or they will sneak in
    to the regualr blog.
    """
    article_gen.articles = non_standalone_articles
    article_gen.context['articles'] = non_standalone_articles
    article_gen.standalone_articles = standalone_articles
    article_gen.context['standalone_articles'] = standalone_articles
    """ Ditto for the category page """
    article_gen.categories = non_standalone_categories
    article_gen.context['categories'] = non_standalone_categories


def register():
    """ Registers plugin functions to run on Pelcian events """
    signals.article_generator_finalized.connect(remove_category_articles)
    signals.get_generators.connect(get_generators)
