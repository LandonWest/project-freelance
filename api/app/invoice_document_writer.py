from reportlab.lib.colors import blue
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas


class InvoiceDocumentWriter(object):
    """docstring for InvoiceDocument"""

    def __init__(
        self, canvas_obj, font_name="Helvetica", font_size=12, font_color="black",
    ):
        self._canvas = canvas_obj
        self._font_name = font_name
        self._font_size = font_size
        self._font_color = font_color

    @property
    def canvas(self):
        return self._canvas

    @property
    def font_name(self):
        return self._font_name

    @property
    def font_size(self):
        return self._font_size

    @property
    def font_color(self):
        return self._font_color

    def draw_header(self, freelancer_contact_info, font_name="Helvetica", font_size=10, font_color="black"):
        self._canvas.setFont(font_name, font_size)
        self._canvas.setFillColor(font_color)

        # Freelancer Company Info col. 1
        self._canvas.drawRightString(4.75 * inch, 10 * inch, freelancer_contact_info['phone'])
        self._canvas.drawRightString(4.75 * inch, 9.8 * inch, freelancer_contact_info['email'])
        self._canvas.drawRightString(4.75 * inch, 9.6 * inch, freelancer_contact_info['personal_url_1'])

        # Freelancer Company Info col. 2
        self._canvas.setFont("Helvetica", 10)
        name_or_company = freelancer_contact_info.get('company') or freelancer_contact_info['full_name']
        self._canvas.drawRightString(7.75 * inch, 10 * inch, name_or_company)
        self._canvas.drawRightString(7.75 * inch, 9.8 * inch, freelancer_contact_info['full_street'])
        self._canvas.drawRightString(7.75 * inch, 9.6 * inch, f"{freelancer_contact_info['city']}, {freelancer_contact_info['state']}")
        self._canvas.drawRightString(7.75 * inch, 9.4 * inch, freelancer_contact_info['postal_code'])

        # Header bottom border line
        self._canvas.line(0, 9 * inch, 8.5 * inch, 9 * inch)

        # self._canvas.drawCentredString(4.25 * inch, 10 * inch, text)
        self._canvas.setFont("Helvetica-Bold", 24)
        self._canvas.drawString(0.75 * inch, 10 * inch, 'INVOICE')

    def draw_line_item_grid(self, top_point=8.5, bottom_point=3):
        # draw rectangle
        # self._canvas.rect(0.5*inch, 3*inch, 8*inch, 3.25*inch, fill=0)
        def _get_y_axis_coordinates(top_point, bottom_point):
            list = []
            while top_point > bottom_point:
                list.append(top_point * 72)
                top_point -= 0.25
            list.reverse()
            return list

        y_axis_list = _get_y_axis_coordinates(top_point, bottom_point)
        self._canvas.grid(
            # Description, Quantity, Unit Price, Total Price
            [
                0.75 * inch,
                5.5 * inch,
                6.25 * inch,
                7 * inch,
                7.75 * inch,
            ],  # x-axis grid line locations
            y_axis_list,  # y-axis grid line locations
        )

    def draw_line_items_column_names(self, font_name="Helvetica-Bold", font_size=14, font_color="black"):
        self._canvas.setFillColor(font_color)
        self._canvas.setFont(font_name, font_size)

        bottom = 8.3 * inch
        self._canvas.drawString(1 * inch, bottom, 'Description')
        self._canvas.drawString(5.1 * inch, bottom, 'Quantity')
        self._canvas.drawString(6.26 * inch, bottom, 'Unit Price')
        self._canvas.drawString(7.1 * inch, bottom, 'Total')

    def draw_line_item(self, font_name="Helvetica-Bold", font_size=12, font_color="black"):
        pass

    def draw_line_items(self, font_name="Helvetica", font_size=12, font_color="black"):
        self._canvas.setFillColor(font_color)
        self._canvas.setFont(font_name, font_size)

        from_left, from_bottom = 1, 8.05
        for index, n in enumerate(range(0, 8)):
            self._canvas.drawString(
                from_left * inch,
                from_bottom * inch,
                f"Did some work on some stuff, line {index + 1}",
            )
            from_bottom -= 0.25

    def draw_footer(self, text, font_name="Helvetica-Oblique", font_size=8, font_color="black"):
        self._canvas.setFillColor(font_color)
        self._canvas.setFont(font_name, font_size)

        self._canvas.drawCentredString(4.25 * inch, 0.75 * inch, text)

    def save(self):
        self._canvas.save()


if __name__ == "__main__":

    freelancer_contact_info = {
        'full_name': 'John Doe',
        'full_street': '1600 Pennsylvania Ave',
        'city': 'Washington',
        'state': 'DC',
        'postal_code': '20500',
        'email': 'example@email.com',
        'phone': '410-867-5309',
        'personal_url_1': 'exampleco.com'
    }

    canvas = Canvas("test.pdf", pagesize=LETTER)
    inv_doc = InvoiceDocumentWriter(canvas)

    inv_doc.draw_header(freelancer_contact_info)
    inv_doc.draw_line_item_grid()
    inv_doc.draw_line_items_column_names()
    inv_doc.draw_line_items()
    inv_doc.draw_footer("Example Co. Copywrite 2020")
    inv_doc.save()
