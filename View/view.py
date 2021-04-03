# @Author: Abdellah Oulahyane
# @Date:   2021-03-25 00:09:25
# @Last Modified by:   Abdellah Oulahyane
# @Last Modified time: 2021-03-31 07:52:43



import sys
import datetime

from Controller.bookController import bookController
from Controller.userController import userController
from Controller.saleController import saleController
from Controller.bookdeatailsController import bookdetailsController
from Controller.categoryController import CategoryController
from PyQt5.QtWidgets import QHeaderView, QMessageBox


from PyQt5 import QtCore, QtGui, QtWidgets


class View(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.book = QtWidgets.QTabWidget(self.centralwidget)
        self.book.setObjectName("book")
        self.Books = QtWidgets.QWidget()
        self.Books.setObjectName("Books")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Books)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.new_book = QtWidgets.QTabWidget(self.Books)
        self.new_book.setObjectName("new_book")
        self.file_menuPage1 = QtWidgets.QWidget()
        self.file_menuPage1.setObjectName("file_menuPage1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.file_menuPage1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.file_menuPage1)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_26.addWidget(self.label_28)
        self.book_id = QtWidgets.QLineEdit(self.groupBox)
        self.book_id.setObjectName("book_id")
        self.horizontalLayout_26.addWidget(self.book_id)
        self.verticalLayout.addLayout(self.horizontalLayout_26)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.book_title = QtWidgets.QLineEdit(self.groupBox)
        self.book_title.setObjectName("book_title")
        self.horizontalLayout.addWidget(self.book_title)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.book_author = QtWidgets.QLineEdit(self.groupBox)
        self.book_author.setObjectName("book_author")
        self.horizontalLayout_2.addWidget(self.book_author)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.book_quantity = QtWidgets.QLineEdit(self.groupBox)
        self.book_quantity.setObjectName("book_quantity")
        self.horizontalLayout_3.addWidget(self.book_quantity)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.book_price = QtWidgets.QLineEdit(self.groupBox)
        self.book_price.setObjectName("book_price")
        self.horizontalLayout_5.addWidget(self.book_price)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_21.addWidget(self.label_29)
        self.book_details = QtWidgets.QComboBox(self.groupBox)
        self.book_details.setObjectName("book_details")
        self.horizontalLayout_21.addWidget(self.book_details)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.file_menuPage1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_27.addWidget(self.label_30)
        self.book_details_id = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_id.setObjectName("book_details_id")
        self.horizontalLayout_27.addWidget(self.book_details_id)
        self.verticalLayout_2.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.book_details_language = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_language.setObjectName("book_details_language")
        self.horizontalLayout_7.addWidget(self.book_details_language)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.book_details_pages = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_pages.setObjectName("book_details_pages")
        self.horizontalLayout_8.addWidget(self.book_details_pages)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.book_details_isbn_10 = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_isbn_10.setObjectName("book_details_isbn_10")
        self.horizontalLayout_9.addWidget(self.book_details_isbn_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.book_details_isbn_13 = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_isbn_13.setObjectName("book_details_isbn_13")
        self.horizontalLayout_16.addWidget(self.book_details_isbn_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        self.book_details_weight = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_weight.setObjectName("book_details_weight")
        self.horizontalLayout_17.addWidget(self.book_details_weight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        self.book_details_dementions = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_dementions.setObjectName("book_details_dementions")
        self.horizontalLayout_18.addWidget(self.book_details_dementions)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        self.book_details_description = QtWidgets.QLineEdit(self.groupBox_2)
        self.book_details_description.setObjectName("book_details_description")
        self.horizontalLayout_19.addWidget(self.book_details_description)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        self.book_details_category = QtWidgets.QComboBox(self.groupBox_2)
        self.book_details_category.setObjectName("book_details_category")
        self.horizontalLayout_20.addWidget(self.book_details_category)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 4, 1)
        self.book_btn_add = QtWidgets.QPushButton(self.file_menuPage1)
        self.book_btn_add.setObjectName("book_btn_add")
        self.gridLayout_3.addWidget(self.book_btn_add, 1, 0, 1, 1)
        self.book_btn_update = QtWidgets.QPushButton(self.file_menuPage1)
        self.book_btn_update.setObjectName("book_btn_update")
        self.gridLayout_3.addWidget(self.book_btn_update, 2, 0, 1, 1)
        self.book_btn_delete = QtWidgets.QPushButton(self.file_menuPage1)
        self.book_btn_delete.setObjectName("book_btn_delete")
        self.gridLayout_3.addWidget(self.book_btn_delete, 3, 0, 1, 1)
        self.new_book.addTab(self.file_menuPage1, "")
        self.file_menuPage3 = QtWidgets.QWidget()
        self.file_menuPage3.setObjectName("file_menuPage3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.file_menuPage3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.book_table = QtWidgets.QTableWidget(self.file_menuPage3)
        self.book_table.setObjectName("book_table")
        self.book_table.setColumnCount(5)
        self.book_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.book_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.book_table.setHorizontalHeaderItem(4, item)
        self.gridLayout_5.addWidget(self.book_table, 1, 0, 1, 3)
        self.book_btn_search = QtWidgets.QPushButton(self.file_menuPage3)
        self.book_btn_search.setObjectName("book_btn_search")
        self.gridLayout_5.addWidget(self.book_btn_search, 0, 2, 1, 1)
        self.book_input_search = QtWidgets.QLineEdit(self.file_menuPage3)
        self.book_input_search.setObjectName("book_input_search")
        self.gridLayout_5.addWidget(self.book_input_search, 0, 0, 1, 1)
        self.book_text_change = QtWidgets.QCheckBox(self.file_menuPage3)
        self.book_text_change.setObjectName("book_text_change")
        self.gridLayout_5.addWidget(self.book_text_change, 0, 1, 1, 1)
        self.new_book.addTab(self.file_menuPage3, "")
        self.gridLayout_2.addWidget(self.new_book, 0, 0, 1, 1)
        self.book.addTab(self.Books, "")
        self.Categories = QtWidgets.QWidget()
        self.Categories.setObjectName("Categories")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Categories)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_5 = QtWidgets.QGroupBox(self.Categories)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.category_btn_add = QtWidgets.QPushButton(self.groupBox_5)
        self.category_btn_add.setObjectName("category_btn_add")
        self.horizontalLayout_22.addWidget(self.category_btn_add)
        self.category_btn_update = QtWidgets.QPushButton(self.groupBox_5)
        self.category_btn_update.setObjectName("category_btn_update")
        self.horizontalLayout_22.addWidget(self.category_btn_update)
        self.category_btn_delete = QtWidgets.QPushButton(self.groupBox_5)
        self.category_btn_delete.setObjectName("category_btn_delete")
        self.horizontalLayout_22.addWidget(self.category_btn_delete)
        self.gridLayout.addLayout(self.horizontalLayout_22, 3, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_37 = QtWidgets.QLabel(self.groupBox_5)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_23.addWidget(self.label_37)
        self.category_description = QtWidgets.QPlainTextEdit(self.groupBox_5)
        self.category_description.setObjectName("category_description")
        self.horizontalLayout_23.addWidget(self.category_description)
        self.gridLayout.addLayout(self.horizontalLayout_23, 2, 0, 1, 1)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_36 = QtWidgets.QLabel(self.groupBox_5)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_24.addWidget(self.label_36)
        self.category_label = QtWidgets.QLineEdit(self.groupBox_5)
        self.category_label.setObjectName("category_label")
        self.horizontalLayout_24.addWidget(self.category_label)
        self.gridLayout.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_25.addWidget(self.label_35)
        self.category_id = QtWidgets.QLineEdit(self.groupBox_5)
        self.category_id.setObjectName("category_id")
        self.horizontalLayout_25.addWidget(self.category_id)
        self.gridLayout.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_5, 0, 0, 1, 3)
        self.category_input_search = QtWidgets.QLineEdit(self.Categories)
        self.category_input_search.setInputMask("")
        self.category_input_search.setObjectName("category_input_search")
        self.gridLayout_7.addWidget(self.category_input_search, 1, 0, 1, 1)
        self.category_btn_search = QtWidgets.QPushButton(self.Categories)
        self.category_btn_search.setObjectName("category_btn_search")
        self.gridLayout_7.addWidget(self.category_btn_search, 1, 2, 1, 1)
        self.category_table = QtWidgets.QTableWidget(self.Categories)
        self.category_table.setObjectName("category_table")
        self.category_table.setColumnCount(3)
        self.category_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.category_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.category_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.category_table.setHorizontalHeaderItem(2, item)
        self.gridLayout_7.addWidget(self.category_table, 2, 0, 1, 3)
        self.category_text_change = QtWidgets.QCheckBox(self.Categories)
        self.category_text_change.setObjectName("category_text_change")
        self.gridLayout_7.addWidget(self.category_text_change, 1, 1, 1, 1)
        self.book.addTab(self.Categories, "")
        self.Sales = QtWidgets.QWidget()
        self.Sales.setObjectName("Sales")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.Sales)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Sales)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_7 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_10 = QtWidgets.QLabel(self.splitter_7)
        self.label_10.setObjectName("label_10")
        self.sale_add_client = QtWidgets.QComboBox(self.splitter_7)
        self.sale_add_client.setObjectName("sale_add_client")
        self.verticalLayout_4.addWidget(self.splitter_7)
        self.splitter_6 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_11 = QtWidgets.QLabel(self.splitter_6)
        self.label_11.setObjectName("label_11")
        self.sale_add_book = QtWidgets.QComboBox(self.splitter_6)
        self.sale_add_book.setObjectName("sale_add_book")
        self.verticalLayout_4.addWidget(self.splitter_6)
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_12 = QtWidgets.QLabel(self.splitter_5)
        self.label_12.setObjectName("label_12")
        self.sale_add_quantity = QtWidgets.QLineEdit(self.splitter_5)
        self.sale_add_quantity.setObjectName("sale_add_quantity")
        self.verticalLayout_4.addWidget(self.splitter_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.sale_btn_add_order = QtWidgets.QPushButton(self.groupBox_3)
        self.sale_btn_add_order.setObjectName("sale_btn_add_order")
        self.verticalLayout_5.addWidget(self.sale_btn_add_order)
        self.gridLayout_8.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Sales)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_13 = QtWidgets.QLabel(self.splitter)
        self.label_13.setObjectName("label_13")
        self.sale_id_edit = QtWidgets.QComboBox(self.splitter)
        self.sale_id_edit.setObjectName("sale_id_edit")
        self.verticalLayout_6.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_14 = QtWidgets.QLabel(self.splitter_2)
        self.label_14.setObjectName("label_14")
        self.sale_client_edit = QtWidgets.QComboBox(self.splitter_2)
        self.sale_client_edit.setObjectName("sale_client_edit")
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_15 = QtWidgets.QLabel(self.splitter_3)
        self.label_15.setObjectName("label_15")
        self.sale_book_edit = QtWidgets.QComboBox(self.splitter_3)
        self.sale_book_edit.setObjectName("sale_book_edit")
        self.verticalLayout_6.addWidget(self.splitter_3)
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_27 = QtWidgets.QLabel(self.splitter_4)
        self.label_27.setObjectName("label_27")
        self.sale_quantity_edit = QtWidgets.QLineEdit(self.splitter_4)
        self.sale_quantity_edit.setObjectName("sale_quantity_edit")
        self.verticalLayout_6.addWidget(self.splitter_4)
        self.splitter_8 = QtWidgets.QSplitter(self.groupBox_4)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.sale_btn_edit_order = QtWidgets.QPushButton(self.splitter_8)
        self.sale_btn_edit_order.setObjectName("sale_btn_edit_order")
        self.sale_btn_delete_order = QtWidgets.QPushButton(self.splitter_8)
        self.sale_btn_delete_order.setObjectName("sale_btn_delete_order")
        self.verticalLayout_6.addWidget(self.splitter_8)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 3)
        self.sale_input_search = QtWidgets.QLineEdit(self.Sales)
        self.sale_input_search.setObjectName("sale_input_search")
        self.gridLayout_12.addWidget(self.sale_input_search, 1, 0, 1, 1)
        self.sale_table = QtWidgets.QTableWidget(self.Sales)
        self.sale_table.setObjectName("sale_table")
        self.sale_table.setColumnCount(6)
        self.sale_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sale_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sale_table.setHorizontalHeaderItem(5, item)
        self.gridLayout_12.addWidget(self.sale_table, 2, 0, 1, 3)
        self.sale_btn_search = QtWidgets.QPushButton(self.Sales)
        self.sale_btn_search.setObjectName("sale_btn_search")
        self.gridLayout_12.addWidget(self.sale_btn_search, 1, 2, 1, 1)
        self.sale_text_change = QtWidgets.QCheckBox(self.Sales)
        self.sale_text_change.setObjectName("sale_text_change")
        self.gridLayout_12.addWidget(self.sale_text_change, 1, 1, 1, 1)
        self.book.addTab(self.Sales, "")
        self.Users = QtWidgets.QWidget()
        self.Users.setObjectName("Users")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Users)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_6 = QtWidgets.QLabel(self.Users)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_15.addWidget(self.label_6)
        self.user_id = QtWidgets.QLineEdit(self.Users)
        self.user_id.setObjectName("user_id")
        self.horizontalLayout_15.addWidget(self.user_id)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_4 = QtWidgets.QLabel(self.Users)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_14.addWidget(self.label_4)
        self.user_reference = QtWidgets.QLineEdit(self.Users)
        self.user_reference.setObjectName("user_reference")
        self.horizontalLayout_14.addWidget(self.user_reference)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.Users)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_13.addWidget(self.label_21)
        self.user_fullname = QtWidgets.QLineEdit(self.Users)
        self.user_fullname.setObjectName("user_fullname")
        self.horizontalLayout_13.addWidget(self.user_fullname)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_22 = QtWidgets.QLabel(self.Users)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.user_username = QtWidgets.QLineEdit(self.Users)
        self.user_username.setObjectName("user_username")
        self.horizontalLayout_12.addWidget(self.user_username)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_23 = QtWidgets.QLabel(self.Users)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_11.addWidget(self.label_23)
        self.user_passowrd = QtWidgets.QLineEdit(self.Users)
        self.user_passowrd.setObjectName("user_passowrd")
        self.horizontalLayout_11.addWidget(self.user_passowrd)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_24 = QtWidgets.QLabel(self.Users)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_10.addWidget(self.label_24)
        self.user_roles = QtWidgets.QComboBox(self.Users)
        self.user_roles.setObjectName("user_roles")
        self.user_roles.addItem("")
        self.user_roles.setItemText(0, "")
        self.user_roles.addItem("")
        self.user_roles.addItem("")
        self.horizontalLayout_10.addWidget(self.user_roles)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_25 = QtWidgets.QLabel(self.Users)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_6.addWidget(self.label_25)
        self.user_contact = QtWidgets.QLineEdit(self.Users)
        self.user_contact.setObjectName("user_contact")
        self.horizontalLayout_6.addWidget(self.user_contact)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_26 = QtWidgets.QLabel(self.Users)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_4.addWidget(self.label_26)
        self.user_address = QtWidgets.QPlainTextEdit(self.Users)
        self.user_address.setObjectName("user_address")
        self.horizontalLayout_4.addWidget(self.user_address)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 3)
        self.user_search = QtWidgets.QLineEdit(self.Users)
        self.user_search.setObjectName("user_search")
        self.gridLayout_6.addWidget(self.user_search, 1, 0, 1, 1)
        self.user_text_changing = QtWidgets.QCheckBox(self.Users)
        self.user_text_changing.setObjectName("checkBox")
        self.gridLayout_6.addWidget(self.user_text_changing, 1, 1, 1, 1)
        self.user_btn_search = QtWidgets.QPushButton(self.Users)
        self.user_btn_search.setObjectName("user_btn_search")
        self.gridLayout_6.addWidget(self.user_btn_search, 1, 2, 1, 1)
        self.user_table = QtWidgets.QTableWidget(self.Users)
        self.user_table.setObjectName("user_table")
        self.user_table.setColumnCount(7)
        self.user_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_table.setHorizontalHeaderItem(6, item)
        self.gridLayout_6.addWidget(self.user_table, 2, 0, 1, 3)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.user_btn_add = QtWidgets.QPushButton(self.Users)
        self.user_btn_add.setObjectName("user_btn_add")
        self.horizontalLayout_28.addWidget(self.user_btn_add)
        self.user_btn_update = QtWidgets.QPushButton(self.Users)
        self.user_btn_update.setObjectName("user_btn_update")
        self.horizontalLayout_28.addWidget(self.user_btn_update)
        self.user_btn_delete = QtWidgets.QPushButton(self.Users)
        self.user_btn_delete.setObjectName("user_btn_delete")
        self.horizontalLayout_28.addWidget(self.user_btn_delete)
        self.gridLayout_6.addLayout(self.horizontalLayout_28, 3, 0, 1, 3)
        self.book.addTab(self.Users, "")
        self.gridLayout_9.addWidget(self.book, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 20))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuBook = QtWidgets.QMenu(self.menubar)
        self.menuBook.setObjectName("menuBook")
        self.menuCategory = QtWidgets.QMenu(self.menubar)
        self.menuCategory.setObjectName("menuCategory")
        self.menuSale = QtWidgets.QMenu(self.menubar)
        self.menuSale.setObjectName("menuSale")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Edit = QtWidgets.QAction(MainWindow)
        self.action_Edit.setObjectName("action_Edit")
        self.action_Delete = QtWidgets.QAction(MainWindow)
        self.action_Delete.setObjectName("action_Delete")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_File.addAction(self.action_Edit)
        self.menu_File.addAction(self.action_Delete)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_File.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuBook.menuAction())
        self.menubar.addAction(self.menuCategory.menuAction())
        self.menubar.addAction(self.menuSale.menuAction())
        self.menubar.addAction(self.menuUser.menuAction())

        self.retranslateUi(MainWindow)
        self.book.setCurrentIndex(0)
        self.new_book.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Main Book Details"))
        self.label_28.setText(_translate("MainWindow", "ID            "))
        self.label.setText(_translate("MainWindow", "Title         "))
        self.label_2.setText(_translate("MainWindow", "Author     "))
        self.label_3.setText(_translate("MainWindow", "Quantity  "))
        self.label_5.setText(_translate("MainWindow", "Price        "))
        self.label_29.setText(_translate("MainWindow", "Book Details"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Book Details"))
        self.label_30.setText(_translate("MainWindow", "ID                  "))
        self.label_7.setText(_translate("MainWindow", "Language      "))
        self.label_8.setText(_translate("MainWindow", "Pages            "))
        self.label_9.setText(_translate("MainWindow", "ISBN-10         "))
        self.label_16.setText(_translate("MainWindow", "ISBN-13         "))
        self.label_17.setText(_translate("MainWindow", "Book Weight  "))
        self.label_18.setText(_translate("MainWindow", "Dementions   "))
        self.label_19.setText(_translate("MainWindow", "Description    "))
        self.label_20.setText(_translate("MainWindow", "Category"))
        self.book_btn_add.setText(_translate("MainWindow", "Add New Book"))
        self.book_btn_update.setText(_translate("MainWindow", "Update Book"))
        self.book_btn_delete.setText(_translate("MainWindow", "Delete Book"))
        self.new_book.setTabText(self.new_book.indexOf(self.file_menuPage1), _translate("MainWindow", "Books Management"))
        item = self.book_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.book_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.book_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Author"))
        item = self.book_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.book_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantity"))
        self.book_btn_search.setText(_translate("MainWindow", "Search"))
        self.book_text_change.setText(_translate("MainWindow", "Allow text change"))
        self.new_book.setTabText(self.new_book.indexOf(self.file_menuPage3), _translate("MainWindow", "Books searching "))
        self.book.setTabText(self.book.indexOf(self.Books), _translate("MainWindow", "Books"))
        self.groupBox_5.setTitle(_translate("MainWindow", "| Add new Category"))
        self.category_btn_add.setText(_translate("MainWindow", "Add"))
        self.category_btn_update.setText(_translate("MainWindow", "Update"))
        self.category_btn_delete.setText(_translate("MainWindow", "Delete"))
        self.label_37.setText(_translate("MainWindow", "Description"))
        self.label_36.setText(_translate("MainWindow", "Label          "))
        self.label_35.setText(_translate("MainWindow", "ID               "))
        self.category_btn_search.setText(_translate("MainWindow", "Search"))
        item = self.category_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.category_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Lable"))
        item = self.category_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description"))
        self.category_text_change.setText(_translate("MainWindow", "Allow text change"))
        self.book.setTabText(self.book.indexOf(self.Categories), _translate("MainWindow", "Category"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Add"))
        self.label_10.setText(_translate("MainWindow", "Client"))
        self.label_11.setText(_translate("MainWindow", "Book                       "))
        self.label_12.setText(_translate("MainWindow", "Quantity                 "))
        self.sale_btn_add_order.setText(_translate("MainWindow", "ADD New Order"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Edit/Delete"))
        self.label_13.setText(_translate("MainWindow", "ID                            "))
        self.label_14.setText(_translate("MainWindow", "Client"))
        self.label_15.setText(_translate("MainWindow", "Book                        "))
        self.label_27.setText(_translate("MainWindow", "Quantity                  "))
        self.sale_btn_edit_order.setText(_translate("MainWindow", "EDIT ORDER"))
        self.sale_btn_delete_order.setText(_translate("MainWindow", "DELETE ORDER"))
        item = self.sale_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.sale_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Client"))
        item = self.sale_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Book"))
        item = self.sale_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.sale_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "User"))
        item = self.sale_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Created at"))
        self.sale_btn_search.setText(_translate("MainWindow", "Search"))
        self.sale_text_change.setText(_translate("MainWindow", "Allow text change"))
        self.book.setTabText(self.book.indexOf(self.Sales), _translate("MainWindow", "Sales"))
        self.label_6.setText(_translate("MainWindow", "ID               "))
        self.label_4.setText(_translate("MainWindow", "Referebce  "))
        self.label_21.setText(_translate("MainWindow", "Full Name  "))
        self.label_22.setText(_translate("MainWindow", "UserName "))
        self.label_23.setText(_translate("MainWindow", "Passworld  "))
        self.label_24.setText(_translate("MainWindow", "Roles"))
        self.user_roles.setItemText(1, _translate("MainWindow", "admin"))
        self.user_roles.setItemText(2, _translate("MainWindow", "client"))
        self.label_25.setText(_translate("MainWindow", "Contact      "))
        self.label_26.setText(_translate("MainWindow", "Address      "))
        self.user_text_changing.setText(_translate("MainWindow", "Allow text change"))
        self.user_btn_search.setText(_translate("MainWindow", "Search For User"))
        item = self.user_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.user_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Reference"))
        item = self.user_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Full Name"))
        item = self.user_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Username"))
        item = self.user_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Role"))
        item = self.user_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Contact"))
        item = self.user_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Address"))
        self.user_btn_add.setText(_translate("MainWindow", "User Add"))
        self.user_btn_update.setText(_translate("MainWindow", "Update User"))
        self.user_btn_delete.setText(_translate("MainWindow", "Delete User"))
        self.book.setTabText(self.book.indexOf(self.Users), _translate("MainWindow", "Users"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuBook.setTitle(_translate("MainWindow", "Book"))
        self.menuCategory.setTitle(_translate("MainWindow", "Category"))
        self.menuSale.setTitle(_translate("MainWindow", "Sale"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.action_Edit.setText(_translate("MainWindow", "&Edit"))
        self.action_Delete.setText(_translate("MainWindow", "&Delete"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
    
   

    #####################[set Validations]###########################
        self.book_id.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.book_id))
        self.book_quantity.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.book_quantity))
        self.book_price.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*(\.\d*)?"), self.book_price))

        self.book_details_id.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.book_details_id))
        self.book_details_pages.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.book_details_pages))
        self.book_details_pages.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.book_details_pages))
        
        self.category_id.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.category_id))
        
        self.user_id.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.user_id))

        self.sale_add_quantity.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.sale_add_quantity))
        self.sale_quantity_edit.setValidator( QtGui.QRegExpValidator(QtCore.QRegExp("\d*"), self.sale_quantity_edit))
        
       
    
    ###################[]############################################
    ######[set tables column as stretch size]#########
        userheader = self.user_table.horizontalHeader()
        userheader.setSectionResizeMode(QHeaderView.Stretch)
        categoryheader = self.category_table.horizontalHeader()
        categoryheader.setSectionResizeMode(QHeaderView.Stretch)
        saleheader = self.sale_table.horizontalHeader()
        saleheader.setSectionResizeMode(QHeaderView.Stretch)
        bookheader = self.book_table.horizontalHeader()
        bookheader.setSectionResizeMode(QHeaderView.Stretch)
    #####[end of set tables column as stretch size]########
    
    

    # retranslateUi
        #coder changes goes here
        self.date  = datetime.datetime.now()
        self.book_controller=None
        self.sale_controller=None
        self.user_controller=None
        self.book_details_controller=None
        self.category_controller=None

        self.userid=1
        self.connect_events()
        self.updatesales()
        self.updatebooks()
        self.updateusers()
        self.updatecategory()
        
        

