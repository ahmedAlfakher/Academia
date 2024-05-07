# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CouncilMember(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        employee: DF.Link
        member_name: DF.Data | None
        member_role: DF.Literal["", "Council Head", "Council Member", "Council Reporter"]
        parent: DF.Data
        parentfield: DF.Data
        parenttype: DF.Data
    # end: auto-generated types
    pass

    @property
    def member_name(self):
    	return frappe.get_value('Employee', self.faculty_member, 'employee_name')
