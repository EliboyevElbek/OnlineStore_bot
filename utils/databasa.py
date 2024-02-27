import sqlite3

class Databasa:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()


    def maxsulot_qosh(self, maxsulot_name):
        try:
            self.cursor.execute(f"INSERT INTO maxsulotlar (maxsulot_nomi) VALUES (?);", (maxsulot_name,))
            self.conn.commit()
            return True
        except:
            return False


    def get_maxsulotlar(self):
        maxsulotlar = self.cursor.execute(f"SELECT id, maxsulot_nomi FROM maxsulotlar;")
        return maxsulotlar.fetchall()

    def tekshiriuv(self, nomi):
        maxsulot = self.cursor.execute(f"SELECT id, maxsulot_nomi FROM maxsulotlar WHERE maxsulot_nomi=?;",
                                       (nomi,)).fetchone()
        if not maxsulot:
            return True
        else:
            return False


    def rename_maxsulot(self, eski_nomi, yangisi):
        try:
            self.cursor.execute(f"UPDATE maxsulotlar SET maxsulot_nomi=? WHERE maxsulot_nomi=?;",
                                           (yangisi, eski_nomi))
            self.conn.commit()
            return True
        except:
            return False


    def delete_maxsulot(self, nomi):
        try:
            self.cursor.execute(f"DELETE FROM maxsulotlar WHERE maxsulot_nomi=?;",
                                (nomi,))
            self.conn.commit()
            return True
        except:
            return False


    def add_product(self, nomi, rasmi):
        try:
            self.cursor.execute(f"INSERT INTO products (product_nomi, product_rasm) VALUES (?, ?);",
                                (nomi, rasmi))
            self.conn.commit()
            return True
        except:
            return False


    def all_product(self):
        products = self.cursor.execute(f"SELECT * FROM products")
        return products.fetchall()

    def del_product(self, nomi):
        try:
            self.cursor.execute(f"DELETE FROM products WHERE products=?;", (nomi,))
            return True
        except:
            return False

    def get_product(self):
        product = self.cursor.execute(f"SELECT * FROM products;")
        return product.fetchall()