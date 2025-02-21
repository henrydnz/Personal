from multiprocessing.sharedctypes import Value
import os

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, item_name, price, production) -> None:
        self.name: str = item_name
        self.price: float = price
        self.production: float = production
        self.index: float = price/production

    def get_index(self) -> None:
        self.index = self.price/self.production
    
    def change_price(self, new_price: int) -> None:
        self.price = new_price
        self.get_index()

    def change_production(self, new_production: int) -> None:
        self.production = new_production
        self.get_index()
    
    def change_value(self, type: str, value: float) -> None:
        match type:
            case 'p':
                self.change_price(value)
            case 'v':
                self.change_price(value)
            case _:
                print('command error')

class Main:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def organize_items(self) -> None:
        self.items.sort(key=lambda i: i.index)
    
    def exists(self, name: str) -> bool:
        return any(item.name == name for item in self.items)
    
    def add_item(self, item_name: str, price: float, production: float) -> None:
        new_item: Item = Item(item_name, price, production)
        self.items.append(new_item)
    
    def remove_item(self, item_name: str) -> None:
        self.items.pop(item_name)

    def show_items(self) -> None:
        for item in self.items:
            print(f'{item.name} = {item.index:.2f}')

    def command(self) -> None:
        while True:
            command_input: list[str] = input('\n> ').split()

            if len(command_input) < 2: 
                print('Error: Not enough arguments')
                break

            option: str = command_input[0]

            match option:
                case "add":
                    if len(command_input) != 4:
                        print(f'Error: \'add\' expects 3 arguments. Got {len(command_input)-1}.')
                        break

                    name: str = command_input[1]
                    price = command_input[2]
                    production = command_input[3]

                    try:
                        self.add_item(name, float(price), float(production))
                    except ValueError:
                        print('Error: \'add\' expects 2 numbers. Got', int(price.isdigit() or production.isdigit()))

                    break

                case "remove":
                    if len(command_input) != 2:
                        print(f'Error: \'remove\' expects 1 argument. Got {len(command_input)-1}.')
                        break

                    name: str = command_input[1]

                    if self.exists(name):
                        print(f'Error: Item \'{name}\' not found.')
                    else:
                        self.remove_item(name)

                    break

                case "change":
                    if len(command_input) != 4:
                        print(f'Error: \'change\' expects 1 argument. Got {len(command_input)-1}.')
                        break

                    name: str = command_input[1]
                    type: str = command_input[2]
                    value: str = command_input[3]

                    if self.exists(name):
                        print(f'Error: item \'{name}\' not found.')
                        break
                    elif type not in ['price', 'production']:
                        print(f'Error: \'change\' expects types (\'price\', \'production\'). Got \'{type}\'')
                        break

                    try:
                        item: Item = filter(lambda item: item.name == name, self.objects)
                        item.change_value(type, float(value))             
                    except ValueError:
                        print(f'Error: {value} is not a number.')

                    break

                case _:
                    print('Error: unknown argument')
                    break

    def main(self) -> None:
        while True:
            self.organize_items()
            self.show_items()
            self.command()

def main() -> None:
    main: Main = Main()
    main.main()

if __name__ == '__main__':
    main()