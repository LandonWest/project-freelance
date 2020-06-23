from reportlab.lib.colors import blue
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas


class InvoiceDocumentWriter(object):
    """docstring for InvoiceDocument"""

    MARGIN = 0.75
    BILL_TO_HEIGHT = 8.25
    QTY_X_POS = 6
    RATE_X_POS = 7

    def __init__(
        self, canvas_obj, font_name="Helvetica", font_size=12, font_color="black",
    ):
        self._canvas = canvas_obj

        self._canvas.setFont(font_name, font_size)
        self._canvas.setFillColor(font_color)
        self._canvas.saveState()

    def restore_defaults(self):
        self._canvas.restoreState()

    def draw_header_background(self, stroke_color=None, fill_color=None):
        stroke = 1 if stroke_color else 0
        fill = 1 if fill_color else 0
        if stroke_color:
            self._canvas.setStrokeColor(stroke_color)
        if fill_color:
            self._canvas.setFillColor(fill_color)

        self._canvas.rect(0, 9 * inch, 8.5 * inch, 2.5 * inch, stroke=stroke, fill=fill)

    def draw_header_content(
        self,
        freelancer_contact_info,
        font_name="Helvetica",
        font_size=10,
        font_color="black",
    ):
        self._canvas.setFont(font_name, font_size)
        self._canvas.setFillColor(font_color)

        self._canvas.drawRightString(
            4.75 * inch, 10 * inch, freelancer_contact_info["phone"]
        )
        self._canvas.drawRightString(
            4.75 * inch, 9.8 * inch, freelancer_contact_info["email"]
        )
        self._canvas.drawRightString(
            4.75 * inch, 9.6 * inch, freelancer_contact_info["personal_url_1"]
        )

        # Freelancer Company Info col. 2
        self._canvas.setFont("Helvetica", 10)
        name_or_company = (
            freelancer_contact_info.get("company")
            or freelancer_contact_info["full_name"]
        )
        self._canvas.drawRightString(7.75 * inch, 10 * inch, name_or_company)
        self._canvas.drawRightString(
            7.75 * inch, 9.8 * inch, freelancer_contact_info["full_street"]
        )
        self._canvas.drawRightString(
            7.75 * inch,
            9.6 * inch,
            f"{freelancer_contact_info['city']}, {freelancer_contact_info['state']}",
        )
        self._canvas.drawRightString(
            7.75 * inch, 9.4 * inch, freelancer_contact_info["postal_code"]
        )

        # INVOICE headline
        self._canvas.setFont("Helvetica-Bold", 24)
        self._canvas.drawString(self.MARGIN * inch, 10 * inch, "INVOICE")

    def draw_billed_to(
        self,
        client_contact_info,
        font_name="Helvetica",
        font_size=10,
        font_color="grey",
    ):
        text_object = self._canvas.beginText()
        text_object.setFont(font_name, font_size)

        # Billed To Header
        text_object.setTextOrigin(self.MARGIN * inch, self.BILL_TO_HEIGHT * inch)
        text_object.setFillColor(font_color)
        text_object.textLine("Billed To")

        # Client Info Block
        text_object.moveCursor(0, 0.1 * inch)
        text_object.setFillColor("black")
        text_object.textLines(client_info, trim=1)

        self._canvas.drawText(text_object)

    def draw_invoice_number(
        self,
        invoice_num="000000",
        font_name="Helvetica",
        font_size=10,
        font_color="grey",
    ):
        text_object = self._canvas.beginText()
        text_object.setFont(font_name, font_size)

        # Invoice Number Header
        text_object.setTextOrigin(3 * inch, self.BILL_TO_HEIGHT * inch)
        text_object.setFillColor(font_color)
        text_object.textLine("Invoice Number")

        # Invoice Number
        text_object.moveCursor(0, 0.1 * inch)
        text_object.setFillColor("black")
        text_object.textLine(invoice_number)

        self._canvas.drawText(text_object)

    def draw_issued_date(
        self,
        issued_date="00/00/00",
        font_name="Helvetica",
        font_size=10,
        font_color="grey",
    ):
        text_object = self._canvas.beginText()
        text_object.setFont(font_name, font_size)

        # Issued Date Header
        text_object.setTextOrigin(3 * inch, 7.59 * inch)
        text_object.setFillColor(font_color)
        text_object.textLine("Date of Issue")

        # Issued Date
        text_object.moveCursor(0, 0.1 * inch)
        text_object.setFillColor("black")
        text_object.textLine(issued_date)

        self._canvas.drawText(text_object)

    def draw_invoice_total(
        self,
        invoice_total="0.00",
        font_name="Helvetica",
        font_size=10,
        font_color="grey",
    ):
        self._canvas.setFont(font_name, font_size)

        # Invoice Total Header
        self._canvas.setFillColor(font_color)
        self._canvas.drawRightString(
            7.75 * inch, self.BILL_TO_HEIGHT * inch, "Invoice Total"
        )

        # Invoice Total
        self._canvas.setFillColor("black")
        self._canvas.setFont(font_name, 32)
        self._canvas.drawRightString(7.75 * inch, 7.75 * inch, f"${invoice_total}")

    def draw_line_items_header(
        self, font_name="Helvetica-Bold", font_size=12, font_color="black"
    ):
        self._canvas.setFillColor(font_color)
        self._canvas.setFont(font_name, font_size)

        # Divider Line
        # Making this slightly wider than the block of the body
        self._canvas.rect(
            (self.MARGIN - 0.1) * inch, 6.65 * inch, 7.2 * inch, 1, fill=1
        )

        # Column Names
        bottom = 6.3 * inch
        self._canvas.drawString(self.MARGIN * inch, bottom, "Description")
        self._canvas.drawRightString(self.QTY_X_POS * inch, bottom, "Qty.")
        self._canvas.drawRightString(self.RATE_X_POS * inch, bottom, "Rate/Unit")
        self._canvas.drawRightString(7.75 * inch, bottom, "Total")

    def draw_line_item(
        self,
        y_position=5.8,
        item_category="category",
        item_description="a description of the work",
        quantity=1,
        rate=50,
        unit="Hr.",
        font_name="Helvetica",
        font_size=12,
        font_color="black",
    ):
        ### LINE ITEM
        text_object = self._canvas.beginText()
        text_object.setFont(font_name, font_size)
        # Category
        text_object.setTextOrigin(self.MARGIN * inch, y_position * inch)
        text_object.setFillColor(font_color)
        text_object.textLine(item_category)
        # Description
        text_object.moveCursor(0, 1)  # Using Point instead of IN here.
        text_object.setFont(font_name, font_size - 2)
        text_object.setFillColor("lightgrey")
        text_object.textLine(item_description)
        self._canvas.drawText(text_object)

        # Measurements
        self._canvas.setFillColor(font_color)
        self._canvas.setFont(font_name, font_size)
        self._canvas.drawRightString(
            self.QTY_X_POS * inch, y_position * inch, str(quantity)
        )
        rate = f"{rate:.2f}" if "." in str(rate) else str(rate)
        self._canvas.drawRightString(
            self.RATE_X_POS * inch, y_position * inch, f"${rate}/{str(unit)}"
        )
        total = int(quantity) * float(rate)
        self._canvas.drawRightString(
            7.75 * inch, y_position * inch, "${:.2f}".format(total)
        )

    def draw_line_items(
        self,
        line_items=[1, 2, 3, 4],
        font_name="Helvetica",
        font_size=12,
        font_color="black",
    ):
        y_pos = 5.8
        for item in line_items:
            self.draw_line_item(y_position=y_pos)
            y_pos -= 0.5

    def draw_footer(
        self, text, font_name="Helvetica-Oblique", font_size=8, font_color="black"
    ):
        self._canvas.setFillColor(font_color)
        self._canvas.setFont(font_name, font_size)

        self._canvas.drawCentredString(4.25 * inch, self.MARGIN * inch, text)

    def save(self):
        self._canvas.save()


