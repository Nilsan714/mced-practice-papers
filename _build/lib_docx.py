"""Minimal stdlib .docx writer (no third-party deps). Inline **bold** supported."""
import zipfile
from xml.sax.saxutils import escape

FONT = 'Nirmala UI'
CT = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
      '<Default Extension="xml" ContentType="application/xml"/>'
      '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
      '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
      '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>')
RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
DOCRELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
           '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
           '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/></Relationships>')
NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
RF = '<w:rFonts w:ascii="%s" w:hAnsi="%s" w:cs="%s" w:eastAsia="%s"/>' % ((FONT,) * 4)


def styles():
    def hd(i, sz, col):
        return ('<w:style w:type="paragraph" w:styleId="Heading%d"><w:name w:val="heading %d"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>'
                '<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="%d"/></w:pPr>'
                '<w:rPr><w:b/><w:color w:val="%s"/><w:sz w:val="%d"/><w:szCs w:val="%d"/></w:rPr></w:style>' % (i, i, i - 1, col, sz, sz))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles %s><w:docDefaults><w:rPrDefault><w:rPr>%s'
            '<w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="en-IN" w:bidi="hi-IN"/></w:rPr></w:rPrDefault>'
            '<w:pPrDefault><w:pPr><w:spacing w:after="80" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
            '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>'
            '<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:pPr><w:jc w:val="center"/><w:spacing w:after="60"/></w:pPr>'
            '<w:rPr><w:b/><w:color w:val="1F3864"/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr></w:style>%s%s%s'
            '<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:tblPr><w:tblBorders>'
            '<w:top w:val="single" w:sz="4" w:color="808080"/><w:left w:val="single" w:sz="4" w:color="808080"/><w:bottom w:val="single" w:sz="4" w:color="808080"/>'
            '<w:right w:val="single" w:sz="4" w:color="808080"/><w:insideH w:val="single" w:sz="4" w:color="808080"/><w:insideV w:val="single" w:sz="4" w:color="808080"/>'
            '</w:tblBorders><w:tblCellMar><w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style></w:styles>'
            % (NS, RF, hd(1, 30, '1F3864'), hd(2, 26, '2F5496'), hd(3, 23, '2F5496')))


def footer(label):
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr %s><w:p><w:pPr><w:jc w:val="center"/></w:pPr>'
            '<w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t xml:space="preserve">%s  |  Page </w:t></w:r>'
            '<w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:instrText> PAGE </w:instrText></w:r>'
            '<w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:t>1</w:t></w:r>'
            '<w:r><w:rPr><w:sz w:val="18"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r></w:p></w:ftr>' % (NS, escape(label)))


def runs(text, bold=False, italic=False, size=None, color=None):
    out = []
    for i, part in enumerate(text.split('**')):
        if part == '':
            continue
        b = bold or (i % 2 == 1)
        pr = ('<w:b/><w:bCs/>' if b else '') + ('<w:i/><w:iCs/>' if italic else '')
        if color:
            pr += '<w:color w:val="%s"/>' % color
        if size:
            pr += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size * 2, size * 2)
        out.append('<w:r><w:rPr>%s</w:rPr><w:t xml:space="preserve">%s</w:t></w:r>' % (pr, escape(part)))
    return ''.join(out)


class Doc:
    def __init__(self, footer_label):
        self.b = []
        self.footer_label = footer_label

    def p(self, text='', bold=False, italic=False, size=None, color=None, align=None, indent=0, keep_next=False,
          keep_lines=False, shade=None, before=None, after=None, style=None):
        pp = ''
        if style:
            pp += '<w:pStyle w:val="%s"/>' % style
        if keep_next:
            pp += '<w:keepNext/>'
        if keep_lines:
            pp += '<w:keepLines/>'
        if shade:
            pp += '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % shade
        if before is not None or after is not None:
            pp += '<w:spacing %s%s/>' % ('w:before="%d" ' % before if before is not None else '', 'w:after="%d"' % after if after is not None else '')
        if indent:
            pp += '<w:ind w:left="%d"/>' % indent
        if align:
            pp += '<w:jc w:val="%s"/>' % align
        self.b.append('<w:p><w:pPr>%s</w:pPr>%s</w:p>' % (pp, runs(text, bold, italic, size, color)))

    def title(self, t):
        self.p(t, style='Title')

    def h(self, level, t):
        self.p(t, style='Heading%d' % level)

    def bullets(self, items, indent=360):
        for it in items:
            self.p('•  ' + it, indent=indent, keep_lines=True, after=40)

    def pagebreak(self):
        self.b.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def table(self, rows, widths=None, header=True, size=10, shade_header='D9E2F3', center_cols=()):
        n = len(rows[0])
        widths = widths or [int(9600 / n)] * n
        x = ['<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="%d" w:type="dxa"/><w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>%s</w:tblGrid>'
             % (sum(widths), ''.join('<w:gridCol w:w="%d"/>' % w for w in widths))]
        for ri, row in enumerate(rows):
            x.append('<w:tr><w:trPr><w:cantSplit/>%s</w:trPr>' % ('<w:tblHeader/>' if header and ri == 0 else ''))
            for ci, cell in enumerate(row):
                sh = '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % shade_header if header and ri == 0 else ''
                jc = '<w:jc w:val="center"/>' if ci in center_cols else ''
                paras = ''.join('<w:p><w:pPr><w:spacing w:after="20"/>%s</w:pPr>%s</w:p>' % (jc, runs(line, bold=(header and ri == 0), size=size))
                                for line in str(cell).split('\n'))
                x.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>%s</w:tcPr>%s</w:tc>' % (widths[ci], sh, paras))
            x.append('</w:tr>')
        x.append('</w:tbl>')
        self.b.append(''.join(x))
        self.p('', after=40)

    def save(self, path):
        body = ''.join(self.b)
        doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document %s xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>%s'
               '<w:sectPr><w:footerReference w:type="default" r:id="rId2"/><w:pgSz w:w="11906" w:h="16838"/>'
               '<w:pgMar w:top="1000" w:right="1100" w:bottom="1000" w:left="1100" w:header="500" w:footer="500" w:gutter="0"/></w:sectPr></w:body></w:document>' % (NS, body))
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr('[Content_Types].xml', CT)
            z.writestr('_rels/.rels', RELS)
            z.writestr('word/document.xml', doc)
            z.writestr('word/styles.xml', styles())
            z.writestr('word/footer1.xml', footer(self.footer_label))
            z.writestr('word/_rels/document.xml.rels', DOCRELS)
