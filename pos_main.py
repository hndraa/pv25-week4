import sys
from PyQt5 import QtWidgets, uic

class POSApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pos_app.ui", self)

        self.products = {
            "Bimoli (Rp. 20,000)": 20000,
            "Minyak Kita (Rp. 15,000)": 15000,
            "Filma (Rp. 22,000)": 22000
        }

        self.discounts = {
            "0%": 0,
            "5%": 5,
            "10%": 10
        }

        self.productDropdown.addItems(self.products.keys())
        self.discountDropdown.addItems(self.discounts.keys())

        self.addToCartButton.clicked.connect(self.add_to_cart)
        self.clearButton.clicked.connect(self.clear_cart)
        self.total_price = 0

    def add_to_cart(self):
        product = self.productDropdown.currentText()
        quantity = self.quantityInput.text()
        discount = self.discountDropdown.currentText()

        if not quantity.isdigit() or int(quantity) <= 0:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Quantity harus angka positif!")
            return

        quantity = int(quantity)
        price = self.products[product]
        discount_percent = self.discounts[discount]

        # Hitung harga setelah diskon
        total_item_price = price * quantity
        discount_amount = (discount_percent / 100) * total_item_price
        final_price = total_item_price - discount_amount

        # Tambahkan ke keranjang
        cart_text = f"{product} - {quantity} x Rp. {price:,} (disc {discount})"
        self.cartDisplay.append(cart_text)

        # Perbarui total harga
        self.total_price += final_price
        self.totalLabel.setText(f"Total: Rp. {self.total_price:,.0f}")

    def clear_cart(self):
        self.cartDisplay.clear()
        self.total_price = 0
        self.totalLabel.setText("Total: Rp. 0")

# Jalankan aplikasi
app = QtWidgets.QApplication(sys.argv)
window = POSApp()
window.show()
sys.exit(app.exec_())