if __name__ == "__main__":

    freelancer_contact_info = {
        "company": "Example Co.",
        "full_name": "John Doe",
        "full_street": "1600 Pennsylvania Ave",
        "city": "Washington",
        "state": "DC",
        "postal_code": "20500",
        "email": "example@email.com",
        "phone": "410-867-5309",
        "personal_url_1": "exampleco.com",
    }
    client_info = """
    Client Company
    Attn: Jane Doe
    123 Hollywood Blvd.
    Suite 410
    Beverley Hills, CA 90210
    """
    invoice_number = "0001234"
    issued_date = "04/15/20"
    invoice_total = "239.06"

    canvas = Canvas("test.pdf", pagesize=LETTER)
    inv_doc = InvoiceDocumentWriter(canvas)

    inv_doc.draw_header_background(fill_color="lightgrey")
    inv_doc.draw_header_content(freelancer_contact_info)
    inv_doc.draw_billed_to(client_info)
    inv_doc.draw_invoice_number(invoice_number)
    inv_doc.draw_issued_date(issued_date)
    inv_doc.draw_invoice_total(invoice_total)
    inv_doc.draw_line_items_header()
    inv_doc.draw_line_item()
    inv_doc.draw_line_items()
    inv_doc.draw_footer("Example Co. Copywrite 2020")
    inv_doc.save()
