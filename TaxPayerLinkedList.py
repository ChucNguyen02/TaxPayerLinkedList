from TaxPayer import TaxPayer
from Node import Node

class TaxPayerLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Load data from file
    def load_from_file(self, filename):
        success = False
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) >= 4:
                        code = parts[0].strip()
                        name = parts[1].strip()
                        try:
                            income = float(parts[2])
                            deduction = float(parts[3])
                            if income <= 0 or deduction < 0 or deduction >= income:
                                continue
                            if self.search_by_code(code):
                                continue
                            if self.add_to_end(code, name, income, deduction):
                                success = True
                        except ValueError:
                            continue
            return success
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False


    # 2. Input & add to end
    def add_to_end(self, code, name, income, deduction):
        if income <= 0 or deduction < 0 or deduction >= income:
            print("Invalid data.")
            return False
        if self.search_by_code(code):
            print("Duplicate code.")
            return False
        taxpayer = TaxPayer(code, name, income, deduction)
        new_node = Node(taxpayer)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print('Add data successfully')
        return True

    # 3. Display data
    def display_all(self):
        if not self.head:
            print("The list is empty.")
            return
        print("\n{:<5} {:<10} {:<20} {:<10} {:<10} {:<10}".format(
            "No.", "Code", "Name", "Income", "Deduction", "Tax"))
        print("-" * 70)
        current = self.head
        count = 0
        while current:
            tp = current.taxpayer
            print("{:<5} {:<10} {:<20} {:<10.2f} {:<10.2f} {:<10.2f}".format(count, tp.code, tp.name, tp.income, tp.deduction, tp.tax))
            count += 1
            current = current.next
        print(f"\nTotal records: {count}")


    # 4. Save data to file
    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                current = self.head
                while current:
                    tp = current.taxpayer
                    file.write(f"{tp.code},{tp.name},{tp.income},{tp.deduction},{tp.tax}\n")
                    current = current.next
            print(f"Data saved to {filename}.")
        except Exception as e:
            print(f"Error saving file: {e}")

    # 5. Search by code
    def search_by_code(self, code):
        current = self.head
        while current:
            if current.taxpayer.code == code:
                return current.taxpayer
            current = current.next
        return None

    # 6. Delete by code
    def delete_by_code(self, code):
        if not self.head:
            print("The list is empty.")
            return False
        if self.head.taxpayer.code == code:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            print(f"Deleted taxpayer with code {code}.")
            return True
        current = self.head
        while current.next:
            if current.next.taxpayer.code == code:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                print(f"Deleted taxpayer with code {code}.")
                return True
            current = current.next
        print("Code not found.")
        return False

    # 7. Sort by code
    def sort_by_code(self):
        if not self.head or not self.head.next:
            return
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        nodes.sort(key=lambda node: node.taxpayer.code)
        self.head = nodes[0]
        current = self.head
        for i in range(1, len(nodes)):
            current.next = nodes[i]
            current = current.next
        self.tail = nodes[-1]
        self.tail.next = None
        print("Sorted by code.")

    # 8. Input & add to beginning
    def add_to_beginning(self, code, name, income, deduction):
        if income <= 0 or deduction < 0 or deduction >= income:
            print("Invalid data.")
            return False
        if self.search_by_code(code):
            print("Duplicate code.")
            return False
        taxpayer = TaxPayer(code, name, income, deduction)
        new_node = Node(taxpayer)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print('Add data successfully')
        return True

    # 9. Add after position k
    def add_after_position(self, k, code, name, income, deduction):
        if income <= 0 or deduction < 0 or deduction >= income:
            print("Invalid data.")
            return False
        if self.search_by_code(code):
            print("Duplicate code.")
            return False
        if k < 0:
            print("Invalid position.")
            return False
        taxpayer = TaxPayer(code, name, income, deduction)
        new_node = Node(taxpayer)
        current = self.head
        pos = 0
        while current and pos < k:
            current = current.next
            pos += 1
        if not current:
            print("Position out of range.")
            return False
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node
        print(f"Added after position {k}.")
        return True

    # 10. Delete position k
    def delete_at_position(self, k):
        if k < 0:
            print("Invalid position.")
            return False
        if not self.head:
            print("List is empty.")
            return False
        if k == 0:
            deleted_code = self.head.taxpayer.code
            self.head = self.head.next
            if not self.head:
                self.tail = None
            print(f"Deleted position {k} (code: {deleted_code})")
            return True
        current = self.head
        pos = 0
        while current and pos < k - 1:
            current = current.next
            pos += 1
        if not current or not current.next:
            print("Position out of range.")
            return False
        deleted_code = current.next.taxpayer.code
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
        print(f"Deleted position {k} (code: {deleted_code})")
        return True

    # Extra methods
    def is_empty(self):
        return self.head is None

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.head = None
        self.tail = None
        print("List cleared.")
