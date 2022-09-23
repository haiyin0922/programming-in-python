class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        """Initialize self._categories as a nested list."""
        self._categories =  ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway']], 'income', ['salary', 'bonus']]
 
    def view(self, categories, level):
        """Recursively print the categories with indentation."""
        if type(categories) == list:
            for v in categories:
                self.view(v, level+1)
        else:
            print(f'{"  "*level}- {categories}')
 
    def is_category_valid(self, category, categories):
        """Recursively check if the category name is in self._categories."""
        if type(categories) == list:
            for v in categories:
                p = self.is_category_valid(category, v)
                if p == True:
                    return p
        return categories == category

 
    def find_subcategories(self, category, categories):
        """Recursively find the target category."""
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index + 1], True)
            else:
                if categories == category or found == True:
                    yield categories
        return list(find_subcategories_gen(category, self._categories))