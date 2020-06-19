try:
    import pyshorteners
except:
  print("An error with the module has occurred")

def Menu():
    print("Welcome to the URL Shortener/URL Expander")
    print("--------------------------------------")
    print("You may chose from these url types")
    print("Chilp.it, is.gd, TinyURL")
    print("--------------------------------------")
    url_type = input("Enter url types: ")

    option = input("Would you like to shorten or expand the url?: ")

    if option.lower() == 'shorten':
        URLShortener(url_type)

    elif option.lower() == 'expand':
        URLExpander(url_type)

def URLShortener(url_type):
    url = pyshorteners.Shortener()
    user_url = input("Enter the url here: ")

    if url_type.lower() == 'chilp.it':
        print("Generated URL Link: " + url.chilpit.short(user_url))

    elif url_type.lower() == 'is.gd':
        print("Generated URL Link: " + url.isgd.short(user_url))

    elif url_type.lower() == 'tinyurl':
        print("Generated URL Link: " + url.tinyurl.short(user_url))

    print("--------------------------------------")

def URLExpander(url_type):
    expand_url = pyshorteners.Shortener()
    expand_user_url = input("Enter the url here: ")

    if url_type.lower() == 'chilp.it':
        print("Expanded URL Link: " + expand_url.chilpit.expand(expand_user_url))

    elif url_type.lower() == 'is.gd':
        print("Expanded URL Link: " + expand_url.isgd.expand(expand_user_url))

    elif url_type.lower() == 'tinyurl':
        print("Expanded URL Link: " + expand_url.tinyurl.expand(expand_user_url))

    print("--------------------------------------")

Menu()