#User Comment 
    def updatesales(self):
        self.sale_controller         = saleController()
        self.sale_id_edit.addItems(list(map(lambda x:str(x.id),self.sale_controller.getall())))

    def updatebooks(self):
        self.book_controller         = bookController()
        self.book_details_controller = bookdetailsController()
        books = list(map(lambda x:str(x.id),self.book_controller.getall()))
        self.book_details.addItems(list(map(lambda x:str(x.id),self.book_details_controller.getall())))
        self.sale_add_book.addItems(books)
        self.sale_book_edit.addItems(books)
        del books

    def updateusers(self):
        self.user_controller         = userController()
        users = list(map(lambda x:str(x.id),self.user_controller.getall()))
        self.sale_add_client.addItems(users)
        self.sale_client_edit.addItems(users) 
        del users

    def updatecategory(self):
        self.category_controller     = CategoryController()
        self.book_details_category.addItems(list(map(lambda x:str(x.id),self.category_controller.getall())))

    
       
        
        
        
        

        
        

        
        
        
        
        
               
        
        
        
        
         
    def connect_events(self):

        #initial Controllers 
        #self.bookControl = bookController()
    #####################################################
        #connect eventes to functions for book section
        self.book_btn_add.clicked.connect(self.clicked_book_btn_add)
        self.book_btn_update.clicked.connect(self.clicked_book_btn_update)
        self.book_btn_delete.clicked.connect(self.clicked_book_btn_delete)
        self.book_btn_search.clicked.connect(self.clicked_book_btn_search)
        self.book_input_search.textChanged.connect(self.book_input_search_textchanging)
        self.book_table.selectionModel().selectionChanged.connect(self.select_book_items)
        
        #end eventes to functions for book section
    #####################################################
    ##################################
        #connect eventes to functions for category section
        self.category_btn_add.clicked.connect(self.clicked_category_btn_add)
        self.category_btn_update.clicked.connect(self.clicked_category_btn_update)
        self.category_btn_delete.clicked.connect(self.clicked_category_btn_delete)
        self.category_btn_search.clicked.connect(self.clicked_category_btn_search)
        self.category_input_search.textChanged.connect(self.category_input_search_textchanging)
        self.category_table.selectionModel().selectionChanged.connect(self.select_category_items)
        #end eventes to functions for category section
        #####################################################
        #connect eventes to functions for sales section
        self.sale_btn_add_order.clicked.connect(self.clicked_sale_btn_add)
        self.sale_btn_edit_order.clicked.connect(self.clicked_sale_btn_update)
        self.sale_btn_delete_order.clicked.connect(self.clicked_sale_btn_delete)
        self.sale_btn_search.clicked.connect(self.clicked_sale_btn_search)
        self.sale_input_search.textChanged.connect(self.sale_search_textchanging)
        self.sale_table.selectionModel().selectionChanged.connect(self.select_sale_items)
        
        #end eventes to functions for sales section
        #####################################################
        #connect eventes to functions for user section
        self.user_btn_add.clicked.connect(self.clicked_user_btn_add)
        self.user_btn_update.clicked.connect(self.clicked_user_btn_update)
        self.user_btn_delete.clicked.connect(self.clicked_user_btn_delete)
        self.user_btn_search.clicked.connect(self.clicked_user_btn_search)
        self.user_search.textChanged.connect(self.user_search_textchanging)
        self.user_table.selectionModel().selectionChanged.connect(self.select_user_items)
        #end eventes to functions for user section
        #####################################################
        #####################################################

