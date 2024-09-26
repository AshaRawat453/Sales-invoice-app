# Copyright (c) 2024, asha rawat and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CustomerDetail(Document):
	def validate(self):
		total_amount=0
		discount = 0
		for item in self.product:
			total_amount+=item.quantity * item.price
			discount += (item.discount / 100) * total_amount
			payable_amount = total_amount - discount

		self.total_amount = total_amount
		self.discount = discount
		self.payable_amount = payable_amount
