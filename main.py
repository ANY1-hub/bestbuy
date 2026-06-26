from config import colors
import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store):
    """
    handles the main menu
    :return: None
    """

    exit_item = len(menu_items) - 1
    while True:
        print("\n")
        for i, item in enumerate(menu_items):
            print(f"{colors.CYAN}{i + 1}.{colors.RESET}\t {item[0]}")
        try:
            menu_choice = int(
                input(
                    f"\nPlease choose: {colors.YELLOW}({colors.CYAN}1-{len(menu_items)}"
                    f"{colors.YELLOW}){colors.RESET}: ")) - 1
        except ValueError:
            print(f"\n{colors.YELLOW}Ooops, This was not even a {colors.BRIGHT}number "
                  f"{colors.NORMAL}{colors.RESET}")
            continue
        if (len(menu_items) - 1 < menu_choice or menu_choice < 0) and isinstance(menu_choice, int):
            print(
                f"\n{colors.RED}Please enter one of the {colors.BRIGHT}menu item{colors.NORMAL}s "
                f"{colors.BRIGHT}number{colors.RESET}\n")
            continue

        if menu_choice == exit_item:
            break
        menu_items[menu_choice][1]()



menu_items = [("List all products in sotre", None), ("Show total amount in store", None),
              ("Make an order", None),
              ("Quit", None)]


def main():
    """Main entry point of the application."""
    print(
        f"\n\n{colors.GREEN_B}**********{colors.RESET_B} {colors.YELLOW} Best buy{colors.RESET} "
        f"{colors.GREEN_B}**********{colors.RESET_B}")
    start('store1')


if __name__ == '__main__':
    main()