################################[Book & book details]#########################
    ################################
    #click eventes for book section 
   ################################
    #self.bookControl.add(self.book_id,self.book_title,self.book_author,self.book_quantity,self.book_price,self.book_details)
    #self.book_id
    #self.book_title.text(),
    #self.book_author.text(),
    #self.book_quantity.text(),
    #self.book_price.text(),
    #self.book_details.text()
    
    #self.book_details_id
    #self.book_details_language
    #self.book_details_pages
    #self.book_details_isbn_10
    #self.book_details_isbn_13
    #self.book_details_weight
    #self.book_details_dementions
    #self.book_details_category
    #self.book_search
    #self.book_table
    #click_add event
   ############################
    def clicked_book_btn_add(self):
        self.book_controller = bookController()
        self.book_details_controller = bookdetailsController()
        if  self.book_details_id.text()==""or\
            self.book_details_language.text()==""or\
            self.book_details_pages.text()==""or\
            self.book_details_isbn_10.text()==""or\
            self.book_details_isbn_13.text()==""or\
            self.book_details_weight.text()==""or\
            self.book_details_dementions.text()==""or\
            self.book_details_description.text()==""or\
            self.book_details_category.currentText()=="" or \
            self.book_id.text()=="" or \
            self.book_title.text() == "" or \
            self.book_author.text() == "" or \
            self.book_quantity.text() == "" or \
            self.book_price.text() == "" or \
            self.book_details.currentText() == "" :
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            bkdetails = self.book_details_controller.add(
                                            self.book_details_id.text(),                # id
                                            self.book_details_language.text(),          # language
                                            self.book_details_pages.text(),             # pages number
                                            self.book_details_isbn_10.text(),           # isbn 10 ref
                                            self.book_details_isbn_13.text(),           # isbn 13 ref
                                            self.book_details_weight.text(),            # weight
                                            self.book_details_dementions.text(),        # dementions
                                            self.book_details_description.text(),       # description
                                            str(self.date.strftime("%Y-%m-%d")),        # published date
                                            self.userid,                                # publisher id
                                            self.book_details_category.currentText()    # book category id
                                    )
            if bkdetails!=None:
                self.book_details.addItem(self.book_details_id.text())  
                self.book_details.setCurrentIndex(self.book_details.count()-1)  
                bk = self.book_controller.add(
                                        self.book_id.text(),
                                        self.book_title.text(),
                                        self.book_author.text(),
                                        self.book_quantity.text(),
                                        self.book_price.text(),
                                        self.book_details.currentText()
                                    )
                if bk != None:
                    self.sale_add_book.addItem(self.book_id.text())
                    self.sale_id_edit.addItem(self.book_id.text())
            self.updatebooks()
                            
    def clicked_book_btn_update(self):
        if  self.book_details_id.text()==""or\
            self.book_details_language.text()==""or\
            self.book_details_pages.text()==""or\
            self.book_details_isbn_10.text()==""or\
            self.book_details_isbn_13.text()==""or\
            self.book_details_weight.text()==""or\
            self.book_details_dementions.text()==""or\
            self.book_details_description.text()==""or\
            self.book_details_category.currentText()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            self.book_controller = bookController()
            self.book_details_controller = bookdetailsController()
            bkdetails = self.book_details_controller.update(
                                            self.book_details_id.text(),                # id
                                            self.book_details_language.text(),          # language
                                            self.book_details_pages.text(),             # pages number
                                            self.book_details_isbn_10.text(),           # isbn 10 ref
                                            self.book_details_isbn_13.text(),           # isbn 13 ref
                                            self.book_details_weight.text(),            # weight
                                            self.book_details_dementions.text(),        # dementions
                                            self.book_details_description.text(),       # description
                                            str(self.date.strftime("%Y-%m-%d")),        # published date
                                            self.userid,                                # publisher id
                                            self.book_details_category.currentText()    # book category id
                                    )
            bk = self.book_controller.update(
                                    self.book_id.text(),
                                    self.book_title.text(),
                                    self.book_author.text(),
                                    self.book_quantity.text(),
                                    self.book_price.text(),
                                    self.book_details.currentText()
                                )
            self.updatebooks()
    
    def clicked_book_btn_delete(self):
        if  self.book_details_id.text()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","ID Field are required!")
        else:
            self.book_controller = bookController()
            self.book_details_controller = bookdetailsController()
            bkdetails = self.book_details_controller.delete(self.book_details_id.text())
            if bkdetails!=None:  
                bk = self.book_controller.delete(self.book_id.text())
                if bk != None:
                    self.updatebooks()
                    
            self.updatebooks()

    def clicked_book_btn_search(self):
        self.book_controller = bookController()
        self.book_table.setRowCount(0)
        if self.book_input_search.text() != "":
            for line,row in enumerate(self.book_controller.search(self.book_input_search.text())):
                self.book_table.setRowCount(line+1)
                self.book_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                self.book_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.title)))
                self.book_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.author)))
                self.book_table.setItem(line,3,QtWidgets.QTableWidgetItem(str(row.price)))
                self.book_table.setItem(line,4,QtWidgets.QTableWidgetItem(str(row.quantity)))
          
    def book_input_search_textchanging(self,text):
        self.book_controller = bookController()
        self.book_table.setRowCount(0)
        if self.book_text_change.isChecked():
            if self.book_input_search.text() != "":
                for line,row in enumerate(self.book_controller.search(self.book_input_search.text())):
                    self.book_table.setRowCount(line+1)
                    self.book_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                    self.book_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.title)))
                    self.book_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.author)))
                    self.book_table.setItem(line,3,QtWidgets.QTableWidgetItem(str(row.price)))
                    self.book_table.setItem(line,4,QtWidgets.QTableWidgetItem(str(row.quantity)))

    def select_book_items(self,selected,deselected):
        self.book_controller = bookController()
        self.book_details_controller = bookdetailsController()
        try:
            index = self.book_table.selectionModel().currentIndex().row()
            id = self.book_table.item(index,0).text()
            book = self.book_controller.getById(id)
            bookdetails = self.book_details_controller.getById(book.book_details)

            self.book_id.setText(str(book.id))
            self.book_title.setText(str(book.title))
            self.book_author.setText(str(book.author))
            self.book_quantity.setText(str(book.quantity))
            self.book_price.setText(str(book.price))
            self.book_details.setCurrentText(str(book.book_details))

            self.book_details_id.setText(str(bookdetails.id))
            self.book_details_language.setText(str(bookdetails.langauge))
            self.book_details_pages.setText(str(bookdetails.pages))
            self.book_details_isbn_10.setText(str(bookdetails.isbn_10))
            self.book_details_isbn_13.setText(str(bookdetails.isbn_13))
            self.book_details_weight.setText(str(bookdetails.book_weight))
            self.book_details_dementions.setText(str(bookdetails.dementions))
            self.book_details_description.setText(str(bookdetails.description))
            self.book_details_category.setCurrentText(str(bookdetails.category))
            
        except Exception as err:
            pass
    
    #end of eventes for book section
    ################################
