class ItemCard:
    """Класс карточки товара."""

    def __init__(self, id: int, name: str, quantity: int, status: str,
                 supplier: str, manufacturer: str, price: float,
                 location: str, category: str, min_stock: int = 0) -> None:
        """Инициализация карточки товара.

        Args:
            id: Уникальный идентификатор.
            name: Наименование товара.
            quantity: Количество на складе.
            status: Статус товара.
            supplier: Поставщик.
            manufacturer: Производитель.
            price: Цена за единицу.
            location: Местоположение на складе.
            category: Категория товара.
            min_stock: Минимальный запас.
        """
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__status = status
        self.__supplier = supplier
        self.__manufacturer = manufacturer
        self.__price = price
        self.__location = location
        self.__category = category
        self.__min_stock = min_stock

    def get_id(self) -> int:
        """Геттер для id.

        Returns:
            ID товара.
        """
        return self.__id

    def get_name(self) -> str:
        """Геттер для наименования."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Сеттер для наименования.

        Args:
            name: Новое наименование.

        Raises:
            ValueError: Если имя пустое.
        """
        if not name or not name.strip():
            raise ValueError('наименование не может быть пустым')
        
        self.__name = name.strip()

    def get_quantity(self) -> int:
        """Геттер для количества."""
        return self.__quantity

    def set_quantity(self, quantity: int) -> None:
        """Сеттер для количества.

        Args:
            quantity: Новое количество.

        Raises:
            ValueError: Если количество отрицательное.
        """
        if quantity < 0:
            raise ValueError('количество не может быть отрицательным')
        
        self.__quantity = quantity

    def get_status(self) -> str:
        """Геттер для статуса."""
        return self.__status

    def set_status(self, status: str) -> None:
        """Сеттер для статуса.

        Args:
            status: Новый статус (принято, зарезервировано, списано).

        Raises:
            ValueError: Если статус не из допустимых.
        """
        valid_statuses = {'принято', 'зарезервировано', 'списано'}

        if status not in valid_statuses:
            raise ValueError('статус должен быть одним из: принято, зарезервировано, списано')
        
        self.__status = status

    def get_supplier(self) -> str:
        """Геттер для поставщика."""
        return self.__supplier

    def set_supplier(self, supplier: str) -> None:
        """Сеттер для поставщика.

        Args:
            supplier: Новый поставщик.

        Raises:
            ValueError: Если поставщик пустой.
        """
        if not supplier or not supplier.strip():
            raise ValueError('поставщик не может быть пустым')
        
        self.__supplier = supplier.strip()

    def get_manufacturer(self) -> str:
        """Геттер для производителя."""
        return self.__manufacturer

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер для производителя.

        Args:
            manufacturer: Новый производитель.

        Raises:
            ValueError: Если производитель пустой.
        """
        if not manufacturer or not manufacturer.strip():
            raise ValueError('производитель не может быть пустым')
        
        self.__manufacturer = manufacturer.strip()

    def get_price(self) -> float:
        """Геттер для цены."""
        return self.__price

    def set_price(self, price: float) -> None:
        """Сеттер для цены.

        Args:
            price: Новая цена.

        Raises:
            ValueError: Если цена отрицательная.
        """
        if price < 0:
            raise ValueError('цена не может быть отрицательной')
        
        self.__price = price

    def get_location(self) -> str:
        """Геттер для местоположения."""
        return self.__location

    def set_location(self, location: str) -> None:
        """Сеттер для местоположения.

        Args:
            location: Новое местоположение.

        Raises:
            ValueError: Если местоположение пустое.
        """
        if not location or not location.strip():
            raise ValueError('местоположение не может быть пустым')
        
        self.__location = location.strip()

    def get_category(self) -> str:
        """Геттер для категории."""
        return self.__category

    def set_category(self, category: str) -> None:
        """Сеттер для категории.

        Args:
            category: Новая категория.

        Raises:
            ValueError: Если категория пустая.
        """
        if not category or not category.strip():
            raise ValueError('категория не может быть пустой')
        
        self.__category = category.strip()

    def get_min_stock(self) -> int:
        """Геттер для минимального запаса."""
        return self.__min_stock

    def set_min_stock(self, min_stock: int) -> None:
        """Сеттер для минимального запаса.

        Args:
            min_stock: Новый минимальный запас.

        Raises:
            ValueError: Если запас отрицательный.
        """
        if min_stock < 0:
            raise ValueError('минимальный запас не может быть отрицательным')
        
        self.__min_stock = min_stock

    def write_off(self) -> None:
        """Списать товар (перевести статус в 'списано' и обнулить количество).

        Raises:
            ValueError: Если статус товара не 'принято'.
        """
        if self.__status != 'принято':
            raise ValueError('списать можно только товар со статусом принято')
        
        self.__status = 'списано'
        self.__quantity = 0


items = []
next_id = 1


def create_card() -> None:
    """Создание новой карточки товара."""
    global next_id
    print('\n--- Новая карточка ---')
    try:
        card = ItemCard(
            id=next_id,
            name=input('Наименование: ').strip(),
            quantity=int(input('Количество: ')),
            status='принято',
            supplier=input('Поставщик: ').strip(),
            manufacturer=input('Производитель: ').strip(),
            price=float(input('Цена: ')),
            location=input('Местоположение: ').strip(),
            category=input('Категория: ').strip(),
            min_stock=int(input('Минимальный запас: '))
        )
        items.append(card)
        print(f'Карточка создана с id {next_id}')
        next_id += 1
    except ValueError as e:
        print(f'Ошибка: {e}')


def show_all() -> None:
    """Показать все карточки."""
    if not items:
        print('\nКарточек нет')
        return
    print('\n- Все карточки -')
    for card in items:
        print(f'id: {card.get_id()} | {card.get_name()} | {card.get_quantity()} шт | '
              f'статус: {card.get_status()} | цена: {card.get_price()} руб')
        print(f'поставщик: {card.get_supplier()}, производитель: {card.get_manufacturer()}')
        print(f'категория: {card.get_category()}, место: {card.get_location()}')
        print(f'мин запас: {card.get_min_stock()}')
        print('-' * 40)


def find_card() -> ItemCard | None:
    """Найти карточку по id и вернуть её."""
    try:
        id = int(input('Введите id карточки: '))
        for card in items:
            if card.get_id() == id:
                return card
        print('Карточка не найдена')
        return None
    except ValueError:
        print('Ошибка id должно быть числом')
        return None


def show_card() -> None:
    """Найти и показать карточку."""
    card = find_card()
    if card:
        print(f'id: {card.get_id()} | {card.get_name()} | {card.get_quantity()} шт | '
              f'статус: {card.get_status()} | цена: {card.get_price()} руб')
        print(f'поставщик: {card.get_supplier()}, производитель: {card.get_manufacturer()}')
        print(f'категория: {card.get_category()}, место: {card.get_location()}')
        print(f'мин запас: {card.get_min_stock()}')
        print('-' * 30)


def update_card() -> None:
    """Редактирование карточки."""
    card = find_card()
    if not card:
        return
    if card.get_status() == 'списано':
        print('Нельзя редактировать списанный товар')
        return

    print('Enter - оставить без изменений')
    fields = [
        ('наименование', card.get_name(), str, card.set_name),
        ('количество', card.get_quantity(), int, card.set_quantity),
        ('статус', card.get_status(), str, card.set_status),
        ('поставщик', card.get_supplier(), str, card.set_supplier),
        ('производитель', card.get_manufacturer(), str, card.set_manufacturer),
        ('цена', card.get_price(), float, card.set_price),
        ('местоположение', card.get_location(), str, card.set_location),
        ('категория', card.get_category(), str, card.set_category),
        ('мин запас', card.get_min_stock(), int, card.set_min_stock),
    ]

    try:
        for name, old, typ, setter in fields:
            val = input(f'{name} ({old}): ').strip()
            if val:
                if typ is int:
                    setter(int(val))
                elif typ is float:
                    setter(float(val))
                else:
                    setter(val)
        print('Данные обновлены')
    except ValueError as e:
        print(f'Ошибка: {e}')


def write_off_card() -> None:
    """Списание товара."""
    card = find_card()
    if not card:
        return
    try:
        card.write_off()
        print('Товар списан')
    except ValueError as e:
        print(f'Ошибка: {e}')


def main() -> None:
    """Главное меню."""
    while True:
        print('\n=== Учёт товаров ===')
        print('1. Создать карточку')
        print('2. Показать все')
        print('3. Найти карточку')
        print('4. Редактировать')
        print('5. Списать товар')
        print('0. Выход')
        match input('Выберите действие: '):
            case '1':
                create_card()
            case '2':
                show_all()
            case '3':
                show_card()
            case '4':
                update_card()
            case '5':
                write_off_card()
            case '0':
                print('До свидания!')
                break
            case _:
                print('Неверный ввод')


if __name__ == '__main__':
    main()