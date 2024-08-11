import wikipedia


def main():
    """get user input for page title and display the details"""
    title = False
    while not title:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you")
        else:
            get_page_details(title)


def get_page_details(title):
    """Get and display page information."""
    try:
        page = wikipedia.page(title, auto_suggest=False)
        summary = page.summary[:200] + ('...' if len(page.summary) > 200 else '')
        print(f'Title: {page.title}\nSummary: {summary}\nURL: {page.url}\n')
    except wikipedia.DisambiguationError as disambiguation:
        print('The title you entered is ambiguous. Please choose from the following options:')
        for option in disambiguation.options:
            print(f' - {option}')
    except wikipedia.PageError:
        print(f'No page found with the title "{title}". Please try a different title.')


main()