################################[end of Book]#################################

################################[Category]####################################
   ################################
    #self.category_id.text()
    #self.category_label.text()
    #self.category_description

    #self.category_input_search
    #self.category_table
    #end of eventes for Categories section
   ##########################################
    #click eventes for Categories section
    def clicked_category_btn_add(self):
        if  self.category_id.text()=="" or\
            self.category_label.text()=="" or\
            self.category_description.toPlainText()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            self.category_controller=CategoryController()
            self.category_controller.add(self.category_id.text(),
                                        self.category_label.text(),
                                        self.category_description.toPlainText()
                                        )
            self.updatecategory()
        
    def clicked_category_btn_update(self):
        if  self.category_id.text()=="" or\
            self.category_label.text()=="" or\
            self.category_description.toPlainText()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            self.category_controller=CategoryController()
            self.category_controller.update(self.category_id.text(),
                                            self.category_label.text(),
                                            self.category_description.toPlainText()
                                        )
            self.updatecategory()
    
    def clicked_category_btn_delete(self):
        if  self.category_id.text()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","ID Field are required!")
        else:
            self.category_controller=CategoryController()
            self.category_controller.delete(self.category_id.text())
            self.updatecategory()

    def clicked_category_btn_search(self):
        self.category_controller = CategoryController()
        self.category_table.setRowCount(0)
        if self.category_input_search.text() != "":
            for line,row in enumerate(self.category_controller.search(self.category_input_search.text())):
                self.category_table.setRowCount(line+1)
                self.category_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                self.category_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.label)))
                self.category_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.description)))
    
    def category_input_search_textchanging(self,text):
        self.category_controller = CategoryController()
        self.category_table.setRowCount(0)
        if self.category_text_change.isChecked():
            if self.category_input_search.text() != "":
                for line,row in enumerate(self.category_controller.search(self.category_input_search.text())):
                    self.category_table.setRowCount(line+1)
                    self.category_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                    self.category_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.label)))
                    self.category_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.description)))            

    def select_category_items(self,selected,deselected):
        try:
            index = self.category_table.selectionModel().currentIndex().row()
            self.category_id.setText(str(self.category_table.item(index,0).text()))
            self.category_label.setText(str(self.category_table.item(index,1).text()))
            self.category_description.setPlainText(str(self.category_table.item(index,2).text()))
        except Exception as err:
            print(err)
