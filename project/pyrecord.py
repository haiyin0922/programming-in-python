from datetime import date
from tkinter import messagebox as mb

class Record:
    """Represent a record."""
    def __init__(self, date, category, description, amount):
        """A Record can be instantiated by calling Record('2020-06-27', 'meal', 'breakfast', -50)."""
        self._date = date
        self._category = category
        self._description = description
        self._amount = amount

    @property
    def date(self):
        return self._date
        
    @property
    def category(self):
        return self._category

    @property
    def description(self):
        return self._description  

    @property
    def amount(self):
        return self._amount

class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        """Initialize the attributes from the file or user input."""
        self._records = []
        try:
            fh = open('records.txt')
        except FileNotFoundError:
            try:
                self._balance = 0
            except ValueError:
                print('Invalid value for money. Set to 0 by default.')
                self._balance = 0
        else:
            try:
                print('Welcome back!')
                self._balance = int(fh.readline())
            except ValueError:
                print('No line is in the file, or the line cannot be interpreted as initial amount of money.\n')
                self._balance = int(input('How much money do you have? '))
            for line in fh.readlines():
                try:
                    self._records.append(Record(line.split()[0], line.split()[1], line.split()[2], int(line.split()[3])))
                except:
                    print('Any of lines cannot be interpreted as a record.')
            fh.close()
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def records(self):
        return self._records
        
    def set_balance(self, money):
        self._balance = money
            
    def add(self, record, categories):
        """Add the Record into self._records if the date and category are valid."""
        if len(record.split()) == 3:
            try:
                category = record.split()[0]
                if categories.is_category_valid(category, categories._categories):
                    today = str(date.today())
                    description = record.split()[1]
                    amount = int(record.split()[2])
                    self._records.append(Record(today, category, description, amount))
                    self._balance += amount
                else:
                    print('''The specified category is not in the category list. \nYou can check the category list by command "view categories". \nFail to add a record.''')
            except IndexError:
                print('The format of a record should be like this: meal breakfast -50. \nFail to add a record.')
            except ValueError:
                print('Invalid value for money.\nFail to add a record.')
        else:
            try:
                today = str(date.fromisoformat(record.split()[0]))
            except ValueError:
                mb.showerror('ERROR', 'Fail to add a record.', detail = 'The format of date should be YYYY-MM-DD.')
                print('The format of date should be YYYY-MM-DD. \nFail to add a record.')
            else:
                try:
                    category = record.split()[1]
                    if categories.is_category_valid(category, categories._categories):
                        description = record.split()[2]
                        amount = int(record.split()[3])
                        self._records.append(Record(today, category, description, amount))
                        self._balance += amount
                    else:
                        print('''The specified category is not in the category list. \nYou can check the category list by command "view categories". \nFail to add a record.''')
                except IndexError:
                    print('The format of a record should be like this: meal breakfast -50. \nFail to add a record.')
                except ValueError:
                    print('Invalid value for money.\nFail to add a record.')

 
    def view(self):
        """Print all the records and report the balance."""
        print('''Here's your expense and income records:''')
        print('Date           Category        Description          Amount')
        print('============== =============== ==================== ======')
        for i, r in enumerate(self._records):
            print(f'{i+1:<2}) {r.date:<11}{r.category:<16}{r.description:<21}{r.amount}')
        print('==========================================================')
        print(f'Now you have {self._balance} dollars.')
 
    def delete(self, delete_record):
        """Delete the specified record from self._records."""
        try:
            num = int(delete_record)
            self._balance -= self._records[num].amount
            del self._records[num]
        except IndexError:
            print(f'''There's no record number {delete_record}. Fail to delete a record.''')
        except ValueError:
            print('Invalid format. Fail to delete a record.')
 
    def find(self, target_categories):
        """Print the records whose category is in the list passed in and report the total amount of money of the listed records."""
        if not target_categories:
            print('The specified category is not in the category list. \nYou can check the category list by command "view categories".')
        else:
            money = 0
            item = list(filter(lambda x: x.category in target_categories, self._records))
            #print(f'''Here's your expense and income records under category "{category}":''')
            print('Date       Category           Description          Amount')
            print('========== ================== ==================== ======')
            for r in item:
                print(f'{r.date:<11}{r.category:<19}{r.description:<21}{r.amount}')
                money += r.amount
            print('=========================================================')
            print(f'The total amount above is {money}.')
            return (money, item)
 
    def save(self):
        """Write the initial money and all the records to 'records.txt'."""
        records_list = []
        for r in self._records:
            records_list.extend([r.date, ' ', r.category, ' ', r.description, ' ', str(r.amount), '\n'])
        with open('records.txt', 'w') as fh:
            fh.write(str(self._balance)+'\n')
            fh.writelines(records_list)
