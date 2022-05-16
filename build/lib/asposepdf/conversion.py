import jpype
import jpype.imports

class Conversion(object):
    def __init__(self, licence_path):
        self.Document = jpype.JClass("com.aspose.pdf.Document")
        self.Image = jpype.JClass("com.aspose.pdf.Image")
        self.License = jpype.JClass("com.aspose.pdf.License")
        self.DocSaveOptions = jpype.JClass("com.aspose.pdf.DocSaveOptions")
        self.SvgLoadOptions = jpype.JClass("com.aspose.pdf.SvgLoadOptions")

        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = self.License()
            self.aspose_license.SetLicense(self.licence_path)

    def convert_image_to_PDF(self, infile, outfile, height, width):

        # Initialize new Document

        document = self.Document()
        page = document.Pages.Add()
        image = self.Image()
        image.File = infile

        # Set page dimensions

        page.PageInfo.Height = height
        page.PageInfo.Width = width
        page.PageInfo.Margin.Bottom = 0
        page.PageInfo.Margin.Top = 0
        page.PageInfo.Margin.Right = 0
        page.PageInfo.Margin.Left = 0
        page.Paragraphs.Add(image)

        # Save output PDF

        document.Save(outfile)


    def convert_SVG_to_PDF(self, infile, outfile):
        option = self.SvgLoadOptions()

        document = self.Document(infile, option)
        document.Save(outfile)


    def convert_PDF_to_Word(self, infile, outfile):

        document = self.Document(infile)
        option = self.DocSaveOptions()
        option.Format = self.DocSaveOptions.DocFormat.DocX

        # Save the file into MS document format

        document.Save(outfile, option)