################################[end of category]#############################

################################[USER]########################################
  ################################
    #click eventes for Users section
    #self.user_id
    #self.user_reference
    #self.user_fullname
    #self.user_username
    #self.user_passowrd
    #self.user_roles
    #self.user_contact
    #self.user_address
    #self.user_search
    #self.user_table
  ##################################
    def clicked_user_btn_add(self):
        if  self.user_id.text()=="" or \
            self.user_reference.text()=="" or \
            self.user_fullname.text()=="" or \
            self.user_username.text()=="" or \
            self.user_passowrd.text()=="" or \
            self.user_roles.currentText()=="" or \
            self.user_contact.text()=="" or \
            self.user_address.toPlainText()=="" :
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            self.user_controller = userController()
            self.user_controller.add(  
                    self.user_id.text(),
                    self.user_reference.text(),
                    self.user_fullname.text(),
                    self.user_username.text(),
                    self.user_passowrd.text(),
                    self.user_roles.currentText(),
                    self.user_contact.text(),
                    self.user_address.toPlainText()
            )
            self.updateusers()

    def clicked_user_btn_update(self):
        if  self.user_id.text()=="" or \
            self.user_reference.text()=="" or \
            self.user_fullname.text()=="" or \
            self.user_username.text()=="" or \
            self.user_passowrd.text()=="" or \
            self.user_roles.currentText()=="" or \
            self.user_contact.text()=="" or \
            self.user_address.toPlainText()=="" :
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            self.user_controller = userController()
            self.user_controller.update(  
                    self.user_id.text(),
                    self.user_reference.text(),
                    self.user_fullname.text(),
                    self.user_username.text(),
                    self.user_passowrd.text(),
                    self.user_roles.currentText(),
                    self.user_contact.text(),
                    self.user_address.toPlainText()
            )
            self.updateusers()
    
    def clicked_user_btn_delete(self):
        if  self.user_id.text()==""  :
            self.alert("Some Thing Wrrong!","You missed some field!","ID Field are required!")
        else:
            self.user_controller = userController()
            self.user_controller.delete(  
                    self.user_id.text()
            )
            self.updateusers()   
        
    def clicked_user_btn_search(self):
        self.user_table.setRowCount(0)
        if self.user_search.text() != "":
            self.user_controller = userController()
            for line,row in enumerate(self.user_controller.search(self.user_search.text())):
                self.user_table.setRowCount(line+1)
                self.user_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                self.user_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.reference)))
                self.user_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.fullname)))
                self.user_table.setItem(line,3,QtWidgets.QTableWidgetItem(str(row.username)))
                self.user_table.setItem(line,4,QtWidgets.QTableWidgetItem(str(row.password)))
                self.user_table.setItem(line,5,QtWidgets.QTableWidgetItem(str(row.role)))
                self.user_table.setItem(line,6,QtWidgets.QTableWidgetItem(str(row.contact)))
                self.user_table.setItem(line,7,QtWidgets.QTableWidgetItem(str(row.address)))
        
    def user_search_textchanging(self,txt):
        if self.user_text_changing.isChecked():
            self.user_table.setRowCount(0)
            if self.user_search.text() != "":
                self.user_controller = userController()
                for line,row in enumerate(self.user_controller.search(self.user_search.text())):
                    self.user_table.setRowCount(line+1)
                    self.user_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                    self.user_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.reference)))
                    self.user_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.fullname)))
                    self.user_table.setItem(line,3,QtWidgets.QTableWidgetItem(str(row.username)))
                    self.user_table.setItem(line,4,QtWidgets.QTableWidgetItem(str(row.role)))
                    self.user_table.setItem(line,5,QtWidgets.QTableWidgetItem(str(row.contact)))
                    self.user_table.setItem(line,6,QtWidgets.QTableWidgetItem(str(row.address)))

    def select_user_items(self,selected,deselected):
        try:
            index = self.user_table.selectionModel().currentIndex().row()
            self.user_id.setText(str(self.user_table.item(index,0).text()))
            self.user_reference.setText(str(self.user_table.item(index,1).text()))
            self.user_fullname.setText(str(self.user_table.item(index,2).text()))
            self.user_username.setText(str(self.user_table.item(index,3).text()))
            self.user_roles.setCurrentText(str(self.user_table.item(index,4).text()))
            self.user_contact.setText(str(self.user_table.item(index,5).text()))
            self.user_address.setPlainText(str(self.user_table.item(index,6).text()))
        except Exception as err:
            print(err)
    #end of eventes for Users section
    ################################
