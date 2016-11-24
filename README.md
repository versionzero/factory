# About

This project manages a simple inventory for a factory:

* Allow users to define/query product types
* Allow users to add/remove items from the inventory.
* Allow users to query the inventory

# Installation

The following will help install and configure the project. First, clone the repository:

```
git clone https://github.com/versionzero/factory
```

Next, make sure that `make` is installed locally:

```
sudo apt-get install build-essential
```

Now, install the dependencies and bring them in to the current environment:

```
cd factory
make install
. ~/venvs/factory/bin/activate
```

Lastly, launch the web-server:

```
make start
```

# Using the web-interface

There are a number of ways in which the interface can be used. For instance, a listing of the RESTful URLs can be seen by visiting the following in a web-browser:

```
http://localhost:8888/
```

Products and inventory items can be listed using the following URLs, respectivelly:

```
http://localhost:8888/products/
```

and

```
http://localhost:8888/inventory/
```

In both either case, products and inventory items can be added by using the form at the bottom of the page.

Similarly, both endpoints can filter and search for a subset of results. For instance, to retrive a list of products that cost more than $30, the following can be used:

```
http://localhost:8888/products/?price__gt=30
```

To find all the products with the word `Storm` contained within them, use the following:

```
http://localhost:8888/products/?search=Storm
```

A similar query can be used to look up items in the inventory:

```
http://localhost:8888/inventory/?search=IDE
```

The above returns a subset of the inventory where `ISD` is contained in the product that is inventoried, rather than any field in the inventory item itself.

A few other examples of queries are:

```
http://localhost:8888/inventory/?quantity__lt=11
http://localhost:8888/products/?name__contains=IDEA
http://localhost:8888/products/?description__contains=intelligent
http://localhost:8888/products/?price__gte=400
...
```

