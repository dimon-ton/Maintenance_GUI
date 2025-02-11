from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.pdfgen import canvas



# add font

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from subprocess import Popen # open pdf for automatically



class Report(object):
    # constructor
    def __init__(self):
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()


    def createPDF(self, filename, data):
        self.doc = SimpleDocTemplate(filename, pagesize=A4, leftMargin=30, rightMargin=30, topMargin=50, bottomMargin=10)
        self.story = [Spacer(1, 1*cm)]
        self.createTable(data)
        self.doc.build(self.story, onFirstPage=self.createDocument)

        print("create file : {}".format(filename))

    def createCoord(self, x, y, unit=1):
        x, y = x * unit, self.height -  y * unit
        return x, y
    

    def createDocument(self, canvas, doc):
        pdfmetrics.registerFont(TTFont('normalFont', './fonts/THSarabunNew.ttf'))
        pdfmetrics.registerFont(TTFont('boldFont', './fonts/THSarabunNew Bold.ttf'))
        pdfmetrics.registerFont(TTFont('italicFont', './fonts/THSarabunNew Italic.ttf'))
        pdfmetrics.registerFont(TTFont('boldItalicFont', './fonts/THSarabunNew BoldItalic.ttf'))


        self.c = canvas
        normal = self.styles["Title"]

        htext = "<font size=18 name='boldFont'>บริษัท อังเคิล เมนเทนแนนซ์ จำกัด</font>"
        h = Paragraph(htext, normal)
        h.wrapOn(self.c, self.width, self.height)
        h.drawOn(self.c, *self.createCoord(0, 12, mm))

        eng_text = "<font size=18 name='boldFont'>UNCLE MAINTENANCE CO.,LTD.</font>"
        h = Paragraph(eng_text, normal)
        h.wrapOn(self.c, self.width, self.height)
        h.drawOn(self.c, *self.createCoord(0, 18, mm))

        eng_text = "<font size=18 name='boldFont'>ตารางแสดงรายการซ่อมบำรุงรักษา</font>"
        h = Paragraph(eng_text, normal)
        h.wrapOn(self.c, self.width, self.height)
        h.drawOn(self.c, *self.createCoord(0, 28, mm))
    
    def createTable(self, datatext):
        pdfmetrics.registerFont(TTFont('normalFont', './fonts/THSarabunNew.ttf'))
        pdfmetrics.registerFont(TTFont('boldFont', './fonts/THSarabunNew Bold.ttf'))
        pdfmetrics.registerFont(TTFont('italicFont', './fonts/THSarabunNew Italic.ttf'))
        pdfmetrics.registerFont(TTFont('boldItalicFont', './fonts/THSarabunNew BoldItalic.ttf'))

        styles = getSampleStyleSheet()
        styleNormal = styles["Normal"]
        styleTitle = styles["Title"]


        # Header of Table
        CH1 = Paragraph("<font size=13 name='boldFont'>TSID</font>", styleTitle)
        CH2 = Paragraph("<font size=13 name='boldFont'>ชื่อ</font>", styleTitle)
        CH3 = Paragraph("<font size=13 name='boldFont'>แผนก</font>", styleTitle)
        CH4 = Paragraph("<font size=13 name='boldFont'>อุปกรณ์</font>", styleTitle)
        CH5 = Paragraph("<font size=13 name='boldFont'>อาการเสีย</font>", styleTitle)
        CH6 = Paragraph("<font size=13 name='boldFont'>หมายเลข</font>", styleTitle)
        CH7 = Paragraph("<font size=13 name='boldFont'>เบอร์โทรศัพท์ผู้แจ้ง</font>", styleTitle)
        CH8 = Paragraph("<font size=13 name='boldFont'>สถานะ</font>", styleTitle)


       # Table
        data = [
                ['หน้าที่ 1', '', '', '', '', '', '', ''],
                [CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH8]
            ]


        tableThatSplitsOverPages = Table(data, [2 * cm, 2.5 * cm, 2.5 * cm, 4 * cm, 1.8 * cm, 1.8 * cm, 2.2 * cm, 1.5 * cm], repeatRows=1)
        tableStyle = TableStyle(
            [
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 1, colors.black)
            ]
        )


        tableThatSplitsOverPages.setStyle(tableStyle)
        self.story.append(tableThatSplitsOverPages)



if __name__ == '__main__':

    report = Report()
    data = []
    report.createPDF('test.pdf', data)
    print('Done!')
    Popen('test.pdf', shell=True)