################################[end of user ]################################


################################[Sale]########################################
  ################################
    #click eventes for Sale section
    #self.sale_add_client
    #self.sale_add_book
    #self.sale_add_quantity
    #self.sale_id_edit
    #self.sale_client_edit
    #self.sale_book_edit
    #self.sale_quantity_edit
    #self.sale_input_search
    #self.sale_table
  ####
    def clicked_sale_btn_add(self):
        if  self.sale_add_client.currentText()==""or\
            self.sale_add_book.currentText()==""or\
            self.sale_add_quantity.text()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            self.sale_controller = saleController()
            self.book_controller = bookController()
            book = self.book_controller.getById(self.sale_add_book.currentText())
            if book != None and book.quantity >= int(self.sale_add_quantity.text()):
                self.sale_controller.add(None,
                                        self.sale_add_client.currentText(),
                                        self.sale_add_book.currentText(),
                                        self.sale_add_quantity.text(),
                                        self.userid,
                                        str(self.date.strftime("%Y-%m-%d")))
                book.quantity =  int(book.quantity) - int(self.sale_add_quantity.text())
                self.book_controller.update(book.id,
                                            book.title,
                                            book.author,
                                            book.price,
                                            book.quantity,
                                            book.book_details)
                self.updatesales()
        
    def clicked_sale_btn_update(self):
        if  self.sale_add_client.currentText()==""or\
            self.sale_add_book.currentText()==""or\
            self.sale_add_quantity.text()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","All Field are required!")
        else:
            self.sale_controller = saleController()
            self.book_controller = bookController()
            book = self.book_controller.getById(self.sale_book_edit.currentText())
            sale = self.sale_controller.getById(self.sale_id_edit.currentText())
            if book != None and sale != None and int(book.quantity) + int(sale.quantity) >= int(self.sale_quantity_edit.text()):
                self.sale_controller.update(self.sale_id_edit.currentText(),
                                            self.sale_client_edit.currentText(),
                                            self.sale_book_edit.currentText(),
                                            self.sale_quantity_edit.text(),
                                            self.userid,
                                            str(self.date.strftime("%Y-%m-%d")))
                book.quantity =  int(book.quantity)+int(sale.quantity) - int(self.sale_quantity_edit.text())
                self.book_controller.update(book.id,
                                            book.title,
                                            book.author,
                                            book.price,
                                            book.quantity,
                                            book.book_details)
                self.updatesales()

    def clicked_sale_btn_delete(self):
        if  self.sale_add_client.currentText()=="":
            self.alert("Some Thing Wrrong!","You missed some field!","ID Field are required!")
        else:
            self.sale_controller = saleController()
            self.sale_controller.delete(self.sale_id_edit.currentText())
            self.updatesales()

    def clicked_sale_btn_search(self):
        self.sale_controller = saleController()
        self.sale_table.setRowCount(0)
        if self.sale_input_search.text() != "":
            for line,row in enumerate(self.sale_controller.search(self.sale_input_search.text())):
                self.sale_table.setRowCount(line+1)
                self.sale_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                self.sale_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.client)))
                self.sale_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.book)))
                self.sale_table.setItem(line,3,QtWidgets.QTableWidgetItem(str(row.quantity)))
                self.sale_table.setItem(line,4,QtWidgets.QTableWidgetItem(str(row.user)))            
                self.sale_table.setItem(line,5,QtWidgets.QTableWidgetItem(str(row.date_created)))            
   
    def select_sale_items(self,selected,deselected):
        print("selected")
        try:
            index = self.sale_table.selectionModel().currentIndex().row()
            self.sale_id_edit.setCurrentText(str(self.sale_table.item(index,0).text()))
            self.sale_client_edit.setCurrentText(str(self.sale_table.item(index,1).text()))
            self.sale_book_edit.setCurrentText(str(self.sale_table.item(index,2).text()))
            self.sale_quantity_edit.setText(str(self.sale_table.item(index,3).text()))
            
            self.sale_cleint_add.setCurrentText(str(self.sale_table.item(index,1).text()))
            self.sale_book_add.setCurrentText(str(self.sale_table.item(index,2).text()))
            self.sale_quantity_add.setText(str(self.sale_table.item(index,3).text()))
        except Exception as err:
            print(err)
    
    def sale_search_textchanging(self):
        self.sale_controller = saleController()
        self.sale_table.setRowCount(0)
        if self.sale_text_change.isChecked():
            if self.sale_input_search.text() != "":
                for line,row in enumerate(self.sale_controller.search(self.sale_input_search.text())):
                    self.sale_table.setRowCount(line+1)
                    self.sale_table.setItem(line,0,QtWidgets.QTableWidgetItem(str(row.id)))
                    self.sale_table.setItem(line,1,QtWidgets.QTableWidgetItem(str(row.client)))
                    self.sale_table.setItem(line,2,QtWidgets.QTableWidgetItem(str(row.book)))
                    self.sale_table.setItem(line,3,QtWidgets.QTableWidgetItem(str(row.quantity)))
                    self.sale_table.setItem(line,4,QtWidgets.QTableWidgetItem(str(row.user)))            
                    self.sale_table.setItem(line,5,QtWidgets.QTableWidgetItem(str(row.date_created)))            

    #end of eventes for Sale section
    ################################
################################[end of Sale]#################################

    def alert(self,title="",message="",detais=""):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setDetailedText(detais)
        msgBox.exec_()




def run():    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = View()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
